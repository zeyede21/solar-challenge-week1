🌞 Solar Potential Assessment – West Africa (Benin, Togo, Sierra Leone)

This project analyzes solar irradiance data from Benin, Togo, and Sierra Leone to assess solar energy potential across regions. The project includes data profiling, cleaning, exploratory data analysis (EDA), cross-country comparison, and an interactive Streamlit dashboard.

🔍 Key Features
EDA Notebooks
Individual notebooks for Benin, Togo, and Sierra Leone.

Includes profiling, missing value checks, outlier detection, time series analysis, wind & temperature insights, and sensor data trends.

Cross-Country Comparison

Statistical summary (mean, median, std) of GHI, DNI, and DHI.

Boxplots and bar charts for comparison.

One-way ANOVA test on GHI values.

Streamlit Dashboard

Interactive UI to compare countries.

Dynamic visualizations of solar potential metrics.

Country selection, metric filtering, and KPI display.

🚀 Deployment
This app is deployable to Streamlit Community Cloud.

Steps:

Fork this repo and clone locally.

Ensure the cleaned .csv files are stored in data/ folder.

Install dependencies:

pip install -r requirements.txt

Launch locally:

streamlit run app/main.py

Deploy to Streamlit Cloud and point to app/main.py.

Dependencies
streamlit

pandas

seaborn

matplotlib

✅ Tasks Completed
✔ Data profiling, cleaning, EDA for each country

✔ Comparative analysis with statistics and visualizations

✔ Interactive Streamlit dashboard

✔ Git hygiene and structured codebase

🧠 Insights & Outcomes
Benin and Sierra Leone show strong GHI potential, with Togo slightly lower on average.

Variability exists both within and between countries.

Interactive dashboard enables easy stakeholder exploration.
