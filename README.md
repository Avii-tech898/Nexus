<img width="887" height="497" alt="image" src="https://github.com/user-attachments/assets/1e51c1e1-0556-4d83-8738-d0ca9858c911" /># 🚀 NEXUS — Retail Business Intelligence & Analytics Platform

> An end-to-end Retail Business Intelligence and Analytics project that transforms retail transaction data into meaningful business insights using Python, Pandas, Power BI, Data Modeling, and DAX.
<div align="center">

# 🚀 NEXUS
### Retail Business Intelligence & Analytics Platform

**From synthetic retail data to business insights**

`Python` → `Pandas` → `Validation` → `CSV` → `Power Query` → `Data Modeling` → `DAX` → `Power BI`

<p>
  <img src="https://img.shields.io/badge/Python-Data%20Generation-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/DAX-Analytics-6B4FBB?style=for-the-badge">
  <img src="https://img.shields.io/badge/GitHub-Portfolio-181717?style=for-the-badge&logo=github&logoColor=white">
</p>

**End-to-end Retail Analytics • Data Validation • ETL • Data Modeling • KPI Development • Executive Dashboard**

</div>

---

## 📊 Dashboard Preview

<div align="center">

<img src=C:\Users\avani\Downloads\NEXUS.png>

**NEXUS Executive Dashboard — Retail Business Performance Overview**

</div>

---

## ⚡ At a Glance

| 📦 Data Scale | 📈 Analytics | 🧩 Platform |
|---|---|---|
| **50K** Orders | Sales & Profitability | Power BI |
| **150,251** Order Items | YoY & YTD Analysis | Power Query |
| **10K** Customers | Returns & Refunds | DAX |
| **1K** Products | Regional & Category Analysis | Python + Pandas |
| **9** Connected Datasets | Executive KPIs | Git + GitHub |

---

## 🧭 Table of Contents

<details>
<summary><b>Click to expand</b></summary>

