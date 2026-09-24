
# 📊 MetricMind

### Conversational Business Intelligence & Business Analytics Platform

MetricMind is a business intelligence project focused on transforming corporate sales data into meaningful business insights through data analysis, reusable business metrics, interactive visualizations, and dashboards.

The project aims to help users explore business performance, understand key performance indicators (KPIs), and make data-driven decisions using structured data and natural language interaction.

---

## 🚀 Project Overview

MetricMind analyzes corporate sales data to provide insights into:

- Revenue and profit performance
- Regional sales performance
- Product category analysis
- Sales channel performance
- Monthly revenue trends
- Overall profit margins
- Top-performing products

The project is being developed incrementally, beginning with data analysis and dashboard development and progressing toward a conversational business intelligence platform.

---

## 🛠️ Technologies Used

### Current Technologies

- **Python** — Data analysis and business logic
- **Pandas** — Data cleaning, transformation, and aggregation
- **Matplotlib** — Business data visualizations
- **Streamlit** — Interactive dashboard development
- **CSV** — Corporate sales dataset storage
- **Git & GitHub** — Version control and collaboration

### Planned Technologies

- PostgreSQL / Snowflake — Data storage
- dbt — Data transformation and modeling
- Cube.dev — Semantic layer and governed metrics
- FastAPI — Backend API development
- LLM integration — Natural language business queries
- LangChain — LLM application development

---

## 📁 Project Structure

```text
MetricMind/
│
├── data/
│   ├── corporate_data_.csv
│   ├── category_metrics.csv
│   ├── channel_metrics.csv
│   └── region_metrics.csv
│
├── reports/
│   └── charts/
│       ├── monthly_revenue_trend.png
│       ├── profit_by_category.png
│       ├── revenue_by_channel.png
│       └── revenue_by_region.png
│
├── src/
│   ├── data_exploration.py
│   ├── business_metrics.py
│   ├── metrics.py
│   ├── test_metrics.py
│   ├── visualizations.py
│   └── dashboard.py
│
├── README.md
└── .gitignore
```

---

## 📈 Current Features

### 1. Data Exploration

- Dataset shape and column inspection
- Data type analysis
- Missing-value checks
- Date conversion and validation
- Numerical data summaries

### 2. Business Metrics

Reusable Python functions for calculating:

- Total revenue
- Total profit
- Total quantity sold
- Regional performance
- Category performance
- Sales channel performance
- Overall profit margin
- Average order revenue
- Monthly revenue and profit
- Top products by revenue

### 3. Data Visualizations

The project generates business charts using Matplotlib:

- Revenue by region
- Profit by category
- Revenue by sales channel
- Monthly revenue trend

Generated charts are stored in the `reports/charts/` directory.

### 4. Interactive Streamlit Dashboard

The dashboard currently provides:

- Total revenue KPI
- Total profit KPI
- Total quantity sold KPI
- Overall profit margin KPI
- Region-based filtering
- Category-based filtering
- Revenue by region visualization
- Profit by category visualization
- Revenue by sales channel visualization
- Monthly revenue trend
- Filtered data preview

---

## 📊 Dataset

The project currently uses a corporate sales dataset containing the following fields:

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `order_date` | Date of the order |
| `customer_id` | Customer identifier |
| `product_id` | Product identifier |
| `product_name` | Name of the product |
| `category` | Product category |
| `region` | Sales region |
| `country` | Country of sale |
| `quantity` | Quantity sold |
| `unit_price` | Price per unit |
| `revenue` | Total revenue |
| `cost` | Total cost |
| `profit` | Total profit |
| `sales_channel` | Sales channel |
| `profit_margin_pct` | Profit margin percentage |

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/bhavyachenreddy/MetricMind.git
```

### 2. Navigate to the Project

```bash
cd MetricMind
```

### 3. Install Dependencies

```bash
python -m pip install pandas matplotlib streamlit
```

### 4. Run the Data Analysis Scripts

```bash
python src/data_exploration.py
```

```bash
python src/business_metrics.py
```

### 5. Generate Visualizations

```bash
python src/visualizations.py
```

### 6. Launch the Streamlit Dashboard

```bash
python -m streamlit run src/dashboard.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

---

## 🎯 Project Goals

The long-term objective of MetricMind is to develop a conversational business intelligence platform that enables users to interact with business data using natural language.

Planned improvements include:

- Governed and reusable business metrics
- Data modeling and transformation pipelines
- Backend APIs
- Natural language query processing
- LLM-powered business insights
- Role-based access and data governance
- Interactive business intelligence workflows

---

## 🔮 Future Enhancements

- [ ] Add date-range filters
- [ ] Add top-product analysis to the dashboard
- [ ] Add revenue and profit comparison charts
- [ ] Add downloadable filtered reports
- [ ] Improve dashboard layout and styling
- [ ] Add automated data validation
- [ ] Integrate a relational database
- [ ] Build backend APIs
- [ ] Add semantic-layer integration
- [ ] Implement natural language business queries
- [ ] Integrate LLM-based business insights

---

## 🤝 Team Collaboration

MetricMind is being developed collaboratively using Git and GitHub.

Development workflow:

```text
Create Feature
     ↓
Test Changes
     ↓
Commit Changes
     ↓
Push Feature Branch
     ↓
Create Pull Request
     ↓
Code Review
     ↓
Merge Changes
```

---

## 📌 Project Status

**Current Phase:** Data Analysis, Business Metrics, Visualization, and Streamlit Dashboard Development

The project is being developed incrementally, with future plans to expand into a complete conversational business intelligence application.

---

## 👨‍💻 Contributors

Developed collaboratively by the MetricMind project team.

---

⭐ If you find this project useful, consider starring the repository.