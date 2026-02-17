**Trader Behavior & Market Sentiment Analysis**


**Project Overview**

This project analyzes how market sentiment (measured by the Fear & Greed Index) impacts trader behavior and profitability on the Hyperliquid exchange.

By merging historical trade data with daily sentiment classifications, this analysis uncovers behavioral patterns—specifically regarding risk management and directional bias—to formulate actionable trading strategies.

**Setup & Usage**

1. Prerequisites

Python 3.8+

pip package manager

2. Installation

# Clone the repository
git clone [https://github.com/yourusername/primetrade-assignment.git](https://github.com/yourusername/primetrade-assignment.git)
cd primetrade-assignment

# Install dependencies
pip install -r requirements.txt



3. Running the Analysis

Jupyter Notebook: Open analysis_notebook.ipynb to view the full data cleaning, EDA, and Machine Learning workflow.

Interactive Dashboard: Run the Streamlit app to explore trader segments:

streamlit run app.py



**Methodology**

Data Alignment: Converted Hyperliquid Timestamp IST to daily-level UTC dates to enable a Many-to-One left join with the Fear & Greed Index.

Feature Engineering: Aggregated trade-level data into Daily Trader Metrics:

Win Rate: (Winning Trades / Total Closed Trades)

Risk Proxy: Used Size USD (Average & Max) to approximate leverage usage.

Directional Bias: Calculated Long/Short ratios per day.

Segmentation: Grouped traders using K-Means Clustering (k=3) based on frequency and volume to identify distinct behavioral archetypes.

**Key Insights & Evidence**

1. The "Panic-Buying" Paradox

Insight: Contrary to the expectation of "de-risking" during uncertainty, traders actually increase their average position size by ~40% during "Fear" days compared to "Greed" days.

Evidence: Average trade size jumps from $6,000 (Greed) to $8,500 (Fear).

Interpretation: This suggests a strong psychological bias to "average down" on losing positions or aggressively "buy the dip," often leading to larger drawdowns.

2. Profitability Divergence by Frequency

Insight: High-frequency traders (Intraday/Scalpers) thrive in Fear regimes, while Low-frequency (Swing) traders underperform.

Evidence: Segmenting by frequency reveals that Day Traders generated ~32% higher Net PnL on Fear days compared to Greed days, whereas Swing Traders saw their PnL flatten or turn negative.

Interpretation: Volatility in Fear markets offers more arbitrage/scalping opportunities, whereas directional swing trades suffer from rapid reversals.

3. Retail Long Bias

Insight: The retail crowd exhibits a dangerous directional skew during market bottoms.

Evidence: The Long/Short ratio spikes to nearly 2.0 (2 Longs for every 1 Short) during "Extreme Fear," compared to a balanced 1.5 during "Greed."

Interpretation: Retail traders overwhelmingly bet on reversals rather than riding the trend, making them highly susceptible to long-squeeze cascades.

**Strategy Recommendations ("Actionable Output")**

Strategy A: The "Volatility Regime" Filter

Logic: Since high-frequency strategies outperform during Fear, but swing strategies bleed:

Rule: "If Sentiment == 'Fear' AND Daily_Volatility > Threshold: Disable all swing-trading entry signals and Double capital allocation for mean-reversion scalping bots."

Strategy B: Contrarian Liquidation Hunting

Logic: Retail traders are over-leveraged and over-long during Fear (Insight 2 & 3).

Rule: "If Sentiment == 'Extreme Fear' AND Long/Short Ratio > 1.8: Enter Short positions targeting the liquidation wicks of these over-extended long positions. Do not go Long until the L/S ratio resets below 1.2."

**Machine Learning Models**

1. Predictive Modeling (Random Forest)

Goal: Predict if a trader will be profitable tomorrow based on today's behavior.

Result: Achieved 62% Accuracy (Precision: 68% for profitable class).

Top Feature: Total_Trades (Frequency) was the strongest predictor of future success.

2. Behavioral Clustering (K-Means)

Identified 3 distinct trader archetypes:

Cluster 0 (Retail Scalpers): High frequency, low volume.

Cluster 1 (Whale Swingers): Low frequency, massive volume ($100k+ avg size).

Cluster 2 (Directional Algos): Extreme Long/Short bias.

**File Structure**

analysis_notebook.ipynb: Complete code for Data Prep, Part B Analysis, and ML models.

app.py: Source code for the Streamlit dashboard.

requirements.txt: Python dependencies.

data/: Folder containing the raw CSVs (not included in repo for privacy).