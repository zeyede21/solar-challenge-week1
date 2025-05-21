import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("🌞 Solar Energy Data Explorer")

# Load datasets
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    sierra = pd.read_csv("data/sierraleone_clean.csv")
    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"
    return pd.concat([benin, togo, sierra], ignore_index=True)

df = load_data()

# Sidebar filters
countries = st.sidebar.multiselect("Select countries:", df["Country"].unique(), default=df["Country"].unique())
metric = st.sidebar.selectbox("Select metric to visualize:", ["GHI", "DNI", "DHI"])

# Filtered data
df_filtered = df[df["Country"].isin(countries)]

# Layout
col1, col2 = st.columns([2, 1])

# Boxplot
with col1:
    st.subheader(f"Distribution of {metric} by Country")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_filtered, x="Country", y=metric, palette="viridis", ax=ax)
    st.pyplot(fig)

# Summary Table
with col2:
    st.subheader(f"Summary Statistics for {metric}")
    summary = df_filtered.groupby("Country")[metric].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)

# Footer
st.markdown("---")
st.caption("Built for 10 Academy Week 1 Solar Data Challenge")
