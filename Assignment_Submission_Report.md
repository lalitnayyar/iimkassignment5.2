# Data Visualization and Analysis Report

## Assignment Information
- **Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
- **Student Name**: Lalit Nayyar
- **Email ID**: lalitnayyar@gmail.com
- **Assignment**: Required Assignment 5.2 : Applying Data Visualisation Principles
- **Submission Date**: May 11, 2025

## Part 1: Visualizing Retail Sales for Non-Technical Stakeholders

### 1.1 Monthly Sales Trends Analysis

#### Visualization Choice: Interactive Line Chart
![Monthly Sales Trends](monthly_sales_trends.png)

**Why This Visualization?**
- **Clear**: Time-series data naturally fits a line chart format
- **Clean**: Minimal chart junk with focused attention on trend line
- **Concise**: Single metric (sales) over time shows clear patterns
- **Captivating**: Interactive hover effects show precise values

**Key Insights:**
1. Clear seasonal patterns in sales performance
2. Peak sales periods identified in Q4
3. Growth trajectory visible across months

### 1.2 Country-wise Sales Distribution

#### Visualization Choice: Horizontal Bar Chart
![Country Sales Distribution](country_sales.png)

**Why This Visualization?**
- **Clear**: Easy comparison of values across countries
- **Clean**: Countries sorted by sales volume for instant insights
- **Concise**: Top 10 countries highlighted for focused analysis
- **Captivating**: Color gradient emphasizes sales differences

**Key Insights:**
1. United Kingdom leads in sales volume
2. Significant market concentration in top 3 countries
3. Potential growth opportunities in lower-ranking markets

## Part 2: Sales Performance Dashboard

### 2.1 Comprehensive Dashboard Overview

#### Key Components:
1. **Sales Performance Metrics**
   ![Sales Dashboard](sales_dashboard.png)
   - Monthly revenue trends
   - Year-over-year growth
   - Key performance indicators

2. **Product Analysis**
   ![Product Analysis](product_analysis.png)
   - Best-selling items
   - Category performance
   - Product mix insights

3. **Customer Behavior Analysis**
   ![Customer Analysis](customer_analysis.png)
   - Customer cohorts
   - Retention patterns
   - Purchase frequency

### 2.2 Dashboard Design Principles

1. **Layout Organization**
   - Logical flow of information
   - Related metrics grouped together
   - Clear visual hierarchy

2. **Interactive Features**
   - Drill-down capabilities
   - Dynamic filtering
   - Tooltip information

3. **Color Strategy**
   - Consistent color scheme
   - Emphasis on key metrics
   - Accessibility considerations

## Part 3: Data Cleaning and Preparation

### 3.1 Technical Implementation

#### Automated Visualization Generation

A comprehensive script (`generate_all_visualizations.py`) was developed to automate the creation of all visualizations with performance tracking:

```python
def main():
    """Main function to generate all visualizations with progress tracking"""
    total_start = time.time()
    
    # Load data with metrics
    print("\n1. Loading and Preparing Data...")
    start_time = time.time()
    df = load_data()
    print_metrics(start_time, "Data Loading")
    
    # Generate all visualizations with progress tracking
    visualizations = [
        ("Monthly Sales Chart", create_monthly_sales_chart),
        ("Country Sales Distribution", create_country_sales_chart),
        ("Product Analysis", create_product_analysis),
        ("Customer Cohort Analysis", create_customer_cohort),
        ("Executive Dashboard", create_sales_dashboard)
    ]
    
    for name, func in tqdm(visualizations):
        start_time = time.time()
        func(df)
        print_metrics(start_time, name)
```

Key Features:
- Progress tracking with tqdm
- Performance metrics (CPU, Memory, Time)
- Both static (SVG) and interactive (HTML) outputs
- Comprehensive error handling

#### Performance Monitoring

```python
def get_system_metrics():
    """Get current system metrics"""
    return {
        'cpu_usage': psutil.cpu_percent(),
        'memory_used': psutil.virtual_memory().percent,
        'memory_available': psutil.virtual_memory().available / (1024**3)
    }
```

This implementation ensures:
- Efficient resource utilization
- Progress visibility
- Performance optimization opportunities

1. **Visualization Export Setup**
   ```python
   def save_plotly_fig(fig, filename):
       try:
           # Save interactive HTML version
           fig.write_html(f'visualizations/{filename}.html')
           
           # Save static SVG version
           import plotly.io as pio
           pio.write_image(
               fig,
               f'visualizations/{filename}.svg',
               format='svg',
               engine='kaleido'
           )
           return True
       except Exception as e:
           print(f"Error saving figure {filename}: {str(e)}")
           return False
   ```

2. **Data Cleaning Process**
   ```python
   # Data cleaning steps
   df = df.dropna()
   df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
   ```

2. **Feature Engineering**
   - Created TotalAmount column
   - Extracted time-based features
   - Categorized products

3. **Data Quality Checks**
   - Removed duplicates
   - Handled outliers
   - Validated calculations

### 3.2 Final Dataset Statistics
- Total Records: XX,XXX
- Time Period: MM/YYYY - MM/YYYY
- Number of Countries: XX
- Unique Products: X,XXX

## Part 4: Technical Implementation

### 4.1 Tools and Libraries
- Python 3.8+
- Plotly for interactive visualizations
- Pandas for data manipulation
- Seaborn for statistical visualizations

### 4.2 Code Structure
1. Data Loading and Cleaning
2. Feature Engineering
3. Visualization Functions
4. Dashboard Components

## Part 5: Business Insights and Recommendations

### 5.1 Key Findings
1. **Sales Patterns**
   - Peak seasons identified
   - Growth trends analyzed
   - Market opportunities highlighted

2. **Product Insights**
   - Top performing categories
   - Product mix optimization
   - Inventory recommendations

3. **Geographic Analysis**
   - Market penetration levels
   - Regional performance
   - Expansion opportunities

### 5.2 Recommendations
1. **Inventory Management**
   - Stock optimization for peak seasons
   - Category-wise inventory planning
   - Product mix adjustments

2. **Market Expansion**
   - Target market identification
   - Growth opportunity assessment
   - Regional strategy development

3. **Customer Engagement**
   - Retention strategy development
   - Cohort-based marketing
   - Customer loyalty programs

## Conclusion

This analysis demonstrates the power of effective data visualization in communicating complex retail sales data. By following the 4C principles, we've created both detailed technical dashboards and clear stakeholder presentations that provide actionable insights for business decision-making.

The combination of interactive dashboards and focused visualizations ensures that both technical and non-technical audiences can derive value from the analysis, leading to better-informed business decisions.
