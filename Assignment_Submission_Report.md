# Data Visualization Assignment Submission Report
## IIMK Professional Certificate in Data Science and AI for Managers

### Student Information
- Course: Data Visualization and Communication
- Assignment: Module 5.2 - Retail Sales Analysis
- Dataset: Online Retail Data Set

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
