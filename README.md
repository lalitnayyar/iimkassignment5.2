# Data Visualization Assignment: Online Retail Analysis
- **Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
- **Student Name**: Lalit Nayyar
- **Email ID**: lalitnayyar@gmail.com
- **Assignment**: Required Assignment 5.2 : Applying Data Visualisation Principles
- **Submission Date**: May 11, 2025
## Project Overview
This project demonstrates the application of data visualization principles using an online retail dataset. The analysis is presented in two complementary notebooks, each focusing on different aspects of data visualization and analysis while following the 4C's principles (Clear, Clean, Concise, Captivating).

## Assignment Details
- **Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
- **Assignment**: Module 5.2 - Applying Data Visualization Principles
- **Dataset**: Online Retail Data Set.xlsx

## Learning Outcomes Addressed
- Understanding the importance of visualization in data presentation
- Application of 4C Principles (Clear, Clean, Concise, Captivating)
- Design of effective data dashboards
- Creation of appropriate color palettes for data visualization

## Project Structure
```
module5.2assignment/
├── Online Retail Data Set.xlsx      # Source dataset
├── Sales_Dashboard_Updated.ipynb   # Interactive dashboard notebook
├── Retail_Sales_Visualization.ipynb # Non-technical presentation notebook
├── requirements.txt                 # Python dependencies
└── README.md                       # This file
```

## Notebook Functionality

### 1. Sales Dashboard Updated (`Sales_Dashboard_Updated.ipynb`)
Comprehensive analysis dashboard with interactive visualizations:

1. **Data Processing & Cleaning**
   - Robust data cleaning pipeline
   - Missing value handling
   - Sales metrics calculation

2. **Interactive Visualizations**
   - Monthly Sales Trends (Interactive Line Chart)
   - Best-Selling Products Analysis (Bar Chart)
   - Geographic Sales Distribution (Bar Chart)
   - Product Categories Analysis (Pie Chart)
   - Customer Cohort Analysis (Heatmap)
   - RFM Analysis

3. **Advanced Features**
   - Custom color palettes
   - Interactive tooltips
   - Drill-down capabilities

### 2. Retail Sales Visualization (`Retail_Sales_Visualization.ipynb`)
Focused on non-technical stakeholder presentation:

1. **Simplified Visualizations**
   - Monthly Sales Trends
   - Country-wise Sales Distribution
   - Top Products Analysis
   - Daily Sales Patterns

2. **Business Insights**
   - Executive summaries
   - Key performance indicators
   - Market trends

3. **Presentation Features**
   - Clear annotations
   - Business-friendly terminology
   - Actionable insights

## User Guide

### Setup Instructions
1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

3. **Choose the Appropriate Notebook**
   - For detailed analysis: Open `Sales_Dashboard_Updated.ipynb`
   - For executive presentation: Open `Retail_Sales_Visualization.ipynb`

### Using the Notebooks

#### Sales Dashboard (Technical Users)
1. **Data Processing**
   - Execute cells sequentially (Shift + Enter)
   - Monitor data cleaning outputs
   - Check for any warnings or errors

2. **Interactive Features**
   - Hover over charts for detailed tooltips
   - Use zoom and pan controls
   - Click legends to filter data
   - Export visualizations as needed

3. **Customization**
   - Modify color schemes in the configuration cell
   - Adjust chart parameters for different views
   - Add new analysis sections as needed

#### Retail Visualization (Business Users)
1. **Navigation**
   - Use the table of contents for quick access
   - Follow the narrative flow of insights
   - Review executive summaries

2. **Presentation Mode**
   - Use Jupyter's presentation mode for meetings
   - Focus on key insights and trends
   - Leverage interactive features for Q&A

3. **Exporting Results**
   - Download as PDF for sharing
   - Export specific visualizations
   - Create custom reports

## Analysis Summary

### Key Insights

1. **Sales Performance**
   - Temporal trends and seasonality
   - Peak sales periods identification
   - Growth pattern analysis

2. **Geographic Distribution**
   - Top performing countries
   - Market penetration insights
   - Regional opportunities

3. **Product Analysis**
   - Best-selling items
   - Category performance
   - Product mix optimization

4. **Customer Behavior**
   - Cohort analysis results
   - Customer retention patterns
   - Purchase frequency insights

### Visualization Principles Applied

1. **Clear**
   - Consistent labeling
   - Intuitive chart types
   - Proper scaling and axes

2. **Clean**
   - Minimal chart junk
   - Appropriate white space
   - Professional color schemes

3. **Concise**
   - Focused messaging
   - Essential information only
   - Efficient use of space

4. **Captivating**
   - Interactive elements
   - Engaging color palette
   - Professional layout

## Technical Requirements

- Python 3.9+
- Required packages:
  - pandas >= 1.3.0
  - plotly == 5.13.1
  - kaleido == 0.2.1
  - numpy >= 1.21.0
  - jupyter >= 1.0.0
  - tqdm >= 4.65.0
  - psutil >= 5.9.0

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate all visualizations:
   ```bash
   python generate_all_visualizations.py
   ```

   This will create both interactive (.html) and static (.svg) versions of all visualizations in the `visualizations` folder, with progress tracking and performance metrics.

3. **Generate the Assignment Submission Report:**
   ```bash
   python generate_report.py
   ```
   This will produce `Assignment_Submission_Report.docx` in the project directory.

   - The report contains all key visualizations and outputs from both notebooks (`Retail_Sales_Visualization.ipynb` and `Sales_Dashboard_Updated.ipynb`).
   - The report is structured into two main sections:
     1. **Key Visual Insights**: Presents two insightful charts (monthly sales trends and country-wise sales distribution) with clear, concise, captivating explanations.
     2. **Comprehensive Dashboard**: Includes dashboard visualizations (monthly sales, best-selling products, sales by country, and more), each with a brief explanation.
   - **Note:** The report does not include a Table of Contents.

## Presentation Guidelines

1. **Technical Presentations**
   - Use `Sales_Dashboard_Updated.ipynb`
   - Focus on methodology and detailed analysis
   - Highlight technical insights

2. **Executive Presentations**
   - Use `Retail_Sales_Visualization.ipynb`
   - Emphasize business impacts
   - Focus on actionable insights

3. **Documentation**
   - Both notebooks are self-documenting
   - Code is thoroughly commented
   - Visualization choices are explained
   - 4C principles application is documented
   - Analysis is clear and professional

## Technical Requirements
- Python 3.8 or higher
- Jupyter Notebook
- Required Python packages (specified in requirements.txt):
  - pandas
  - matplotlib
  - seaborn
  - openpyxl
  - jupyter
  - notebook

## Support
For any technical issues or questions:
1. Review the notebook's markdown cells for detailed explanations
2. Check the Python package documentation for specific function usage
3. Consult course materials for visualization best practices

## Author Information
- Student Name: Lalit Nayyar
- Email ID: lalitnayyar@gmail.com
- Course: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
- Assignment: Required Assignment 5.2 : Applying Data Visualisation Principles
- Submission Date: May 11, 2025
