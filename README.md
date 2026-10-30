# E-commerce Product Analytics & Growth Intelligence

An end-to-end data analytics project focused on understanding e-commerce customer behaviour, product performance, revenue trends, order status, and business growth opportunities using Python, SQL, statistics, and data automation.

## 1. Business Problem

An e-commerce business wants to understand:

- Which products and categories generate the highest revenue?
- How do customers behave, and how much revenue comes from repeat customers?
- Which cities and acquisition channels perform best?
- What are the cancellation and return patterns?
- How can customer retention and business performance be improved?

The objective is to transform raw transactional and application-event data into actionable business insights.

## 2. Technology Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Database | MySQL |
| Querying | SQL, Joins, CTEs, Window Functions |
| Statistics | SciPy, Hypothesis Testing |
| Automation | Python, Logging, Papermill |
| Documentation | Git, GitHub, Jupyter Notebook |

## 3. Project Workflow

1. **Data Understanding:** Inspected datasets, data types, missing values, duplicate records, and data quality issues.
2. **Data Cleaning:** Removed duplicates, standardized values, handled missing fields, and validated financial calculations.
3. **Exploratory Data Analysis:** Analyzed revenue, products, categories, customers, cities, payment methods, and order trends.
4. **Statistical Analysis:** Developed descriptive statistics, correlation analysis, confidence intervals, hypothesis tests, and an A/B testing simulation.
5. **SQL Analysis:** Used MySQL to calculate business KPIs, customer segments, repeat purchases, revenue trends, and product performance.
6. **Automation:** Developed a reusable Python pipeline for cleaning, validation, KPI generation, reporting, and logging.

## 4. Dataset Overview

The project uses independently generated synthetic e-commerce datasets. They do not represent actual company or customer transactions.

| Dataset | Raw Records | Cleaned Records |
|---|---:|---:|
| Application Events | 12,035 | 12,000 |
| Orders | 3,612 | 3,600 |

The datasets cover approximately October 2023 to October 2026.

## 5. Key Business KPIs

The following KPIs are calculated using delivered orders unless otherwise specified.

| KPI | Result |
|---|---:|
| Total Orders | 3,600 |
| Delivered Orders | 2,550 |
| Unique Delivered Customers | 1,639 |
| Units Sold | 3,298 |
| Delivered Revenue | ₹42,80,663.88 |
| Average Order Value | ₹1,678.69 |
| Repeat Customer Share | 40.95% |
| Repeat Customer Revenue Share | 62.08% |
| Cancellation Rate | 7.97% |
| Return Rate | 6.33% |

## 6. Key Business Insights

### Revenue and Product Performance

- Electronics contributed 28.52% of delivered revenue.
- Home & Kitchen contributed 24.93%.
- Electronics and Home & Kitchen together generated 53.45% of delivered revenue.
- Mixer Grinder was the highest-revenue product, generating ₹7,87,040.55.

### Customer Behaviour

- Repeat customers represented 40.95% of delivered customers.
- Repeat customers generated 62.08% of delivered revenue.
- The analysis identified 671 repeat customers and 968 one-time customers.

### Geographic Performance

- Kolkata recorded the highest average order value at ₹1,823.88.
- Ahmedabad recorded the lowest average order value at ₹1,558.88.
- Electronics was the leading revenue category in 7 out of 10 cities.

### Order Status and Returns

- 70.83% of orders were delivered.
- 7.97% were cancelled.
- 6.33% were returned.
- Fashion and Sports had the highest category-level return rates at 7.63% and 7.45%, respectively.

### Customer Segmentation

Customer segmentation identified Champions, Loyal Customers, Potential Customers, At Risk High Value, and Inactive Customers.

The analysis classified 87.37% of delivered customers as inactive based on the project's 90-day activity rule.

## 7. Business Recommendations

1. **Improve Customer Retention:** Develop loyalty campaigns and repeat-purchase incentives.
2. **Win Back Inactive Customers:** Use targeted re-engagement campaigns for customers without recent delivered purchases.
3. **Improve Product Quality:** Investigate return patterns in Fashion and Sports categories.
4. **Optimize Product Strategy:** Monitor high-revenue products and category-level performance.
5. **Review Payment Experience:** Investigate differences in cancellation and return rates across payment methods.
6. **Improve Regional Strategy:** Use city-level revenue and AOV differences to identify growth opportunities.

These are analytical recommendations and hypotheses, not proven causal relationships.

## 8. Automation Pipeline

A reusable Python pipeline was developed to:

- Load raw CSV datasets.
- Clean and transform application events and orders.
- Remove duplicate records.
- Validate important data quality conditions.
- Generate KPI reports.
- Export cleaned datasets and quality reports.
- Maintain execution logs.

The pipeline was tested interactively, and the Jupyter notebook was executed using Papermill.

## 9. Repository Structure

```text
product-analytics/
│
├── Data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Understanding_and_Quality_Assessment.ipynb
│   ├── 02_Data_Cleaning_and_Transformation.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Statistical_Analysis.ipynb
│   └── 05_Automation_Pipeline.ipynb
│
├── automation/
│   ├── data_pipeline.py
│   ├── run_pipeline.bat
│   └── logs/
│
├── reports/
│
├── .gitignore
└── README.md
```

## 10. Project Limitations

- The datasets are synthetic and independently generated.
- Application events do not provide reliable sequential user sessions, so a valid conversion funnel could not be calculated.
- Reliable cohort retention analysis was not established.
- Marketing spend is unavailable, so CAC and ROAS cannot be calculated.
- Product cost and margin information is unavailable, so profit analysis is outside the current scope.
- Return reasons and delivery timestamps are unavailable.
- Monthly and yearly comparisons involving partial periods should be interpreted carefully.
- Statistical tests and simulated A/B tests require their results to be interpreted separately from observed business KPIs.

## 11. How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Ganesh9110/product-analytics.git
```

2. Navigate to the project directory:

```bash
cd product-analytics
```

3. Install the required Python packages:

```bash
pip install pandas numpy matplotlib scipy jupyter papermill
```

4. Open Jupyter Notebook:

```bash
jupyter notebook
```

5. Execute the notebooks in numerical order.

6. Configure MySQL separately if you want to reproduce the SQL analysis.

## 12. Author

**Kolluri Venkata Ganesh**

Aspiring Data Analyst | Business Intelligence | Product Analytics

GitHub: https://github.com/Ganesh9110

Portfolio: https://ganesh9110.github.io/Ganesh-Portfolio/

---

*This project demonstrates an end-to-end analytical workflow, from data understanding and cleaning to business analysis, statistical exploration, SQL querying, and automation.*
