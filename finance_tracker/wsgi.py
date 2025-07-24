"""
WSGI config for finance_tracker project.
"""

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_tracker.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# For Vercel
app = application