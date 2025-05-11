# %% [markdown]
# # Sales Performance Dashboard
#
# ## Assignment Information
# - **Course**: IIMK's Professional Certificate in Data Science and Artificial Intelligence for Managers
# - **Student Name**: Lalit Nayyar
# - **Email ID**: lalitnayyar@gmail.com
# - **Assignment**: Required Assignment 5.2 : Applying Data Visualisation Principles
# - **Submission Date**: May 11, 2025

# %% [markdown]
# ## Introduction
# This notebook demonstrates the application of data visualization principles to analyze an online retail dataset. 
# The visualizations follow the 4C's principles:
# - **Clear**: Easy to understand and interpret
# - **Clean**: Minimal clutter and distractions
# - **Concise**: Focused on key information
# - **Captivating**: Visually engaging and memorable

# %%
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set style for better visualizations
plt.style.use('bmh')
sns.set_palette('husl')

# %% [markdown]
# ## Data Loading and Preprocessing

# %%
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

# %% [markdown]
# ## 1. Monthly Sales Trends

# %%
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
plt.show()

# %% [markdown]
# ## 2. Best-selling Products

# %%
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
plt.show()

# %% [markdown]
# ## 3. Sales by Country

# %%
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
plt.show()

# %% [markdown]
# ## Conclusion
#
# The visualizations above provide key insights into the online retail business:
#
# 1. **Monthly Sales Trends**: Shows the overall business growth and seasonal patterns
# 2. **Best-selling Products**: Identifies the most profitable products
# 3. **Sales by Country**: Reveals the geographical distribution of sales
#
# These visualizations follow the 4C's principles:
# - **Clear**: Each visualization has proper titles, labels, and scales
# - **Clean**: Minimal gridlines and no unnecessary decorations
# - **Concise**: Focus on the most important metrics
# - **Captivating**: Use of appropriate colors and visual elements
