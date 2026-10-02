# 📊 MetricMind

### Conversational Business Intelligence & Business Analytics Platform

MetricMind is a Business Intelligence platform focused on transforming corporate sales data into meaningful, governed, and explainable business insights.

The project started with data exploration, reusable business metrics, visualizations, and an interactive dashboard, and has progressively evolved toward a conversational Business Intelligence platform where users can interact with business metrics using natural language.

---

## 🚀 Project Overview

MetricMind analyzes corporate sales data to provide insights into:

- Revenue and profit performance
- Regional sales performance
- Product category analysis
- Sales channel performance
- Monthly revenue trends
- Overall profit margins
- Business metric analysis
- Natural-language metric queries
- Business explanations
- Multi-step business analysis
- Dynamic visualizations
- Query transparency
- Query governance

The project follows a governed analytics approach where business metrics are defined consistently and the application does not rely on uncontrolled interpretation of raw business data.

---

# 🎯 Project Objective

The main objective of MetricMind is to develop a conversational Business Intelligence platform that allows users to interact with governed business metrics using natural language.

Instead of manually analyzing raw data or writing SQL queries, users should be able to ask questions such as:

```text
Show revenue by region

or:

Show profit by category

and receive structured business results, explanations, and visualizations.

🧩 Problem Statement

Businesses generate large amounts of sales data containing information about orders, products, customers, regions, revenue, cost, and profit.

However, raw business data can be difficult to analyze manually.

Common challenges include:

Business users may not know SQL.
The same business metric may be calculated differently by different users.
Raw data can contain many dimensions and measures.
Numerical results alone may not explain the business meaning.
Uncontrolled natural-language queries can request unsupported metrics or dimensions.

MetricMind addresses these challenges by introducing reusable business metrics, a semantic layer, natural-language interaction, business explanations, visualizations, transparency, and query governance.

🛠️ Technologies Used
Current Technologies
Python — Data analysis, business logic, and application components
Pandas — Data processing and aggregation
Matplotlib — Business visualizations
Streamlit — Interactive dashboard
Cube — Semantic layer
OpenAI API integration — LLM integration layer
Git & GitHub — Version control and collaboration
CSV — Current corporate sales dataset
Project Architecture Technologies
Snowflake — Data warehouse layer
dbt — Data transformation and modeling
Cube.dev — Semantic layer and governed metrics
Backend API — Application-level metric access
LLM integration — Natural-language interaction
📁 Project Structure
MetricMind/
│
├── cube/
│   ├── cube.js
│   ├── package.json
│   └── model/
│       └── sales.yml
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
│       ├── revenue_by_region.png
│       ├── dynamic_revenue_by_region.png
│       └── dynamic_monthly_revenue.png
│
├── src/
│   ├── application_testing.py
│   ├── backend_api.py
│   ├── business_explanations.py
│   ├── business_metrics.py
│   ├── chat_ui.py
│   ├── dashboard.py
│   ├── data_exploration.py
│   ├── dynamic_visualizations.py
│   ├── llm_integration.py
│   ├── metrics.py
│   ├── multi_step_reasoning.py
│   ├── natural_language_queries.py
│   ├── query_governance.py
│   ├── semantic_api.py
│   ├── test_governance.py
│   ├── test_metrics.py
│   ├── transparency.py
│   └── visualizations.py
│
├── README.md
├── requirements.txt
└── .gitignore
📊 Dataset

The main dataset is:

data/corporate_data_.csv

The dataset contains corporate sales information including:

Column	Description
order_id	Unique order identifier
order_date	Date of the order
customer_id	Customer identifier
product_id	Product identifier
product_name	Name of the product
category	Product category
region	Sales region
country	Country of sale
quantity	Quantity sold
unit_price	Price per unit
revenue	Total revenue
cost	Total cost
profit	Total profit
sales_channel	Sales channel
profit_margin_pct	Profit margin percentage
📈 Current Business Metrics

MetricMind calculates reusable business metrics including:

Total revenue
Total profit
Total quantity sold
Profit margin
Regional performance
Category performance
Sales channel performance
Monthly revenue
Monthly profit
Average order revenue
Top-product analysis
Example Overall Metrics
Metric	Value
Total Revenue	51,078,276.55
Total Profit	17,955,389.77
Total Quantity	34,081
Profit Margin	35.15%
🌎 Revenue by Region
Region	Revenue
North	13,570,772.18
South	13,002,574.40
West	12,277,613.87
East	12,227,316.10
🏷️ Revenue by Category
Category	Revenue
Electronics	14,044,080.10
Office Supplies	10,972,876.60
Furniture	9,478,420.21
Software	8,994,170.63
Services	7,588,729.01
📢 Revenue by Sales Channel
Sales Channel	Revenue
Online	26,350,189.43
Offline	15,189,643.87
Partner	9,538,443.25
📊 Data Visualizations

MetricMind generates business visualizations using Matplotlib.

Current visualizations include:

Revenue by region
Profit by category
Revenue by sales channel
Monthly revenue trend
Dynamic revenue by region
Dynamic monthly revenue

Generated charts are stored in:

reports/charts/
🖥️ Interactive Streamlit Dashboard

The Streamlit dashboard provides:

Total Revenue KPI
Total Profit KPI
Total Quantity Sold KPI
Overall Profit Margin KPI
Region filtering
Category filtering
Revenue by region
Profit by category
Revenue by sales channel
Monthly revenue trend
Filtered data preview

Run the dashboard using:

python -m streamlit run src/dashboard.py

The application will normally be available at:

http://localhost:8501
🧠 Semantic Layer

MetricMind includes a semantic layer using Cube.

The semantic layer provides a governed interface for business metrics and dimensions.

The architecture is:

Raw Business Data
        ↓
Semantic Layer
        ↓
Governed Business Metrics
        ↓
MetricMind Application

This approach helps maintain consistent business definitions and reduces uncontrolled interpretation of raw business tables.

🔌 Semantic API

MetricMind includes a semantic API client that communicates with the semantic layer.

MetricMind
     ↓
Semantic API
     ↓
Cube
     ↓
Business Metrics

Implementation:

src/semantic_api.py
⚙️ Backend Metrics API

The project includes a backend metrics API that provides an application-level interface for accessing business metrics.

Chat UI
   ↓
Backend API
   ↓
Semantic API
   ↓
Cube
   ↓
Business Metrics

Implementation:

src/backend_api.py
💬 Chat UI

MetricMind includes a conversational interface that allows users to enter business questions using natural language.

Example:

Show me revenue by region

The query is then passed through the MetricMind processing workflow.

Implementation:

src/chat_ui.py
🤖 LLM Integration

MetricMind contains an LLM integration layer for processing natural-language business questions.

Implementation:

src/llm_integration.py

The main function is:

ask_llm(prompt)

The integration is designed to connect natural-language questions with the MetricMind business-metric workflow.

The external LLM API requires an available API account/credit balance. The project also contains local data-grounded functionality for demonstration when the external API is unavailable.

🗣️ Natural Language Metric Queries

MetricMind can identify the type of business metric requested in a natural-language question.

Example:

Show me revenue by region

The system identifies the request as a revenue query.

Another example:

Show me revenue and profit by region

The system identifies it as a combined revenue-and-profit query.

Implementation:

src/natural_language_queries.py

The basic workflow is:

User Question
      ↓
Query Type Detection
      ↓
Metric Prompt
      ↓
LLM / Processing Layer
💡 Business Explanations

MetricMind includes a business explanation layer.

The purpose is to convert metric results into concise, business-readable explanations instead of presenting only raw numerical values.

Implementation:

src/business_explanations.py

Example input:

North: ₹13,570,772
South: ₹13,002,574
West: ₹12,277,614
East: ₹12,227,316

The system can convert the metric result into a structured business explanation.

🔎 Multi-Step Business Reasoning

MetricMind includes a multi-step regional margin analysis workflow.

The analysis performs:

Region filtering
Revenue calculation
Cost calculation
Profit calculation
Profit margin calculation

Workflow:

Region
   ↓
Filter Data
   ↓
Revenue
   ↓
Cost
   ↓
Profit
   ↓
Profit Margin
   ↓
Business Explanation

Implementation:

src/multi_step_reasoning.py
📉 Dynamic Visualizations

MetricMind includes dynamic chart generation.

Currently implemented chart types include:

Regional Comparison

Bar chart:

Revenue by Region
Time-Series Analysis

Line chart:

Monthly Revenue Trend

Implementation:

src/dynamic_visualizations.py
🔍 Transparency

MetricMind includes a transparency layer to show how a business query is represented.

Transparency information includes:

User question
Metric
Dimensions
Filters
SQL representation

Example:

Question:
Show revenue by region

Metric:
Revenue

Dimensions:
Region

Filters:
{}

SQL:
SELECT
    region,
    SUM(revenue) AS revenue
FROM corporate_data
GROUP BY region
ORDER BY revenue DESC;

Implementation:

src/transparency.py
🛡️ Query Governance

MetricMind restricts queries to approved metrics and dimensions.

Approved Metrics
revenue
profit
quantity
profit_margin
Approved Dimensions
region
category
sales_channel
order_date

Unsupported metrics or dimensions are rejected.

Example:

Revenue + Region
        ↓
     ALLOWED
Customer Salary + Region
        ↓
     REJECTED

Implementation:

src/query_governance.py
🧪 Application Testing

MetricMind includes application-level testing for important components.

Tests include:

Revenue queries
Profit queries
Invalid metric rejection
Invalid dimension rejection
Regional margin analysis
Business explanation generation
Dynamic visualization generation

Run:

python src/application_testing.py

Expected result:

All MetricMind application tests passed.
🏗️ System Architecture

The overall MetricMind workflow is:

                         ┌───────────────┐
                         │     User      │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    Chat UI    │
                         └───────┬───────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │ Natural Language Query │
                    └────────────┬───────────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ LLM / Query   │
                         │  Processing    │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │  Governance   │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ Backend API   │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ Semantic API  │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │     Cube      │
                         └───────┬───────┘
                                 │
                                 ▼
                       ┌────────────────────┐
                       │ Business Metrics   │
                       └─────────┬──────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
             Explanation   Visualization  Transparency
📅 20-Day Development Roadmap
Days 1–13 — Foundation & Conversational Pipeline
Day	Work
Day 1	Project Setup
Day 2	Mock Data Creation
Day 3	Snowflake Setup
Day 4	dbt Staging
Day 5	Analytics Data Model
Day 6	Metric Definitions
Day 7	Semantic Layer Setup
Day 8	Semantic API
Day 9	Governance Testing
Day 10	Backend Metrics API
Day 11	Chat UI
Day 12	LLM Integration
Day 13	Natural Language Queries
Days 14–20 — Intelligence, Governance & Finalization
Day	Work
Day 14	Business Explanations
Day 15	Multi-Step Reasoning
Day 16	Dynamic Visualizations
Day 17	Transparency
Day 18	Query Governance
Day 19	Application Testing
Day 20	Final Documentation & Demo
🔄 Complete Business Workflow

A simplified MetricMind workflow is:

1. User asks a business question
             ↓
2. Natural-language query processing
             ↓
3. Identify requested metric and dimensions
             ↓
4. Apply query governance
             ↓
5. Access governed business metrics
             ↓
6. Perform required calculations
             ↓
7. Generate business explanation
             ↓
8. Generate visualization when required
             ↓
9. Provide transparency information
             ↓
10. Return business insight
🔐 Design Principle

A core design principle of MetricMind is:

The LLM should not have uncontrolled direct access to raw business tables.

Instead, the intended workflow is:

LLM
 ↓
Governed Semantic Layer
 ↓
Approved Metrics
 ↓
Business Data

This helps maintain consistent business definitions and controlled access to business metrics.

▶️ Installation
1. Clone the Repository
git clone https://github.com/bhavyachenreddy/MetricMind.git
2. Navigate to the Project
cd MetricMind
3. Install Dependencies
python -m pip install -r requirements.txt

If required:

python -m pip install openai
▶️ Running the Project
Data Exploration
python src/data_exploration.py
Business Metrics
python src/business_metrics.py
Visualizations
python src/visualizations.py
Business Explanations
python src/business_explanations.py
Multi-Step Reasoning
python src/multi_step_reasoning.py
Dynamic Visualizations
python src/dynamic_visualizations.py
Transparency
python src/transparency.py
Query Governance
python src/query_governance.py
Application Testing
python src/application_testing.py
Streamlit Dashboard
python -m streamlit run src/dashboard.py
🔑 LLM Configuration

The LLM integration reads the API key from an environment variable.

Windows PowerShell:

$env:OPENAI_API_KEY="YOUR_API_KEY"

Verify without displaying the secret:

python -c "import os; print('API key configured:', bool(os.getenv('OPENAI_API_KEY')))"

Never commit API keys to GitHub.

🤝 Team Collaboration

MetricMind is developed collaboratively using Git and GitHub.

Development workflow:

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
Merge into Main
📌 Project Status
Current Phase: Final Demonstration & Documentation

MetricMind has progressed from a basic data-analysis project into a prototype conversational Business Intelligence platform.

Current implemented areas include:

Data analysis
Business metrics
Data visualizations
Streamlit dashboard
Semantic layer components
Semantic API
Backend metrics API
Chat UI
LLM integration layer
Natural-language metric queries
Business explanations
Multi-step reasoning
Dynamic visualizations
Transparency
Query governance
Application testing
Final documentation

Some external services, such as the live LLM API, depend on external account configuration and availability.

🔮 Future Enhancements

Potential future improvements include:

More advanced natural-language query understanding
Additional business metrics
More dimensions and filters
Date and period comparison
Advanced visualization types
Improved multi-step reasoning
Production database integration
Authentication
Role-based access control
More sophisticated query governance
Improved frontend experience
Automated anomaly detection
Automated business insight generation
Expanded test coverage
👨‍💻 Contributors

Developed collaboratively by the MetricMind project team.

⭐ Conclusion

MetricMind demonstrates how traditional Business Intelligence can be extended with natural-language interaction and governed business metrics.

The project combines:

Data Analysis
      +
Business Metrics
      +
Semantic Layer
      +
APIs
      +
Natural Language
      +
Business Explanations
      +
Visualization
      +
Transparency
      +
Governance
      +
Testing