from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.shared import OxmlElement, qn
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
import os
import json

def create_toc_entry(paragraph):
    run = paragraph.add_run()
    fldChar = create_element('w:fldChar')
    create_attribute(fldChar, 'w:fldCharType', 'begin')
    run._r.append(fldChar)

    instrText = create_element('w:instrText')
    create_attribute(instrText, 'xml:space', 'preserve')
    instrText.text = 'TOC \\o "1-3" \\h \\z \\u'
    run._r.append(instrText)

    fldChar = create_element('w:fldChar')
    create_attribute(fldChar, 'w:fldCharType', 'end')
    run._r.append(fldChar)

def add_toc_heading(doc):
    heading = doc.add_heading('Table of Contents', level=1)
    heading.style.font.size = Pt(16)
    heading.style.font.bold = True
    heading.style.font.color.rgb = RGBColor(31, 73, 125)
    return heading

def setup_styles(doc):
    # Heading styles
    for i in range(1, 4):
        style = doc.styles[f'Heading {i}']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(16 - (i-1)*2)
        font.bold = True
        font.color.rgb = RGBColor(31, 73, 125)
        style.paragraph_format.space_before = Pt(24)
        style.paragraph_format.space_after = Pt(12)
        style.paragraph_format.keep_with_next = True

    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    style.paragraph_format.space_after = Pt(12)
    style.paragraph_format.line_spacing = 1.15

    # Code style
    style = doc.styles.add_style('Code', WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = 'Consolas'
    font.size = Pt(9)
    style.paragraph_format.space_before = Pt(6)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.left_indent = Inches(0.5)
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    style.paragraph_format.line_spacing = 1.0
    style.paragraph_format.widow_control = True

    # List Bullet style
    style = doc.styles['List Bullet']
    style.paragraph_format.left_indent = Inches(0.5)
    style.paragraph_format.first_line_indent = Inches(-0.25)
    style.paragraph_format.space_after = Pt(6)
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)

def create_element(name):
    return OxmlElement(name)

def create_attribute(element, name, value):
    element.set(qn(name), value)

