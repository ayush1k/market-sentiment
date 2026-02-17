import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page layout
st.set_page_config(page_title="Trader Insights Dashboard", layout="wide")
st.title("📈 Hyperliquid Trader Behavior & Segmentation")

# 1. Load Data with Caching
@st.cache_data
def load_data():
    daily_stats = pd.read_csv("daily_trader_stats.csv")
    profiles = pd.read_csv("trader_profiles.csv")
    return daily_stats, profiles

daily_stats, profiles = load_data()

# 2. Sidebar Filters
st.sidebar.header("Dashboard Controls")
sentiment_filter = st.sidebar.selectbox(
    "Filter by Market Sentiment:", 
    ["All", "Extreme Greed", "Greed", "Neutral", "Fear", "Extreme Fear"]
)

if sentiment_filter != "All":
    daily_stats = daily_stats[daily_stats['sentiment_class'] == sentiment_filter]

# 3. Top Level Metrics
st.markdown("### 🔍 High-Level Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Total Traders Analyzed", profiles['Account'].nunique())
col2.metric("Average Win Rate", f"{daily_stats['win_rate'].mean():.2f}%")
col3.metric("Average Trade Size", f"${daily_stats['avg_trade_size_usd'].mean():,.2f}")

st.divider()

# 4. Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Profitability by Behavioral Cluster")
    # Show the K-Means results
    fig_cluster, ax_cluster = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=profiles, 
        x='Cluster', 
        y='net_pnl', 
        palette='Set2', 
        errorbar=None, 
        ax=ax_cluster
    )
    ax_cluster.set_ylabel("Average Net PnL (USD)")
    ax_cluster.set_xlabel("K-Means Archetype Cluster")
    st.pyplot(fig_cluster)
    st.caption("Cluster 0: Retail Scalpers | Cluster 1: High-Conviction Swings | Cluster 2: Directional Algos")

with col_right:
    st.markdown("#### Trade Sizing vs. Sentiment")
    # Show the behavior shift based on Fear/Greed
    fig_sent, ax_sent = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=daily_stats, 
        x='sentiment_class', 
        y='avg_trade_size_usd', 
        palette='magma', 
        errorbar=None,
        ax=ax_sent
    )
    ax_sent.set_ylabel("Average Trade Size (USD)")
    ax_sent.set_xlabel("Market Sentiment")
    plt.xticks(rotation=45)
    st.pyplot(fig_sent)

# 5. Raw Data Explorer
st.divider()
st.markdown("### 🗄️ Raw Data Explorer")
st.dataframe(profiles[['Account', 'Cluster', 'total_trades', 'avg_trade_size_usd', 'net_pnl', 'win_rate']].head(50))