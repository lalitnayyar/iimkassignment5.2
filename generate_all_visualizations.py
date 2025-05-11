import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from datetime import datetime
import time
from tqdm import tqdm
import psutil
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configure plotly for better performance
import plotly.io as pio
pio.templates.default = "plotly_white"
pio.renderers.default = 'browser'

# Create visualizations directory if it doesn't exist
os.makedirs('visualizations', exist_ok=True)

def save_plotly_fig(fig, filename):
    """Save plotly figure with optimized settings"""
    try:
        # Save only HTML version for better performance
        config = {
            'responsive': True,
            'displayModeBar': False,
            'staticPlot': False
        }
        
        fig.write_html(
            f'visualizations/{filename}.html',
            include_plotlyjs='cdn',
            config=config,
            full_html=False,
            auto_play=False
        )
        return True
    except Exception as e:
        print(f"Error saving figure {filename}: {str(e)}")
        return False

# Load and prepare data
def load_data():
    """Load and prepare the retail dataset with optimizations"""
    # Read only necessary columns
    usecols = ['InvoiceDate', 'Quantity', 'UnitPrice', 'Country', 'CustomerID', 'Description']
    df = pd.read_excel('Online Retail Data Set.xlsx', usecols=usecols)
    
    # Convert to appropriate types after loading
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
    
    # Clean data
    df = df.dropna(subset=['Quantity', 'UnitPrice'])
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    
    # Convert to memory-efficient types
    df['Country'] = df['Country'].astype('category')
    df['Description'] = df['Description'].astype('category')
    
    # Calculate total amount
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    
    # Process dates
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    
    return df

def create_monthly_sales_chart(df):
    """Create monthly sales trend visualization"""
    monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()
    
    fig = px.line(
        monthly_sales,
        x='Month',
        y='TotalAmount',
        title='Monthly Sales Performance'
    )
    
    fig.update_traces(mode='lines+markers')
    fig.update_layout(height=500)
    
    save_plotly_fig(fig, 'monthly_sales_performance')
    return fig

def create_country_sales_chart(df):
    """Create country-wise sales distribution visualization"""
    country_sales = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=True).tail(10)
    
    fig = go.Figure(go.Bar(
        x=country_sales.values,
        y=country_sales.index,
        orientation='h'
    ))
    
    fig.update_layout(
        title='Top 10 Countries by Sales',
        xaxis_title='Total Sales',
        yaxis_title='Country',
        template='plotly_white'
    )
    
    save_plotly_fig(fig, 'country_sales_distribution')
    return fig

def create_product_analysis(df):
    """Create product analysis visualization"""
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    
    fig = go.Figure(go.Bar(
        x=top_products.index,
        y=top_products.values,
        text=top_products.values,
        textposition='auto'
    ))
    
    fig.update_layout(
        title='Top 10 Products by Quantity Sold',
        xaxis_title='Product Description',
        yaxis_title='Total Quantity Sold',
        template='plotly_white',
        xaxis_tickangle=45
    )
    
    save_plotly_fig(fig, 'top_products_analysis')
    return fig

def create_customer_cohort(df):
    """Create customer cohort analysis visualization"""
    # Get first purchase month for each customer
    customer_first_purchase = df.groupby('CustomerID')['Month'].min()
    df['CohortMonth'] = df['CustomerID'].map(customer_first_purchase)
    
    # Calculate cohort metrics
    cohort_data = df.groupby(['CohortMonth', 'Month'])['CustomerID'].nunique().reset_index()
    cohort_data = cohort_data.pivot(index='CohortMonth', columns='Month', values='CustomerID')
    
    fig = go.Figure(data=go.Heatmap(
        z=cohort_data.values,
        x=cohort_data.columns,
        y=cohort_data.index,
        colorscale='RdYlBu'
    ))
    
    fig.update_layout(
        title='Customer Cohort Analysis',
        xaxis_title='Purchase Month',
        yaxis_title='Cohort Month',
        template='plotly_white'
    )
    
    save_plotly_fig(fig, 'customer_cohort_analysis')
    return fig

def create_sales_dashboard(df):
    """Create comprehensive sales dashboard"""
    # Create subplots
    fig = go.Figure()
    
    # Monthly trend
    monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()
    fig.add_trace(go.Scatter(
        x=monthly_sales['Month'],
        y=monthly_sales['TotalAmount'],
        name='Monthly Sales'
    ))
    
    # Add annotations for peak sales
    peak_month = monthly_sales.loc[monthly_sales['TotalAmount'].idxmax()]
    fig.add_annotation(
        x=peak_month['Month'],
        y=peak_month['TotalAmount'],
        text=f"Peak Sales: £{peak_month['TotalAmount']:,.0f}",
        showarrow=True,
        arrowhead=1
    )
    
    fig.update_layout(
        title='Executive Sales Dashboard',
        xaxis_title='Month',
        yaxis_title='Total Sales (£)',
        template='plotly_white',
        showlegend=True
    )
    
    save_plotly_fig(fig, 'executive_dashboard')
    return fig

def get_system_metrics():
    """Get current system metrics"""
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    return {
        'cpu_usage': cpu_percent,
        'memory_used': memory.percent,
        'memory_available': memory.available / (1024 * 1024 * 1024)  # Convert to GB
    }

def print_metrics(start_time, operation):
    """Print processing metrics"""
    metrics = get_system_metrics()
    elapsed_time = time.time() - start_time
    print(f"\n{operation} Metrics:")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")
    print(f"CPU Usage: {metrics['cpu_usage']}%")
    print(f"Memory Usage: {metrics['memory_used']}%")
    print(f"Available Memory: {metrics['memory_available']:.2f} GB")

def main():
    """Main function with optimized visualization generation"""
    total_start = time.time()
    
    print("\n1. Loading and Preparing Data...")
    start_time = time.time()
    df = load_data()
    print_metrics(start_time, "Data Loading")
    
    # List of visualizations to create
    visualizations = [
        ("Monthly Sales Chart", create_monthly_sales_chart),
        ("Country Sales Distribution", create_country_sales_chart),
        ("Product Analysis", create_product_analysis),
        ("Customer Cohort Analysis", create_customer_cohort),
        ("Executive Dashboard", create_sales_dashboard)
    ]
    
    print("\n2. Generating Visualizations...")
    for name, func in tqdm(visualizations, desc="Creating Plots"):
        try:
            start_time = time.time()
            func(df)
            print(f"\n✓ {name} completed in {time.time() - start_time:.2f} seconds")
        except Exception as e:
            print(f"\n✗ Error generating {name}: {str(e)}")
    
    # Final summary
    total_time = time.time() - total_start
    print(f"\nTotal Processing Time: {total_time:.2f} seconds")
    print(f"Visualizations Generated: {len(visualizations)}")
    print("\nAll visualizations have been saved in the 'visualizations' folder!")

if __name__ == "__main__":
    main()
