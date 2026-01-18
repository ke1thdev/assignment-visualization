"""
Data Visualization App: AI Growth vs Data Center Energy Consumption
A Streamlit app analyzing the relationship between AI compute growth 
and global data center electricity consumption from 2022 to 2026.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PAGE CONFIGURATION & NEUBRUTALISM STYLING
# =============================================================================
st.set_page_config(
    page_title="AI & Energy Visualization",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS for Neubrutalism design
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #FFFEF0;
    }
    
    /* Neubrutalism card styling */
    .neu-card {
        background-color: #FFFFFF;
        border: 3px solid #1a1a1a;
        border-radius: 0px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 6px 6px 0px #1a1a1a;
        color: #1a1a1a !important;
    }
    
    .neu-card p {
        color: #1a1a1a !important;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }
    
    .neu-card strong {
        color: #1a1a1a !important;
    }
    
    /* Title styling */
    .neu-title {
        font-family: 'Arial Black', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: #1a1a1a;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 1rem;
        background-color: #FFE156;
        border: 3px solid #1a1a1a;
        box-shadow: 6px 6px 0px #1a1a1a;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Subtitle styling */
    .neu-subtitle {
        font-family: 'Arial Black', sans-serif;
        font-size: 1.3rem;
        font-weight: 800;
        color: #1a1a1a;
        background-color: #A8E6CF;
        border: 3px solid #1a1a1a;
        padding: 0.8rem 1.2rem;
        box-shadow: 4px 4px 0px #1a1a1a;
        margin: 1rem 0;
        display: inline-block;
    }
    
    /* Dataframe container */
    .dataframe-container {
        border: 3px solid #1a1a1a;
        box-shadow: 6px 6px 0px #1a1a1a;
        padding: 0;
        background-color: #FFFFFF;
    }
    
    /* Note styling */
    .neu-note {
        background-color: #FFB6C1;
        border: 2px solid #1a1a1a;
        padding: 0.8rem;
        box-shadow: 4px 4px 0px #1a1a1a;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    /* Chart container */
    .chart-container {
        background-color: #FFFFFF;
        border: 3px solid #1a1a1a;
        box-shadow: 8px 8px 0px #1a1a1a;
        padding: 1rem;
        margin: 1.5rem 0;
    }
    
    /* Hide default Streamlit header */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# MAIN TITLE
# =============================================================================
st.markdown('<div class="neu-title">⚡ AI Growth & Data Center Energy Analysis</div>', unsafe_allow_html=True)

# =============================================================================
# LOAD DATA
# =============================================================================
# Load the dataset from the CSV file
df = pd.read_csv('data.csv')

# =============================================================================
# DISPLAY RAW DATA TABLE
# =============================================================================
st.markdown('<div class="neu-subtitle">📊 Raw Data Table</div>', unsafe_allow_html=True)

# Display the raw data using st.dataframe()
st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
st.dataframe(df, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create two columns for the visualizations
col1, col2 = st.columns(2)

# =============================================================================
# VISUALIZATION 1: LINE CHART - Energy Consumption Trend
# =============================================================================
with col1:
    st.markdown('<div class="neu-subtitle">📈 Energy Consumption Trend</div>', unsafe_allow_html=True)
    
    # Note: 2025-2026 values are projections based on industry forecasts
    st.markdown('<div class="neu-note">📌 Note: 2025–2026 values are projections</div>', unsafe_allow_html=True)
    
    # Create a new figure for the line chart
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    # Extract data for plotting
    years = df['year']
    electricity = df['DataCenter_Electricity_Twh']
    
    # Plot line chart with markers
    ax1.plot(years, electricity, marker='o', linewidth=2.5, markersize=10)
    
    # Set title and labels
    ax1.set_title('Global Data Center Electricity Consumption (2022–2026)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Electricity Consumption (TWh)', fontsize=12, fontweight='bold')
    
    # Enable grid lines for readability
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Set proper x-axis ticks to show all years
    ax1.set_xticks(years)
    
    # Adjust layout for better spacing
    plt.tight_layout()
    
    # Display the figure in Streamlit
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show the plot (as required by task)
    plt.show()

# =============================================================================
# VISUALIZATION 2: BAR CHART - AI Compute Growth
# =============================================================================
with col2:
    st.markdown('<div class="neu-subtitle">📊 AI Compute Growth</div>', unsafe_allow_html=True)
    
    # Note: Log scale is used because AI compute growth is exponential
    # The AI Compute Index grows 5x each year (1 → 5 → 25 → 125 → 625)
    st.markdown('<div class="neu-note">📌 Log scale used due to exponential AI growth</div>', unsafe_allow_html=True)
    
    # Create a new figure for the bar chart
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    # Extract data for plotting
    years = df['year']
    ai_compute = df['Ai_Compute_Index']
    
    # Plot bar chart
    ax2.bar(years, ai_compute, width=0.6, edgecolor='black', linewidth=1.5)
    
    # Set title and labels
    ax2.set_title('Relative AI Training Compute Growth (Index, 2022 = 1)', 
                  fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('AI Compute Index', fontsize=12, fontweight='bold')
    
    # Apply logarithmic scale to y-axis (required for exponential growth visualization)
    ax2.set_yscale('log')
    
    # Enable grid lines for both major and minor ticks
    ax2.grid(True, which='major', linestyle='-', alpha=0.7)
    ax2.grid(True, which='minor', linestyle=':', alpha=0.4)
    
    # Set proper x-axis ticks to show all years
    ax2.set_xticks(years)
    
    # Adjust layout for better spacing
    plt.tight_layout()
    
    # Display the figure in Streamlit
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show the plot (as required by task)
    plt.show()

# =============================================================================
# FOOTER - Analysis Summary
# =============================================================================
st.markdown("---")
st.markdown('<div class="neu-subtitle">💡 Key Insights</div>', unsafe_allow_html=True)
st.markdown("""
<div class="neu-card">
    <p><strong>1. Energy Consumption:</strong> Data center electricity usage is projected to grow from 331 TWh (2022) to 520.6 TWh (2026) — a ~57% increase.</p>
    <p><strong>2. AI Compute Growth:</strong> AI training compute is growing exponentially at 5× per year, reaching 625× the 2022 baseline by 2026.</p>
    <p><strong>3. Correlation:</strong> While AI compute grows exponentially, energy consumption grows more linearly, suggesting efficiency improvements are partially offsetting raw compute demands.</p>
</div>
""", unsafe_allow_html=True)
