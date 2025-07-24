from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'color', 'created_at']
    list_filter = ['category_type']
    search_fields = ['name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'transaction_type', 'category', 'user', 'date']
    list_filter = ['transaction_type', 'category', 'date']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'
    ordering = ['-date', '-created_at']
