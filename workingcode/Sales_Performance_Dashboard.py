import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Read and prepare the data
print("Loading data...")
df = pd.read_excel('Online Retail Data Set.xlsx')
print(f"Initial data shape: {df.shape}")

# Data preprocessing
print("\nCleaning data...")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Sales'] = df['Quantity'] * df['UnitPrice']
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]  # Remove cancelled orders
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]  # Remove negative quantities and prices
print(f"Data shape after cleaning: {df.shape}")

# Set style for better visualizations
plt.style.use('bmh')
sns.set_palette('husl')

def create_monthly_sales_trend():
    """Create and save monthly sales trends visualization"""
    plt.figure(figsize=(12, 6))
    monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum().reset_index()
    monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].astype(str)
    
    plt.plot(monthly_sales['InvoiceDate'], monthly_sales['Sales'], 
             marker='o', linewidth=2, markersize=8)
    plt.title('Monthly Sales Trends', fontsize=14, pad=20)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Sales (£)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('monthly_sales_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    return monthly_sales

def create_top_products():
    """Create and save top products visualization"""
    plt.figure(figsize=(12, 6))
    top_products = df.groupby('Description')['Sales'].sum().sort_values(ascending=True).tail(10)
    
    plt.barh(y=range(len(top_products)), width=top_products.values,
            color=sns.color_palette('husl', 10))
    plt.yticks(range(len(top_products)), top_products.index, fontsize=10)
    plt.title('Top 10 Best-selling Products by Sales', fontsize=14, pad=20)
    plt.xlabel('Total Sales (£)', fontsize=12)
    plt.ylabel('Product Description', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('top_products.png', dpi=300, bbox_inches='tight')
    plt.close()
    return top_products

def create_country_sales():
    """Create and save sales by country visualization"""
    plt.figure(figsize=(12, 6))
    country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=True)
    
    plt.barh(y=range(len(country_sales)), width=country_sales.values,
            color=sns.color_palette('husl', len(country_sales)))
    plt.yticks(range(len(country_sales)), country_sales.index, fontsize=10)
    plt.title('Total Sales by Country', fontsize=14, pad=20)
    plt.xlabel('Total Sales (£)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('sales_by_country.png', dpi=300, bbox_inches='tight')
    plt.close()
    return country_sales

if __name__ == "__main__":
    print("\nCreating visualizations...")
    monthly_sales = create_monthly_sales_trend()
    print("1. Monthly sales trends visualization created")
    
    top_products = create_top_products()
    print("2. Top products visualization created")
    
    country_sales = create_country_sales()
    print("3. Sales by country visualization created")
    
    print("\nAll visualizations have been created and saved as PNG files.")