def add_page_number(paragraph):
    run = paragraph.add_run()
    fldChar1 = create_element('w:fldChar')
    create_attribute(fldChar1, 'w:fldCharType', 'begin')
    instrText = create_element('w:instrText')
    create_attribute(instrText, 'xml:space', 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = create_element('w:fldChar')
    create_attribute(fldChar2, 'w:fldCharType', 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)

def add_heading_with_style(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    font = heading.style.font
    font.size = Pt(16) if level == 1 else Pt(14)
    font.color.rgb = RGBColor(31, 73, 125)
    return heading

def add_paragraph_with_style(doc, text, style='Normal'):
    p = doc.add_paragraph(style=style)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run(text)
    font = run.font
    font.size = Pt(11)
    return p

# Create a new document
doc = Document()

# Setup document styles
setup_styles(doc)

# Set up the page margins
section = doc.sections[0]
section.page_height = Inches(11)
section.page_width = Inches(8.5)
section.left_margin = Inches(1)
section.right_margin = Inches(1)
section.top_margin = Inches(1)
section.bottom_margin = Inches(1)
section.header_distance = Inches(0.5)
section.footer_distance = Inches(0.5)

# Title Page
title = doc.add_heading('Data Visualization and Analysis Report', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.runs[0].font.size = Pt(24)
title.runs[0].font.color.rgb = RGBColor(31, 73, 125)

# Add some space after title
doc.add_paragraph('')
doc.add_paragraph('')

# Assignment Information
info = [
    ('Course', "IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers"),
    ('Student Name', 'Lalit Nayyar'),
    ('Email ID', 'lalitnayyar@gmail.com'),
    ('Assignment', 'Required Assignment 5.2 : Applying Data Visualisation Principles'),
    ('Submission Date', 'May 11, 2025')
]

for label, value in info:
    p = doc.add_paragraph()
    p.add_run(f'{label}: ').bold = True
    p.add_run(value)

doc.add_page_break()

# Executive Summary
add_heading_with_style(doc, 'Executive Summary')
add_paragraph_with_style(doc, 
    'This report presents a comprehensive analysis of the Online Retail dataset using advanced '
    'data visualization techniques. The analysis focuses on key business metrics including sales '
    'trends, customer behavior, and product performance.'
)

# Dataset Overview
add_heading_with_style(doc, 'Dataset Overview')
add_heading_with_style(doc, 'Data Description', 2)
add_paragraph_with_style(doc, 
    'The Online Retail dataset contains transactional data from a UK-based online retail company. '
    'Key features include:'
)

features = [
    'InvoiceDate: Date and time of the transaction',
    'Quantity: Number of items purchased',
    'UnitPrice: Price per unit',
    'Country: Customer\'s country',
    'CustomerID: Unique identifier for each customer',
    'Description: Product description'
]

for feature in features:
    doc.add_paragraph(feature, style='List Bullet')

# Data Quality and Preprocessing
add_heading_with_style(doc, 'Data Quality and Preprocessing', 2)
preprocessing_steps = [
    'Removed null values in critical fields',
    'Filtered out negative quantities and prices',
    'Calculated total amount per transaction',
    'Categorized data by month and year',
    'Optimized data types for efficient processing'
]

for step in preprocessing_steps:
    doc.add_paragraph(step, style='List Bullet')

# Section 1: Key Visual Insights
add_heading_with_style(doc, 'Section 1: Key Visual Insights', 1)
add_paragraph_with_style(doc, 'This section presents two insightful charts from the analysis: Monthly Sales Trends and Country-wise Sales Distribution. Each chart is chosen for its clarity, conciseness, and ability to highlight key patterns in the data.')

# Monthly Sales Trends
add_heading_with_style(doc, 'Monthly Sales Trends', 2)
if os.path.exists(os.path.join('workingcode', 'monthly_sales_trends.png')):
    doc.add_picture(os.path.join('workingcode', 'monthly_sales_trends.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'This line chart shows the monthly sales performance over time. The chart is clear and easy to follow, revealing distinct seasonal patterns and peak sales during holiday periods. The design is clean and focuses attention on the overall trend, making it captivating and concise for business insights.')
else:
    add_paragraph_with_style(doc, '[Visualization not available: Monthly Sales Trends]', style='Normal')

# Country-wise Sales Distribution
add_heading_with_style(doc, 'Country-wise Sales Distribution', 2)
if os.path.exists(os.path.join('workingcode', 'sales_by_country.png')):
    doc.add_picture(os.path.join('workingcode', 'sales_by_country.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'This bar chart displays sales distribution across countries. The UK stands out as the dominant market, with other European countries also contributing significantly. The chart is concise, clean, and uses color to clearly distinguish between countries, helping to identify potential growth regions.')
else:
    add_paragraph_with_style(doc, '[Visualization not available: Country-wise Sales Distribution]', style='Normal')

doc.add_page_break()

# Section 2: Comprehensive Dashboard
add_heading_with_style(doc, 'Section 2: Comprehensive Dashboard', 1)
add_paragraph_with_style(doc, 'This section features a comprehensive dashboard with visualizations of monthly sales trends, best-selling products, and sales by country. The dashboard is designed for functionality and ease of navigation, providing actionable insights for decision-makers.')

# Monthly Sales (Dashboard)
add_heading_with_style(doc, 'Dashboard: Monthly Sales Trends', 2)
if os.path.exists(os.path.join('workingcode', 'monthly_sales_trends.png')):
    doc.add_picture(os.path.join('workingcode', 'monthly_sales_trends.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'The dashboard view of monthly sales trends allows for quick identification of peak periods and overall growth. The interactive design (in the original dashboard) enables users to filter and explore trends by time period.')
else:
    add_paragraph_with_style(doc, '[Visualization not available: Monthly Sales Trends]', style='Normal')

# Best-selling Products
add_heading_with_style(doc, 'Dashboard: Best-selling Products', 2)
if os.path.exists(os.path.join('workingcode', 'top_products.png')):
    doc.add_picture(os.path.join('workingcode', 'top_products.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'This chart highlights the top-performing products. It is clean and easy to interpret, showing that paper craft and seasonal items are among the best sellers. Such insights help in inventory and marketing planning.')
else:
    add_paragraph_with_style(doc, '[Visualization not available: Best-selling Products]', style='Normal')

# Sales by Country (Dashboard)
add_heading_with_style(doc, 'Dashboard: Sales by Country', 2)
if os.path.exists(os.path.join('workingcode', 'sales_by_country.png')):
    doc.add_picture(os.path.join('workingcode', 'sales_by_country.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'The dashboard provides a clear view of sales by country, reaffirming the UK’s dominance and identifying other key markets. The functional design makes it easy to compare sales across regions.')
else:
    add_paragraph_with_style(doc, '[Visualization not available: Sales by Country]', style='Normal')

# (Optional) Add any additional dashboard charts
if os.path.exists(os.path.join('workingcode', 'customer_analysis.png')):
    add_heading_with_style(doc, 'Dashboard: Customer Cohort Analysis', 2)
    doc.add_picture(os.path.join('workingcode', 'customer_analysis.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'This visualization explores customer retention and cohort behavior, helping to understand loyalty and repeat purchase patterns.')
if os.path.exists(os.path.join('workingcode', 'seasonal_analysis.png')):
    add_heading_with_style(doc, 'Dashboard: Seasonal Analysis', 2)
    doc.add_picture(os.path.join('workingcode', 'seasonal_analysis.png'), width=Inches(6))
    add_paragraph_with_style(doc, 'Seasonal analysis reveals the impact of holidays and promotions on sales, providing insights for campaign planning.')

doc.add_page_break()

# Add Interactive Visualizations Section
add_heading_with_style(doc, 'Interactive Visualizations', 1)
add_paragraph_with_style(doc, 'The following interactive visualizations are available in HTML format for dynamic exploration:')

html_files = {
    'Monthly Sales Performance': 'visualizations/monthly_sales_performance.html',
    'Country Sales Distribution': 'visualizations/country_sales_distribution.html',
    'Top Products Analysis': 'visualizations/top_products_analysis.html',
    'Customer Cohort Analysis': 'visualizations/customer_cohort_analysis.html',
    'Executive Dashboard': 'visualizations/executive_dashboard.html',
    'Executive Monthly Sales': 'visualizations/executive_monthly_sales.html',
    'Executive Summary': 'visualizations/executive_summary.html'
}

for title, path in html_files.items():
    if os.path.exists(path):
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(f'{title}: ')
        run.bold = True
        run.font.size = Pt(11)
        link_run = p.add_run(path)
        link_run.font.size = Pt(11)
        link_run.font.color.rgb = RGBColor(0, 0, 255)
        link_run.underline = True

doc.add_paragraph('')


# Notebook Implementation Sections
add_heading_with_style(doc, 'Jupyter Notebook Implementation', 1)

# Retail Sales Visualization Notebook
add_heading_with_style(doc, 'Retail Sales Visualization Implementation', 2)
add_paragraph_with_style(doc, 'The following sections detail the implementation of the retail sales visualizations using Python and Plotly.')

def add_code_section(doc, title, code):
    # Add section title
    heading = doc.add_heading(title, level=3)
    heading.style.font.color.rgb = RGBColor(31, 73, 125)
    
    # Add code block with proper formatting
    code_para = doc.add_paragraph(style='Code')
    code_run = code_para.add_run(code.strip())
    code_run.font.name = 'Consolas'
    code_run.font.size = Pt(9)
    
    # Add spacing after code block
    doc.add_paragraph('').paragraph_format.space_after = Pt(12)

code_sections = [
    ('Data Loading and Preprocessing', '''
# Load and preprocess the data
df = pd.read_excel('Online Retail Data Set.xlsx')

# Clean the data
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df = df.dropna(subset=['Quantity', 'UnitPrice'])
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
df['Month'] = df['InvoiceDate'].dt.strftime('%Y-%m')
'''),
    ('Monthly Sales Trend Analysis', '''
# Calculate monthly sales
monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()

# Create visualization
fig = px.line(monthly_sales, 
              x='Month', 
              y='TotalAmount',
              title='Monthly Sales Performance')
fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Total Sales Amount'
)
'''),
    ('Customer Cohort Analysis', '''
# Prepare cohort data
df['CohortMonth'] = df['InvoiceDate'].dt.to_period('M')
df['CohortGroup'] = df.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M')

# Calculate cohort metrics
cohort_data = df.groupby(['CohortGroup', 'CohortMonth']).agg({
    'CustomerID': 'nunique'
}).reset_index()
''')
]

# Add code sections with proper formatting
for title, code in code_sections:
    add_code_section(doc, title, code)

# Sales Dashboard Implementation
add_heading_with_style(doc, 'Sales Dashboard Implementation', 2)
add_paragraph_with_style(doc, 'The interactive sales dashboard was implemented using Plotly Dash, providing real-time insights into sales performance.')

dashboard_sections = [
    ('Dashboard Layout', '''
app.layout = html.Div([
    html.H1('Sales Performance Dashboard'),
    dcc.Graph(id='monthly-trend'),
    dcc.Graph(id='country-distribution'),
    dcc.Graph(id='product-analysis')
])
'''),
    ('Interactive Components', '''
@app.callback(
    Output('monthly-trend', 'figure'),
    Input('date-range', 'value')
)
def update_trend(date_range):
    filtered_df = filter_by_date(df, date_range)
    return create_trend_chart(filtered_df)
''')
]

# Add dashboard sections with proper formatting
for title, code in dashboard_sections:
    add_code_section(doc, title, code)

# Technical Implementation
add_heading_with_style(doc, 'Technical Implementation', 1)

# Tools and Libraries
add_heading_with_style(doc, 'Tools and Libraries Used', 2)
libraries = [
    'pandas>=1.3.0',
    'plotly==5.13.1',
    'numpy>=1.21.0',
    'openpyxl>=3.0.0',
    'tqdm>=4.65.0',
    'psutil>=5.9.0'
]

for lib in libraries:
    doc.add_paragraph(lib, style='List Bullet')

# Performance Optimizations
add_heading_with_style(doc, 'Performance Optimizations', 2)
optimizations = {
    'Data Loading': [
        'Efficient column selection',
        'Optimized data types',
        'Memory-efficient processing'
    ],
    'Visualization Generation': [
        'Streamlined chart creation',
        'Interactive HTML outputs',
        'Optimized rendering'
    ],
    'Processing Metrics': [
        'Data Loading Time: ~39 seconds',
        'Visualization Generation: <1 second',
        'Memory Usage: Optimized (64% utilization)'
    ]
}

for category, items in optimizations.items():
    p = doc.add_paragraph()
    p.add_run(f'{category}:').bold = True
    for item in items:
        doc.add_paragraph(item, style='List Bullet')

# Conclusions and Recommendations
add_heading_with_style(doc, 'Conclusions and Recommendations')

sections = {
    'Key Findings': [
        'Strong seasonal patterns in sales performance',
        'Dominant market presence in the UK',
        'Clear customer retention patterns',
        'Product popularity varies by season'
    ],
    'Business Recommendations': [
        'Optimize inventory for seasonal peaks',
        'Explore expansion opportunities in high-potential markets',
        'Implement targeted customer retention strategies',
        'Develop seasonal marketing campaigns'
    ],
    'Future Enhancements': [
        'Real-time dashboard updates',
        'Predictive analytics integration',
        'Advanced customer segmentation',
        'Automated reporting system'
    ]
}

for title, items in sections.items():
    add_heading_with_style(doc, title, 2)
    for item in items:
        doc.add_paragraph(item, style='List Bullet')

# Add page numbers
section = doc.sections[0]
footer = section.footer
paragraph = footer.paragraphs[0]
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_page_number(paragraph)

# Update section properties for margins and page size
section.page_height = Inches(11)
section.page_width = Inches(8.5)
section.left_margin = Inches(1)
section.right_margin = Inches(1)
section.top_margin = Inches(1)
section.bottom_margin = Inches(1)
section.header_distance = Inches(0.5)
section.footer_distance = Inches(0.5)

# Save the document
doc.save('Assignment_Submission_Report.docx')
print("Report generated successfully!")
print("Note: Please right-click on the Table of Contents and select 'Update Field' to update it.")
