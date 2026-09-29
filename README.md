<img width="887" height="497" alt="image" src="https://github.com/user-attachments/assets/1e51c1e1-0556-4d83-8738-d0ca9858c911" /># 🚀 NEXUS — Retail Business Intelligence & Analytics Platform

> An end-to-end Retail Business Intelligence and Analytics project that transforms retail transaction data into meaningful business insights using Python, Pandas, Power BI, Data Modeling, and DAX.

📌 Project Overview

NEXUS is an end-to-end Retail Business Intelligence and Analytics project designed to simulate a real-world retail data environment and convert raw transactional data into business-ready insights.

The project covers the complete data journey:

Data Generation → Data Validation → CSV Data Layer → Power Query ETL → Data Modeling → DAX → Power BI Dashboard → Business Insights

NEXUS generates interconnected datasets for customers, products, stores, employees, orders, order items, inventory, returns, and dates. The validated data is prepared in Power BI and transformed into an interactive executive dashboard.

📑 Table of Contents

Project Objectives

Business Problem

Tech Stack

Project Architecture

Complete Data Journey

Dataset

Data Model

Data Validation

ETL Process

Project Structure

Key Project Metrics

Core DAX Measures

Power BI Dashboard

Dashboard Preview

Business Questions

Skills Demonstrated

How to Run

Future Enhancements

Interview Explanation

Project Outcome

Author

🎯 Project Objectives

#

Objective

1

Generate a realistic retail business dataset

2

Create interconnected customer, product, store and transaction data

3

Validate generated data using Python and Pandas

4

Prepare data using Power Query

5

Build a structured Power BI data model

6

Create business KPIs using DAX

7

Analyze sales, profitability, customers, products and returns

8

Build an interactive executive dashboard

9

Convert raw data into business-oriented insights

10

Demonstrate an end-to-end industry-style analytics workflow

💼 Business Problem

Retail businesses generate large amounts of data across customers, products, stores, orders, inventory and returns. Raw transaction data is difficult to interpret directly.

NEXUS is designed to answer questions such as:

What is total sales revenue?

How many orders are being processed?

Which regions generate the most sales?

Which product categories contribute most to revenue?

How profitable is the business?

How many returns are recorded?

How much money is refunded?

How is performance changing over time?

How does current-year sales compare with previous-year sales?

🏗️ Project Architecture

Business Problem
      ↓
Python Data Generation
      ↓
Pandas / Data Validation
      ↓
CSV Data Layer
      ↓
Power Query ETL
      ↓
Power BI Data Model
      ↓
DAX Measures & KPIs
      ↓
Power BI Dashboard
      ↓
Business Insights

Architecture in One Line

Python → Pandas → Data Validation → CSV → Power Query → Data Model → DAX → Power BI → Business Insights

🔄 Complete Data Journey

1. Define Retail Business Requirements
              ↓
2. Generate Synthetic Retail Data
              ↓
3. Validate Data Quality
              ↓
4. Store Validated Data as CSV
              ↓
5. Import CSV Files into Power BI
              ↓
6. Transform Data using Power Query
              ↓
7. Set Correct Data Types
              ↓
8. Create Table Relationships
              ↓
9. Build Analytical Data Model
              ↓
10. Create DAX Measures
              ↓
11. Build KPIs and Visualizations
              ↓
12. Add Interactive Slicers
              ↓
13. Build Executive Dashboard
              ↓
14. Extract Business Insights

🛠️ Tech Stack

Technology

Purpose

Python

Synthetic retail data generation

Pandas

Data manipulation and validation

NumPy

Numerical operations

CSV

Data storage layer

Power Query

ETL and data transformation

Power BI

Data modeling and dashboard development

DAX

KPIs, profitability and time intelligence

Git

Version control

GitHub

Project hosting and portfolio

📊 Dataset

NEXUS contains 9 interconnected datasets.

Dataset

Records

Purpose

customers.csv

10,000

Customer master data

products.csv

1,000

Product catalog

stores.csv

20

Store and regional information

employees.csv

100

Employee information

orders.csv

50,000

Order-level transactions

order_items.csv

150,251

