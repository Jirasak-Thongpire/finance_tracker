"""
WSGI config for finance_tracker project.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_tracker.settings')

# Import Django and setup
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Initialize Django
django.setup()

# Run migrations and create initial data
def setup_database():
    try:
        from django.core.management import call_command
        from django.db import connection
        from django.contrib.auth.models import User
        from transactions.models import Category
        
        # Create tables if they don't exist
        with connection.schema_editor() as schema_editor:
            # Check if tables exist, if not create them
            pass
            
        # Run migrations silently
        call_command('migrate', verbosity=0, interactive=False)
        
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        
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
            
    except Exception as e:
        print(f"Setup error: {e}")

# Setup database on first load
setup_database()

application = get_wsgi_application()

# For Vercel
app = application