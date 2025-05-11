import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
    df['YearMonth'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    
    print(f"Data shape after cleaning: {df.shape}")
    return df

def create_monthly_sales_trend(df):
    """Create interactive monthly sales trend visualization"""
    monthly_sales = df.groupby('YearMonth')['Sales'].sum().reset_index()
    
    fig = go.Figure()
    
    # Add lines and markers
    fig.add_trace(go.Scatter(
        x=monthly_sales['YearMonth'],
        y=monthly_sales['Sales'],
        mode='lines+markers',
        name='Monthly Sales',
        hovertemplate='Month: %{x}<br>Sales: £%{y:,.2f}<extra></extra>'
    ))
    
    # Add trend line
    z = np.polyfit(range(len(monthly_sales)), monthly_sales['Sales'], 1)
    p = np.poly1d(z)
    fig.add_trace(go.Scatter(
        x=monthly_sales['YearMonth'],
        y=p(range(len(monthly_sales))),
        mode='lines',
        name='Trend',
        line=dict(dash='dash'),
        hovertemplate='Trend: £%{y:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Monthly Sales Trends with Trend Line',
        xaxis_title='Month',
        yaxis_title='Total Sales (£)',
        hovermode='x unified',
        showlegend=True
    )
    
    return fig

def create_top_products_chart(df):
    """Create interactive top products visualization"""
    top_products = df.groupby('Description')['Sales'].sum().sort_values(ascending=True).tail(10)
    
    fig = go.Figure(go.Bar(
        x=top_products.values,
        y=top_products.index,
        orientation='h',
        text=top_products.values.round(2),
        texttemplate='£%{text:,.0f}',
        textposition='outside',
        hovertemplate='Product: %{y}<br>Sales: £%{x:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Top 10 Best-selling Products by Sales',
        xaxis_title='Total Sales (£)',
        yaxis_title='Product Description',
        height=600
    )
    
    return fig

def create_country_sales_map(df):
    """Create interactive sales by country visualization"""
    country_sales = df.groupby('Country')['Sales'].sum().reset_index()
    
    fig = px.choropleth(
        country_sales,
        locations='Country',
        locationmode='country names',
        color='Sales',
        hover_name='Country',
        color_continuous_scale='Viridis',
        title='Sales Distribution by Country',
        labels={'Sales': 'Total Sales (£)'}
    )
    
    fig.update_layout(
        height=600,
        geo=dict(showframe=False, showcoastlines=True)
    )
    
    return fig

def create_seasonal_analysis(df):
    """Create interactive seasonal analysis visualization"""
    monthly_avg = df.groupby('Month')['Sales'].mean().reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_avg['MonthName'] = month_names
    
    fig = go.Figure(go.Bar(
        x=monthly_avg['MonthName'],
        y=monthly_avg['Sales'],
        text=monthly_avg['Sales'].round(2),
        texttemplate='£%{text:,.0f}',
        textposition='outside',
        hovertemplate='Month: %{x}<br>Average Sales: £%{y:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Average Sales by Month (Seasonal Analysis)',
        xaxis_title='Month',
        yaxis_title='Average Sales (£)',
        showlegend=False
    )
    
    return fig

def create_customer_analysis(df):
    """Create interactive customer analysis visualization"""
    customer_orders = df.groupby('CustomerID')['InvoiceNo'].nunique()
    
    fig = go.Figure(go.Histogram(
        x=customer_orders,
        nbinsx=30,
        name='Customers',
        hovertemplate='Orders: %{x}<br>Count: %{y}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Distribution of Orders per Customer',
        xaxis_title='Number of Orders',
        yaxis_title='Number of Customers',
        showlegend=False
    )
    
    return fig

def calculate_key_metrics(df):
    """Calculate key business metrics"""
    metrics = {
        'total_sales': df['Sales'].sum(),
        'total_orders': df['InvoiceNo'].nunique(),
        'total_customers': df['CustomerID'].nunique(),
        'total_products': df['Description'].nunique(),
        'avg_order_value': df.groupby('InvoiceNo')['Sales'].sum().mean(),
        'top_country': df.groupby('Country')['Sales'].sum().idxmax(),
        'top_product': df.groupby('Description')['Sales'].sum().idxmax()
    }
    return metrics
