🚗 Hyundai Car Sales Dashboard App
🔍 About the Project
This project is a web-based dashboard app designed to analyze Hyundai car sales data from Excel files. It allows users to:

Upload an Excel file containing car booking/purchase data

Automatically process dates and group sales by Day, Week, or Year

Generate insightful visualizations like matrix tables, bar charts, and pie charts

💡 Key Features
📁 Upload a structured Excel file with car data

📆 View data summarized by daily, weekly, or yearly timeframes

📊 Visualize:

Matrix (tabular view of car counts by period)

Bar chart (number of cars sold per time period)

Pie chart (popular models or car names)

⚙️ Fully interactive dashboard built using Python and Streamlit

🧩 Tech Stack
Python 3

Streamlit – For building the interactive web UI

Pandas – For data handling and grouping

Plotly – For generating clean, interactive charts

Openpyxl – For reading Excel files

📂 Required Excel Format
Your Excel should have columns like:

Date	Car Name	Model Name
2024-01-24	Hyundai Creta	GLS
2023-04-15	Hyundai Alcazar	Signature
2024-02-26	Hyundai i20	S

✅ Date is used for time-based grouping
✅ Car Name / Model Name can be used in pie or bar chart visualizations

🧑‍💻 Ideal For
Car dealerships or sales analysts

Automotive data reporting

Business dashboards

Portfolio/demo projects in data analysis or Python development

🚀 How It Works
Upload your Excel file (.xlsx)

App reads and parses the Date, Car Name, and Model Name columns

Choose how to group the data (Day, Week, or Year)

Instantly view the result as a matrix + visual charts

# Excel Dashboard App (Streamlit)

## Overview
Upload an Excel file with `Date` and numeric columns, and get instant visualizations (Daily, Weekly, Yearly) in matrix, bar, and pie chart formats.

## How to Use

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run simple_dashboard.py
```

### 3. Upload Excel File
Ensure your Excel file has at least the following columns:
- Date
- Amount (or any numeric value)

### Example Excel Format
| Date       | Category     | Amount |
|------------|--------------|--------|
| 2024-06-01 | i10         | 100    |
| 2024-06-02 | i20         | 200    |

