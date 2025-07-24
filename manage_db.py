#!/usr/bin/env python
import os
import sys
import django
from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_tracker.settings')
    django.setup()
    
    from transactions.models import Category
    
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
    
    # Create superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superuser created: admin/admin123')
    
    print('Default categories created successfully!')