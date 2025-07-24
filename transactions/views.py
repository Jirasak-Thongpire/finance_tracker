from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Simple demo view"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Personal Finance Tracker</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header bg-primary text-white">
                            <h2 class="text-center mb-0">Personal Finance Tracker</h2>
                        </div>
                        <div class="card-body">
                            <div class="text-center">
                                <h4>🎉 Successfully Deployed on Vercel!</h4>
                                <p class="mt-3">This is a Django-based Personal Finance Tracker with:</p>
                                <ul class="list-unstyled">
                                    <li>📊 Dashboard with Statistics</li>
                                    <li>💰 Income & Expense Tracking</li>
                                    <li>🏷️ Color-coded Categories</li>
                                    <li>📱 Responsive Design</li>
                                    <li>🔐 User Authentication</li>
                                </ul>
                                <hr>
                                <p><strong>Demo is working!</strong></p>
                                <p>The full application with database features would require additional setup for persistent data storage.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def dashboard(request):
    return home(request)

def transaction_list(request):
    return home(request)

def add_transaction(request):
    return home(request)

def edit_transaction(request, pk):
    return home(request)

def delete_transaction(request, pk):
    return home(request)