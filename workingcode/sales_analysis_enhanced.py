import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

def load_and_clean_data():
    """Load and clean the retail dataset"""
    print("Loading data...")
    df = pd.read_excel('Online Retail Data Set.xlsx')
    print(f"Initial data shape: {df.shape}")
    
    print("\nCleaning data...")
    # Convert date and create sales column
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Sales'] = df['Quantity'] * df['UnitPrice']
    
    # Remove cancelled orders and invalid entries
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    # Add month and year columns for analysis
    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    
    print(f"Data shape after cleaning: {df.shape}")
    return df

def create_monthly_trends(df):
    """Create monthly sales trends visualization"""
    plt.figure(figsize=(15, 7))
    monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum().reset_index()
    monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].astype(str)
    
    # Plot with trend line
    plt.plot(monthly_sales['InvoiceDate'], monthly_sales['Sales'], 
             marker='o', linewidth=2, markersize=8, label='Monthly Sales')
    
    # Add trend line
    z = np.polyfit(range(len(monthly_sales)), monthly_sales['Sales'], 1)
    p = np.poly1d(z)
    plt.plot(range(len(monthly_sales)), p(range(len(monthly_sales))), 
             "r--", alpha=0.8, label='Trend Line')
    
    plt.title('Monthly Sales Trends with Trend Line', fontsize=14, pad=20)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Sales (£)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('monthly_sales_trends.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_top_products(df):
    """Create best-selling products visualization"""
    plt.figure(figsize=(15, 8))
    top_products = df.groupby('Description')['Sales'].sum().sort_values(ascending=True).tail(10)
    
    # Create horizontal bar chart
    bars = plt.barh(y=range(len(top_products)), width=top_products.values,
                   color=sns.color_palette('husl', 10))
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, 
                f'£{width:,.0f}', 
                ha='left', va='center', fontsize=10)
    
    plt.yticks(range(len(top_products)), top_products.index, fontsize=10)
    plt.title('Top 10 Best-selling Products by Sales', fontsize=14, pad=20)
    plt.xlabel('Total Sales (£)', fontsize=12)
    plt.ylabel('Product Description', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('top_products.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_country_analysis(df):
    """Create sales by country visualization"""
    plt.figure(figsize=(15, 8))
    country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=True)
    
    # Create horizontal bar chart
    bars = plt.barh(y=range(len(country_sales)), width=country_sales.values,
                   color=sns.color_palette('husl', len(country_sales)))
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, 
                f'£{width:,.0f}', 
                ha='left', va='center', fontsize=10)
    
    plt.yticks(range(len(country_sales)), country_sales.index, fontsize=10)
    plt.title('Total Sales by Country', fontsize=14, pad=20)
    plt.xlabel('Total Sales (£)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('sales_by_country.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_seasonal_analysis(df):
    """Create seasonal sales analysis visualization"""
    plt.figure(figsize=(12, 6))
    monthly_avg = df.groupby('Month')['Sales'].mean()
    
    # Create bar chart with average monthly sales
    bars = plt.bar(range(1, 13), monthly_avg.values, 
                  color=sns.color_palette('husl', 12))
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                f'£{height:,.0f}',
                ha='center', va='bottom', fontsize=10)
    
    plt.title('Average Sales by Month (Seasonal Analysis)', fontsize=14, pad=20)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Sales (£)', fontsize=12)
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('seasonal_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_customer_analysis(df):
    """Create customer analysis visualization"""
    plt.figure(figsize=(12, 6))
    
    # Calculate orders per customer
    customer_orders = df.groupby('CustomerID')['InvoiceNo'].nunique()
    
    # Create histogram of orders per customer
    plt.hist(customer_orders, bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Orders per Customer', fontsize=14, pad=20)
    plt.xlabel('Number of Orders', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('customer_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Set style for better visualizations
    plt.style.use('bmh')
    sns.set_palette('husl')
    
    # Load and clean data
    df = load_and_clean_data()
    
    # Create all visualizations
    print("\nCreating visualizations...")
    create_monthly_trends(df)
    create_top_products(df)
    create_country_analysis(df)
    create_seasonal_analysis(df)
    create_customer_analysis(df)
    
    print("All visualizations have been created and saved as PNG files.")
    
    # Return some key statistics
    stats = {
        'total_sales': df['Sales'].sum(),
        'total_orders': df['InvoiceNo'].nunique(),
        'total_customers': df['CustomerID'].nunique(),
        'total_products': df['Description'].nunique(),
        'avg_order_value': df.groupby('InvoiceNo')['Sales'].sum().mean()
    }
    return stats

if __name__ == "__main__":
    stats = main()
    print("\nKey Statistics:")
    print(f"Total Sales: £{stats['total_sales']:,.2f}")
    print(f"Total Orders: {stats['total_orders']:,}")
    print(f"Total Customers: {stats['total_customers']:,}")
    print(f"Total Products: {stats['total_products']:,}")
    print(f"Average Order Value: £{stats['avg_order_value']:.2f}")
