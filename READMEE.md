# Personal Finance Tracker

A Django-based personal finance tracker that helps you manage your income and expenses with beautiful charts and statistics.

## Features

- 📊 **Dashboard with Statistics**: Visual overview of your finances with charts
- 💰 **Income & Expense Tracking**: Add, edit, and delete transactions
- 🏷️ **Categories**: Organize transactions with color-coded categories
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🔐 **User Authentication**: Secure login system
- ☁️ **Vercel Ready**: Configured for easy deployment

## Demo

- **Username**: admin
- **Password**: admin123

## Quick Start

### Local Development

1. **Clone and Setup**
   ```bash
   git clone <your-repo>
   cd personal-finance-tracker
   pip install -r requirements.txt
   ```

2. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python setup_data.py  # Creates default categories and admin user
   ```

3. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**
   - Open http://127.0.0.1:8000
   - Login with admin/admin123

### Vercel Deployment

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Connect your GitHub repository to Vercel
   - Vercel will automatically detect the configuration
   - Set environment variables in Vercel dashboard:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key
     ALLOWED_HOSTS=.vercel.app
     ```

3. **Database (Production)**
   - For production, set up PostgreSQL
   - Add these environment variables:
     ```
     VERCEL_ENV=production
     POSTGRES_DATABASE=your-db-name
     POSTGRES_USER=your-username
     POSTGRES_PASSWORD=your-password
     POSTGRES_HOST=your-host
     POSTGRES_PORT=5432
     ```

## Project Structure

```
personal-finance-tracker/
├── finance_tracker/          # Django project settings
├── transactions/             # Main app
│   ├── models.py            # Database models
│   ├── views.py             # Business logic
│   ├── forms.py             # Forms
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
├── templates/               # Base templates
├── static/                  # CSS, JS files
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration
└── build_files.sh          # Build script for Vercel
```

## Models

### Category
- Name, type (income/expense), color
- Used to categorize transactions

### Transaction  
- Title, amount, type, category, description, date
- Linked to user account
- Core data model for financial tracking

## Key Features Explained

### Dashboard
- Total income, expenses, and balance
- Monthly income vs expenses chart
- Expense breakdown by category (pie chart)
- Recent transactions list

### Transaction Management
- Add new income/expense transactions
- Edit existing transactions
- Delete transactions with confirmation
- Form validation and error handling

### Categories
- Pre-configured categories for common expenses
- Color-coded for visual organization
- Separate income and expense categories

### Charts & Statistics
- Chart.js integration for beautiful visualizations
- Monthly overview bar chart
- Category breakdown pie chart
- Responsive design

## Technologies Used

- **Backend**: Django 4.2, Python
- **Frontend**: Bootstrap 5, Chart.js
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Vercel
- **Styling**: Custom CSS with gradients

## Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.