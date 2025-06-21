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
| 2024-06-01 | Food         | 100    |
| 2024-06-02 | Entertainment| 200    |

### Deploy Online (Optional)
- Push this repo to GitHub
- Go to https://streamlit.io/cloud and deploy your app for free!