- [📌 Project Overview](#-project-overview)
- [🎯 Project Objectives](#-project-objectives)
- [💼 Business Problem](#-business-problem)
- [🏗️ Project Architecture](#️-project-architecture)
- [🔄 Complete Data Journey](#-complete-data-journey)
- [🛠️ Technology Stack](#️-technology-stack)
- [📊 Dataset](#-dataset)
- [🗂️ Dataset Details](#️-dataset-details)
- [🔍 Data Validation](#-data-validation)
- [🔄 ETL Process](#-etl-process)
- [🧮 Data Model](#-data-model)
- [📐 Core DAX Measures](#-core-dax-measures)
- [📊 Power BI Dashboard](#-power-bi-dashboard)
- [📁 Project Structure](#-project-structure)
- [📊 Key Project Metrics](#-key-project-metrics)
- [❓ Business Questions Answered](#-business-questions-answered)
- [🎓 Skills Demonstrated](#-skills-demonstrated)
- [⚙️ How to Run](#️-how-to-run-the-project)
- [🔁 Reproducible Data Pipeline](#-reproducible-data-pipeline)
- [🚀 Future Enhancements](#-future-enhancements)
- [🗣️ Interview Explanation](#️-interview-explanation)
- [🧩 Architecture Explanation for HR](#-architecture-explanation-for-hr)
- [🏆 Project Highlights](#-project-highlights)
- [🎯 Project Outcome](#-project-outcome)
- [👨‍💻 Author](#-author)

</details>

---

# 📌 Project Overview

**NEXUS** is an end-to-end Retail Business Intelligence and Analytics project designed to simulate a real-world retail data environment and convert raw transactional data into business-ready insights.

The project covers the complete data journey:

> **Data Generation → Data Validation → CSV Data Layer → Power Query ETL → Data Modeling → DAX → Power BI Dashboard → Business Insights**

NEXUS generates interconnected datasets for **customers, products, stores, employees, orders, order items, inventory, returns, and dates**. The validated data is prepared in Power BI and transformed into an interactive executive dashboard.

---

# 🎯 Project Objectives

| # | Objective |
|---:|---|
| 01 | Generate a realistic retail business dataset |
| 02 | Create interconnected customer, product, store and transaction data |
| 03 | Validate generated data using Python and Pandas |
| 04 | Prepare data using Power Query |
| 05 | Build a structured Power BI data model |
| 06 | Create business KPIs using DAX |
| 07 | Analyze sales, profitability, customers, products and returns |
| 08 | Build an interactive executive dashboard |
| 09 | Convert raw data into business-oriented insights |
| 10 | Demonstrate an end-to-end industry-style analytics workflow |

---

# 💼 Business Problem

Retail businesses generate large amounts of data across customers, products, stores, orders, inventory and returns. Raw transaction data is difficult to interpret directly.

NEXUS is designed to answer questions such as:

- 💰 What is total sales revenue?
- 🛒 How many orders are being processed?
- 🌍 Which regions generate the most sales?
- 📦 Which product categories contribute most to revenue?
- 📈 How profitable is the business?
- ↩️ How many returns are recorded?
- 💸 How much money is refunded?
- 📅 How is performance changing over time?
- 🔄 How does current-year sales compare with previous-year sales?

---

# 🏗️ Project Architecture

```text
┌───────────────────────────────┐
│       BUSINESS PROBLEM        │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│   PYTHON DATA GENERATION      │
│     Python + Pandas + NumPy   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       DATA VALIDATION         │
│   IDs • Counts • Consistency  │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│        CSV DATA LAYER         │
│       9 Connected Tables      │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│         POWER QUERY           │
│        ETL / Cleaning         │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       POWER BI MODEL          │
│  Relationships / Data Model   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│            DAX                │
│       KPIs / Analytics        │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       POWER BI DASHBOARD      │
│   Visuals • KPIs • Slicers    │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       BUSINESS INSIGHTS       │
└───────────────────────────────┘
```

### One-Line Architecture

```text
Python → Pandas → Data Validation → CSV → Power Query → Data Model → DAX → Power BI → Business Insights
```

---

# 🔄 Complete Data Journey

```text
01. Define Retail Business Requirements
              ↓
02. Generate Synthetic Retail Data
              ↓
03. Validate Data Quality
              ↓
04. Store Validated Data as CSV
              ↓
05. Import CSV Files into Power BI
              ↓
06. Transform Data using Power Query
              ↓
07. Set Correct Data Types
              ↓
08. Create Table Relationships
              ↓
09. Build Analytical Data Model
              ↓
10. Create DAX Measures
              ↓
11. Build KPIs & Visualizations
              ↓
12. Add Interactive Slicers
              ↓
13. Build Executive Dashboard
              ↓
14. Extract Business Insights
```

---

# 🛠️ Technology Stack

| Technology | Role in NEXUS |
|---|---|
| 🐍 **Python** | Synthetic retail data generation |
| 🐼 **Pandas** | Data manipulation and validation |
| 🔢 **NumPy** | Numerical operations |
| 📄 **CSV** | Data storage layer |
| 🔄 **Power Query** | ETL and data transformation |
| 📊 **Power BI** | Data modeling and dashboard development |
| 🧮 **DAX** | KPIs, profitability and time intelligence |
| 🌿 **Git** | Version control |
| 🐙 **GitHub** | Project hosting and portfolio |

---

# 📊 Dataset

NEXUS contains **9 interconnected datasets**.

| Dataset | Records | Purpose |
|---|---:|---|
| `customers.csv` | **10,000** | Customer master data |
| `products.csv` | **1,000** | Product catalog |
| `stores.csv` | **20** | Store and regional information |
| `employees.csv` | **100** | Employee information |
| `orders.csv` | **50,000** | Order-level transactions |
| `order_items.csv` | **150,251** | Product-level order transactions |
| `inventory.csv` | **20,000** | Store-product inventory |
| `returns.csv` | **8,894** | Return and refund transactions |
| `date_dimension.csv` | **1,096** | Date and time intelligence |

---

# 🗂️ Dataset Details

<details>
<summary>👥 <b>Customers</b></summary>

Customer master data including:

- Customer ID
- Name
- Gender
- Email
- Phone
- Date of Birth
- City
- State
- Country
- Registration Date

</details>

<details>
<summary>📦 <b>Products</b></summary>

Product catalog containing:

- Product ID
- Product Name
- Category
- Unit Cost
- Selling Price
- Launch Date

</details>

<details>
<summary>🏪 <b>Stores</b></summary>

Store information including:

- Store ID
- Store Name
- City
- State
- Region

</details>

<details>
<summary>👨‍💼 <b>Employees</b></summary>

Employee information including:

- Employee ID
- Employee Name
- Store ID
- Role

</details>

<details>
<summary>🛒 <b>Orders</b></summary>

Order-level information including:

- Order ID
- Customer
- Store
- Employee
- Order Date
- Channel
- Payment Method
- Order Status
- Shipping Location
- Total Amount
- Discount
- Shipping Cost

</details>

<details>
<summary>🧾 <b>Order Items</b></summary>

Product-level transaction information including:

- Order Item ID
- Order ID
- Product ID
- Quantity
- Unit Price
- Discount
- Total Price

</details>

<details>
<summary>📦 <b>Inventory</b></summary>

Store-product inventory information including stock quantity and reorder information.

</details>

<details>
<summary>↩️ <b>Returns</b></summary>

Return information including:

- Return ID
- Order ID
- Order Item ID
- Customer ID
- Product ID
- Return Date
- Return Reason
- Refund Amount

</details>

<details>
<summary>📅 <b>Date Dimension</b></summary>

Date attributes used for time-based analysis and DAX time intelligence.

</details>

---

# 🔍 Data Validation

Before Power BI analysis, the generated datasets were validated using **Python and Pandas**.

### Validation Checks

- ✅ Record count validation
- ✅ Unique ID validation
- ✅ Order consistency
- ✅ Customer consistency
- ✅ Product consistency
- ✅ Order-item relationships
- ✅ Missing value checks
- ✅ Transaction consistency
- ✅ Revenue validation
- ✅ Refund validation

### Validation Results

```text
Unique Order IDs      : 50,000
Unique Customer IDs   : 10,000
Unique Product IDs    : 1,000
Order Items Orders    : 50,000
Order Items Products  : 1,000
Total Revenue         : ₹8,911,493,900.79
Total Refund          : ₹448,451,497.51
```

---

# 🔄 ETL Process

Power Query is used as the ETL layer between CSV data and the Power BI model.

```text
CSV Files
   ↓
Import
   ↓
Column Review
   ↓
Data Type Conversion
   ↓
Date / Numeric Preparation
   ↓
Text Validation
   ↓
Relationship Preparation
   ↓
Power BI Model
```

### ETL Steps

1. Import CSV files
2. Review columns
3. Set correct data types
4. Convert date columns to Date
5. Convert IDs to Whole Number
6. Convert monetary fields to Decimal Number
7. Clean and validate text fields
8. Prepare tables for relationships
9. Apply transformations
10. Load the prepared model into Power BI

---

# 🧮 Data Model

## Dimension Tables

```text
Customers
Products
Stores
Employees
Date_Dimension
```

## Transaction Tables

```text
Orders
Order_Items
Inventory
Returns
```

### Simplified Model

```text
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
```

### Main Relationships

| From (1) | To (*) | Cardinality |
|---|---|---|
| `Customers[customer_id]` | `Orders[customer_id]` | **1 : \*** |
| `Products[product_id]` | `Order_Items[product_id]` | **1 : \*** |
| `Orders[order_id]` | `Order_Items[order_id]` | **1 : \*** |
| `Stores[store_id]` | `Orders[store_id]` | **1 : \*** |
| `Stores[store_id]` | `Inventory[store_id]` | **1 : \*** |
| `Products[product_id]` | `Inventory[product_id]` | **1 : \*** |
| `Employees[employee_id]` | `Orders[employee_id]` | **1 : \*** |
| `Date_Dimension[full_date]` | `Orders[order_date]` | **1 : \*** |

---

# 📐 Core DAX Measures

## 💰 Sales & Orders

```DAX
Total Sales =
SUM(Orders[total_amount])
```

```DAX
Total Orders =
DISTINCTCOUNT(Orders[order_id])
```

```DAX
Total Customers =
DISTINCTCOUNT(Customers[customer_id])
```

```DAX
Total Products =
DISTINCTCOUNT(Products[product_id])
```

```DAX
Total Quantity Sold =
SUM(Order_Items[quantity])
```

```DAX
Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders],
    0
)
```

```DAX
Total Shipping Cost =
SUM(Orders[shipping_cost])
```

## 💹 Profitability

```DAX
Total Cost =
SUMX(
    Order_Items,
    Order_Items[quantity] *
    RELATED(Products[unit_cost])
)
```

```DAX
Gross Profit =
[Total Sales] - [Total Cost]
```

```DAX
Profit Margin % =
DIVIDE(
    [Gross Profit],
    [Total Sales],
    0
)
```

```DAX
Net Sales =
[Total Sales] - [Total Refund]
```

```DAX
Net Profit =
[Net Sales] - [Total Cost] - [Total Shipping Cost]
```

```DAX
Net Profit Margin % =
DIVIDE(
    [Net Profit],
    [Net Sales],
    0
)
```

## ↩️ Returns

```DAX
Total Returns =
DISTINCTCOUNT(Returns[return_id])
```

```DAX
Total Refund =
SUM(Returns[refund_amount])
```

```DAX
Return Rate =
DIVIDE(
    [Total Returns],
    [Total Orders],
    0
)
```

## 📅 Time Intelligence

```DAX
Previous Year Sales =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(Date_Dimension[full_date])
)
```

```DAX
YoY Sales Growth % =
DIVIDE(
    [Total Sales] - [Previous Year Sales],
    [Previous Year Sales],
    0
)
```

```DAX
Previous Year Profit =
CALCULATE(
    [Gross Profit],
    SAMEPERIODLASTYEAR(Date_Dimension[full_date])
)
```

```DAX
YoY Profit Growth % =
DIVIDE(
    [Gross Profit] - [Previous Year Profit],
    [Previous Year Profit],
    0
)
```

```DAX
Sales YTD =
TOTALYTD(
    [Total Sales],
    Date_Dimension[full_date]
)
```

---

# 📊 Power BI Dashboard

The **NEXUS Executive Dashboard** provides an interactive view of retail business performance.

### 🎯 KPI Cards

- 💰 Total Sales
- 🛒 Total Orders
- 📈 Gross Profit
- 👥 Total Customers
- 💵 Average Order Value

### 📈 Visualizations

| Visualization | Purpose |
|---|---|
| 📈 Monthly Sales Trend | Analyze sales over time |
| 🌍 Sales by Region | Compare regional performance |
| 🥧 Sales by Category | Analyze category contribution |
| 💹 Gross Profit Trend | Track profitability over time |
| ↩️ Returns by Reason | Analyze return patterns |
| 💸 Refund Amount by Reason | Analyze refund impact |
| 📊 YoY Sales Performance | Compare current vs previous year |
| 📈 YoY Sales Growth % | Track year-over-year growth |

### 🎛️ Interactive Slicers

- Year
- Region
- Category
- Channel
- Order Status

---

# 📁 Project Structure

```text
NEXUS/
│
├── 📂 Data_generator/
│   └── 📂 data/
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
├── 📂 data/
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
├── 📂 dashboard/
│   └── dashboard_preview.png
│
├── config.py
├── main.py
├── init.py
├── .gitignore
└── README.md
```

---

# 📊 Key Project Metrics

| Metric | Value |
|---|---:|
| 👥 Customers | **10,000** |
| 📦 Products | **1,000** |
| 🏪 Stores | **20** |
| 👨‍💼 Employees | **100** |
| 🛒 Orders | **50,000** |
| 🧾 Order Items | **150,251** |
| 📦 Inventory Records | **20,000** |
| ↩️ Returns | **8,894** |
| 📅 Date Records | **1,096** |
| 💰 Total Revenue | **₹8.91B** |
| 💸 Total Refund | **₹448.45M** |

---

# ❓ Business Questions Answered

### 💰 Sales
- What is total sales revenue?
- How are sales changing over time?
- Which regions contribute to sales?
- Which categories contribute to revenue?

### 🛒 Orders
- How many orders are processed?
- What is the average order value?
- How does order performance change over time?

### 📦 Products
- Which categories contribute most to sales?
- How do product costs affect profitability?
- Which products can be investigated further for performance?

### 👥 Customers
- How many customers are represented?
- How does customer activity vary geographically?
- Which customer dimensions can support segmentation?

### 💹 Profitability
- What is gross profit?
- What is net profit?
- What is the profit margin?
- How does profitability change over time?

### ↩️ Returns
- How many returns are recorded?
- What are the major return reasons?
- How much money is refunded?
- What is the return rate?

### 📅 Time Performance
- What is current-year sales performance?
- How does current performance compare with the previous year?
- What is YoY sales growth?
- What is Sales YTD?

---

# 🎓 Skills Demonstrated

| 📊 Data & Analytics | 📈 BI & Modeling | 💻 Development & Delivery |
|---|---|---|
| Data generation | Power Query | Python |
| Data cleaning | Data modeling | Pandas |
| Data validation | Relationships | NumPy |
| KPI development | DAX | Git |
| Sales analysis | Time intelligence | GitHub |
| Profitability analysis | Power BI | Documentation |
| Return analysis | Dashboard development | Business storytelling |

---

# ⚙️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Avii-tech898/Nexus.git
```

## 2️⃣ Navigate to the Project

```bash
cd Nexus
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

## 4️⃣ Install Dependencies

```bash
pip install pandas numpy
```

## 5️⃣ Generate the Dataset

Run the main pipeline from the NEXUS root:

```bash
python main.py
```

## 6️⃣ Validate the Data

```bash
python Data_generator/data/validate_data.py
```

## 7️⃣ Build / Refresh Power BI

Import the generated CSV files into Power BI, perform Power Query transformations, verify relationships, refresh the model, and open the Executive Dashboard.

---

# 🔁 Reproducible Data Pipeline

```text
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
```

---

# 🚀 Future Enhancements

- 🔮 Demand forecasting
- 📈 Sales forecasting
- 👥 Customer segmentation
- 🎯 RFM analysis
- 🔄 Customer churn prediction
- 🤝 Product recommendation
- 📦 Inventory forecasting
- 🤖 Machine Learning models
- 📧 Automated reporting
- 🚨 Anomaly detection
- ☁️ Cloud database integration
- 🌐 Power BI Service deployment
- 🔄 Automated data refresh
- ⚡ Real-time data pipelines

---

# 🗣️ Interview Explanation

### "Tell me about your NEXUS project."

> **NEXUS is an end-to-end Retail Business Intelligence and Analytics project. I started by generating a realistic retail dataset using Python and Pandas, covering customers, products, stores, employees, orders, order items, inventory, returns and dates. I then validated the generated data for record counts, unique IDs, relationships and financial consistency. After that, I imported the CSV datasets into Power BI and used Power Query for ETL and data-type preparation. I created relationships between the tables and built the analytical data model. Using DAX, I developed KPIs such as Total Sales, Total Orders, Gross Profit, Net Sales, Net Profit, Average Order Value, Return Rate and YoY Sales Growth. Finally, I built an interactive executive dashboard with sales trends, regional analysis, category analysis, profitability, returns and refund analysis. The overall objective was to transform raw retail data into structured business insights.**

---

# 🧩 Architecture Explanation for HR

| Layer | What happens |
|---|---|
| 🐍 **Data Generation** | Python generates the synthetic retail ecosystem |
| 🔍 **Validation** | Pandas checks counts, uniqueness, relationships and calculations |
| 📄 **Storage** | Validated datasets are stored as CSV files |
| 🔄 **ETL** | Power Query cleans and prepares the datasets |
| 🧮 **Data Modeling** | Power BI relationships connect dimensions and transaction tables |
| 📐 **Analytics** | DAX calculates KPIs, profitability and time-based metrics |
| 📊 **Visualization** | Power BI converts the model into an executive dashboard |
| 💡 **Business Insight** | Dashboard supports sales, profitability, regional, category and return analysis |

---

# 🏆 Project Highlights

- ✅ Generated a multi-table retail ecosystem using Python
- ✅ Created **50,000 orders**
- ✅ Created **150,251 order-item records**
- ✅ Built **9 interconnected datasets**
- ✅ Implemented Python/Pandas data validation
- ✅ Built Power Query ETL workflows
- ✅ Created a structured Power BI data model
- ✅ Developed DAX-based financial and operational KPIs
- ✅ Implemented time-intelligence calculations
- ✅ Built an interactive executive dashboard
- ✅ Added regional, category, sales, profit, return and refund analysis
- ✅ Hosted the project on GitHub

---

# 🎯 Project Outcome

NEXUS demonstrates a complete analytics workflow from **synthetic raw retail data to an executive business intelligence dashboard**.

```text
        Python
           +
        Pandas
           +
    Data Validation
           +
      CSV Storage
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
           ↓
   Business Insights
```

The result is a practical retail analytics portfolio project demonstrating the complete data journey from **generation and validation to modeling, visualization and business insight**.

---

# 📌 Project Status

<div align="center">

### 🟢 COMPLETED

**Python → Data Validation → CSV → Power Query → Data Modeling → DAX → Power BI**

</div>

---

# 👨‍💻 Author

<div align="center">

## **Avanish Tripathi**

**BCA — Data Science & Artificial Intelligence**

**Focus Areas**

`Data Analytics` · `Business Intelligence` · `Data Science` · `Machine Learning` · `Python` · `SQL` · `Power BI` · `Excel`

</div>

---

# 🔗 Repository

<div align="center">

### 🐙 GitHub

**https://github.com/Avii-tech898/Nexus**

</div>

---

<div align="center">

### ⭐ NEXUS — Turning Retail Data into Business Insights

**Built with Python • Pandas • Power Query • DAX • Power BI**

</div>