Product-level order transactions

inventory.csv

20,000

Store-product inventory

returns.csv

8,894

Return and refund transactions

date_dimension.csv

1,096

Date and time intelligence

🗂️ Dataset Details

👥 Customers

Customer master data including customer ID, name, gender, email, phone, date of birth, city, state, country and registration date.

📦 Products

Product catalog containing product ID, product name, category, unit cost, selling price and launch date.

🏪 Stores

Store information including store ID, store name, city, state and region.

👨‍💼 Employees

Employee information including employee ID, employee name, store ID and role.

🛒 Orders

Order-level information including order ID, customer, store, employee, order date, channel, payment method, order status, shipping location, total amount, discount and shipping cost.

🧾 Order Items

Product-level transaction information including order item ID, order ID, product ID, quantity, unit price, discount and total price.

📦 Inventory

Store-product inventory information including stock quantity and reorder information.

↩️ Returns

Return information including return ID, order ID, order item ID, customer ID, product ID, return date, return reason and refund amount.

📅 Date Dimension

Date attributes used for time-based analysis and DAX time intelligence.

🔍 Data Validation

Before Power BI analysis, the generated datasets were validated using Python and Pandas.

Validation Checks

Record count validation

Unique ID validation

Order consistency

Customer consistency

Product consistency

Order-item relationships

Missing value checks

Transaction consistency

Revenue validation

Refund validation

Validation Results

Unique Order IDs      : 50,000
Unique Customer IDs   : 10,000
Unique Product IDs    : 1,000
Order Items Orders    : 50,000
Order Items Products  : 1,000
Total Revenue         : ₹8,911,493,900.79
Total Refund          : ₹448,451,497.51

🔄 ETL Process

Power Query is used as the ETL layer between CSV data and the Power BI model.

ETL Steps

Import CSV files

Review columns

Set correct data types

Convert date columns to Date

Convert IDs to Whole Number

Convert monetary fields to Decimal Number

Clean and validate text fields

Prepare tables for relationships

Apply transformations

Load the prepared model into Power BI

🧮 Data Model

Dimension Tables

Customers
Products
Stores
Employees
Date_Dimension

Transaction Tables

Orders
Order_Items
Inventory
Returns

Simplified Model

                     Date_Dimension
                           │
                           ▼
Customers ───────────► Orders ◄────────── Stores
                           │
                           ▼
                      Order_Items
                           │
                           ▼
                        Products

Stores ───────────────► Inventory ◄────── Products

Employees ────────────► Orders

Returns ──────────────► Customers
Returns ──────────────► Products
Returns ──────────────► Orders
Returns ──────────────► Order_Items

Main Relationships

From (1)

To (*)

Cardinality

Customers[customer_id]

Orders[customer_id]

1 : *

Products[product_id]

Order_Items[product_id]

1 : *

Orders[order_id]

Order_Items[order_id]

1 : *

Stores[store_id]

Orders[store_id]

1 : *

Stores[store_id]

Inventory[store_id]

1 : *

Products[product_id]

Inventory[product_id]

1 : *

Employees[employee_id]

Orders[employee_id]

1 : *

Date_Dimension[full_date]

Orders[order_date]

1 : *

📐 Core DAX Measures

Sales & Orders

Total Sales =
SUM(Orders[total_amount])

Total Orders =
DISTINCTCOUNT(Orders[order_id])

Total Customers =
DISTINCTCOUNT(Customers[customer_id])

Total Products =
DISTINCTCOUNT(Products[product_id])

Total Quantity Sold =
SUM(Order_Items[quantity])

Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders],
    0
)

Total Shipping Cost =
SUM(Orders[shipping_cost])

Profitability

Total Cost =
SUMX(
    Order_Items,
    Order_Items[quantity] *
    RELATED(Products[unit_cost])
)

Gross Profit =
[Total Sales] - [Total Cost]

Profit Margin % =
DIVIDE(
    [Gross Profit],
    [Total Sales],
    0
)

Net Sales =
[Total Sales] - [Total Refund]

Net Profit =
[Net Sales] - [Total Cost] - [Total Shipping Cost]

