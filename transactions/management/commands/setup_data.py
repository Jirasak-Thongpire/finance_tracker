from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from transactions.models import Category


class Command(BaseCommand):
    help = 'Setup initial data for the application'

    def handle(self, *args, **options):
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superuser created: admin/admin123')

        # Create default categories
        categories = [
            ('Food & Dining', 'expense', '#dc3545'),
            ('Transportation', 'expense', '#fd7e14'),
            ('Shopping', 'expense', '#6f42c1'),
            ('Entertainment', 'expense', '#e83e8c'),
            ('Bills & Utilities', 'expense', '#28a745'),
            ('Healthcare', 'expense', '#17a2b8'),
            ('Education', 'expense', '#6c757d'),
            ('Groceries', 'expense', '#ffc107'),
            ('Salary', 'income', '#20c997'),
            ('Freelance', 'income', '#007bff'),
            ('Investments', 'income', '#28a745'),
            ('Other Income', 'income', '#6f42c1'),
        ]

        for name, cat_type, color in categories:
            Category.objects.get_or_create(
                name=name,
                defaults={'category_type': cat_type, 'color': color}
            )

        self.stdout.write('Default categories created successfully!')