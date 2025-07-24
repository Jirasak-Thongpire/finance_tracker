from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from .models import Transaction, Category
from .forms import TransactionForm
import json

def home(request):
    """Simple home view that redirects to dashboard or login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

@login_required
def dashboard(request):
    try:
        # Initialize data if needed
        if not Category.objects.exists():
            create_default_categories()
            
        transactions = Transaction.objects.filter(user=request.user)[:10]
        
        # Calculate totals
        total_income = Transaction.objects.filter(
            user=request.user, 
            transaction_type='income'
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        total_expense = Transaction.objects.filter(
            user=request.user, 
            transaction_type='expense'
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        balance = total_income - total_expense
        
        # Monthly data for charts
        current_month = timezone.now().month
        current_year = timezone.now().year
        
        monthly_income = Transaction.objects.filter(
            user=request.user,
            transaction_type='income',
            date__month=current_month,
            date__year=current_year
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        monthly_expense = Transaction.objects.filter(
            user=request.user,
            transaction_type='expense',
            date__month=current_month,
            date__year=current_year
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        # Category breakdown
        expense_by_category = Transaction.objects.filter(
            user=request.user,
            transaction_type='expense',
            date__month=current_month,
            date__year=current_year
        ).values('category__name', 'category__color').annotate(
            total=Sum('amount')
        ).order_by('-total')
        
        context = {
            'transactions': transactions,
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'monthly_income': monthly_income,
            'monthly_expense': monthly_expense,
            'expense_by_category': expense_by_category,
            'category_data': json.dumps(list(expense_by_category)),
        }
        
        return render(request, 'transactions/dashboard.html', context)
    except Exception as e:
        return render(request, 'transactions/error.html', {'error': str(e)})

@login_required
def transaction_list(request):
    try:
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'transactions/transaction_list.html', {'transactions': transactions})
    except Exception as e:
        return render(request, 'transactions/error.html', {'error': str(e)})

@login_required
def add_transaction(request):
    try:
        if not Category.objects.exists():
            create_default_categories()
            
        if request.method == 'POST':
            form = TransactionForm(request.POST)
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.user = request.user
                transaction.save()
                messages.success(request, 'Transaction added successfully!')
                return redirect('dashboard')
        else:
            form = TransactionForm()
        
        return render(request, 'transactions/add_transaction.html', {'form': form})
    except Exception as e:
        return render(request, 'transactions/error.html', {'error': str(e)})

@login_required
def edit_transaction(request, pk):
    try:
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        
        if request.method == 'POST':
            form = TransactionForm(request.POST, instance=transaction)
            if form.is_valid():
                form.save()
                messages.success(request, 'Transaction updated successfully!')
                return redirect('dashboard')
        else:
            form = TransactionForm(instance=transaction)
        
        return render(request, 'transactions/edit_transaction.html', {'form': form, 'transaction': transaction})
    except Exception as e:
        return render(request, 'transactions/error.html', {'error': str(e)})

@login_required
def delete_transaction(request, pk):
    try:
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        
        if request.method == 'POST':
            transaction.delete()
            messages.success(request, 'Transaction deleted successfully!')
            return redirect('dashboard')
        
        return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})
    except Exception as e:
        return render(request, 'transactions/error.html', {'error': str(e)})

def create_default_categories():
    """Create default categories if they don't exist"""
    from django.contrib.auth.models import User
    
    # Create admin user if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
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