Net Profit Margin % =
DIVIDE(
    [Net Profit],
    [Net Sales],
    0
)

Returns

Total Returns =
DISTINCTCOUNT(Returns[return_id])

Total Refund =
SUM(Returns[refund_amount])

Return Rate =
DIVIDE(
    [Total Returns],
    [Total Orders],
    0
)

Time Intelligence

Previous Year Sales =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(Date_Dimension[full_date])
)

YoY Sales Growth % =
DIVIDE(
    [Total Sales] - [Previous Year Sales],
    [Previous Year Sales],
    0
)

Previous Year Profit =
CALCULATE(
    [Gross Profit],
    SAMEPERIODLASTYEAR(Date_Dimension[full_date])
)

YoY Profit Growth % =
DIVIDE(
    [Gross Profit] - [Previous Year Profit],
    [Previous Year Profit],
    0
)

Sales YTD =
TOTALYTD(
    [Total Sales],
    Date_Dimension[full_date]
)

📊 Power BI Dashboard

The NEXUS Executive Dashboard provides an interactive view of retail business performance.

KPI Cards

Total Sales

Total Orders

Gross Profit

Total Customers

Average Order Value

Visualizations

Monthly Sales Trend — Line chart

Sales by Region — Clustered column chart

Sales by Category — Donut chart

Gross Profit Trend — Line chart

Returns by Reason — Clustered column chart

Refund Amount by Reason — Clustered column chart

YoY Sales Performance — Clustered column chart

YoY Sales Growth % — Line chart

Interactive Slicers

Year

Region

Category

Channel

Order Status

🖼️ Dashboard Preview



The dashboard preview is the Power BI Executive Dashboard created for NEXUS.

📁 Project Structure

NEXUS/
│
├── Data_generator/
│   └── data/
│       ├── generate_customers.py
│       ├── generate_date_dimension.py
│       ├── generate_employees.py
│       ├── generate_inventory.py
│       ├── generate_order_items.py
│       ├── generate_orders.py
│       ├── generate_products.py
│       ├── generate_returns.py
│       ├── generate_stores.py
│       └── validate_data.py
│
├── data/
│   ├── customers.csv
│   ├── date_dimension.csv
│   ├── employees.csv
│   ├── inventory.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── returns.csv
│   └── stores.csv
│
├── dashboard/
│   └── dashboard_preview.png
│
├── config.py
├── main.py
├── init.py
├── .gitignore
└── README.md

📊 Key Project Metrics

Metric

Value

Customers

10,000

Products

1,000

Stores

20

Employees

100

Orders

50,000

Order Items

150,251

Inventory Records

20,000

Returns

8,894

Date Records

1,096

Total Revenue

₹8.91B

Total Refund

₹448.45M

❓ Business Questions Answered

Sales

What is total sales revenue?

How are sales changing over time?

Which regions contribute to sales?

Which categories contribute to revenue?

Orders

How many orders are processed?

What is the average order value?

How does order performance change over time?

Products

Which categories contribute most to sales?

How do product costs affect profitability?

Which products can be investigated further for performance?

Customers

How many customers are represented?

How does customer activity vary geographically?

Which customer dimensions can support segmentation?

Profitability

What is gross profit?

What is net profit?

What is the profit margin?

How does profitability change over time?

Returns

How many returns are recorded?

What are the major return reasons?

How much money is refunded?

What is the return rate?

Time Performance

What is current-year sales performance?

How does current performance compare with the previous year?

What is YoY sales growth?

What is Sales YTD?

🎓 Skills Demonstrated

Data & Analytics

BI & Modeling

Development & Delivery

Data generation

Power Query

Python programming

Data cleaning

Data modeling

Pandas

Data validation

Relationships

NumPy

KPI development

DAX

Git

Sales analysis

Time intelligence

GitHub

Profitability analysis

Power BI

Documentation

Return analysis

Dashboard development

Business storytelling

⚙️ How to Run the Project

1. Clone the Repository

git clone https://github.com/Avii-tech898/Nexus.git

2. Navigate to the Project

cd Nexus

3. Create a Virtual Environment

python -m venv .venv

Windows

.venv\Scripts\activate

4. Install Dependencies

pip install pandas numpy

5. Generate the Dataset

Run the main pipeline from the NEXUS root:

python main.py

6. Validate the Data

python Data_generator/data/validate_data.py

7. Build / Refresh Power BI

Import the generated CSV files into Power BI, perform Power Query transformations, verify relationships, refresh the model, and open the Executive Dashboard.

🔁 Reproducible Data Pipeline

main.py
   │
   ├── Generate Customers
   ├── Generate Products
   ├── Generate Stores
   ├── Generate Employees
   ├── Generate Orders
   ├── Generate Order Items
   ├── Generate Inventory
   ├── Generate Returns
   └── Generate Date Dimension
            │
            ▼
       data/*.csv
            │
            ▼
        Validation
            │
            ▼
       Power BI
            │
            ▼
    Executive Dashboard

🚀 Future Enhancements

Demand forecasting

Sales forecasting

Customer segmentation

RFM analysis

Customer churn prediction

Product recommendation

Inventory forecasting

Machine Learning models

Automated reporting

Anomaly detection

Real-time data pipelines

Cloud database integration

Power BI Service deployment

Automated refresh

🗣️ Interview Explanation

Tell me about your NEXUS project

NEXUS is an end-to-end Retail Business Intelligence and Analytics project. I started by generating a realistic retail dataset using Python and Pandas, covering customers, products, stores, employees, orders, order items, inventory, returns and dates. I then validated the generated data for record counts, unique IDs, relationships and financial consistency. After that, I imported the CSV datasets into Power BI and used Power Query for ETL and data-type preparation. I created relationships between the tables and built the analytical data model. Using DAX, I developed KPIs such as Total Sales, Total Orders, Gross Profit, Net Sales, Net Profit, Average Order Value, Return Rate and YoY Sales Growth. Finally, I built an interactive executive dashboard with sales trends, regional analysis, category analysis, profitability, returns and refund analysis. The overall objective was to transform raw retail data into structured business insights.

🧩 Architecture Explanation for HR

Data Generation Layer

Python generates the synthetic retail ecosystem.

Validation Layer

Pandas-based validation checks record counts, uniqueness, relationships and calculations.

Storage Layer

Validated datasets are stored as CSV files.

ETL Layer

Power Query cleans and prepares the datasets for analysis.

Data Modeling Layer

Power BI relationships connect customers, products, stores, employees, dates and transaction tables.

Analytics Layer

DAX measures calculate KPIs, profitability and time-based metrics.

Visualization Layer

Power BI converts the analytical model into an interactive executive dashboard.

Business Insight Layer

The dashboard enables users to explore sales, profitability, regional, category and return performance.

🏆 Project Highlights

Generated a multi-table retail ecosystem using Python.

Created 50,000 orders and 150,251 order-item records.

Built 9 interconnected datasets.

Implemented Python/Pandas data validation.

Built Power Query ETL workflows.

Created a structured Power BI data model.

Developed DAX-based financial and operational KPIs.

Implemented time-intelligence calculations.

Built an interactive executive dashboard.

Added regional, category, sales, profit, return and refund analysis.

Hosted the project on GitHub.

🎯 Project Outcome

NEXUS demonstrates a complete analytics workflow from synthetic raw retail data to an executive business intelligence dashboard.

Python
   +
Pandas
   +
Data Validation
   +
Power Query
   +
Data Modeling
   +
DAX
   +
Power BI
   +
GitHub

The result is a practical retail analytics portfolio project that demonstrates the complete data journey from generation and validation to modeling, visualization and business insight.

📌 Project Status

Completed — Python → Data Validation → CSV → Power Query → Data Modeling → DAX → Power BI

👨‍💻 Author

Avanish Tripathi
BCA — Data Science & Artificial Intelligence

Focus Areas

Data Analytics

Business Intelligence

Data Science

Machine Learning

Python

SQL

Power BI

Excel

🔗 Repository

GitHub:
https://github.com/Avii-tech898/Nexus

⭐ Project

If you find this project useful for learning Data Analytics and Business Intelligence, feel free to explore the repository.
