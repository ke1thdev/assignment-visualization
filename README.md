# ⚡ AI Growth & Data Center Energy Visualization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://assignment-visualization.streamlit.app/)

A Streamlit web application that visualizes and analyzes the relationship between **AI compute growth** and **global data center electricity consumption** from 2022 to 2026.

## 🚀 Live Demo

**[View Live App →](https://assignment-visualization.streamlit.app/)**

---

## 📊 Overview

This application provides interactive data visualization to explore two critical trends in the tech industry:

1. **Energy Consumption Trend** — How global data center electricity usage is increasing
2. **AI Compute Growth** — The exponential growth of AI training compute power

### Key Insights

| Metric | 2022 | 2026 | Change |
|--------|------|------|--------|
| Data Center Electricity | 331 TWh | 520.6 TWh | +57% |
| AI Compute Index | 1 | 625 | +62,400% |

> 💡 While AI compute grows exponentially (5× per year), energy consumption grows more linearly, suggesting efficiency improvements are partially offsetting raw compute demands.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Matplotlib** | Data visualization |

---

## 📈 Visualizations

### 1. Line Chart — Energy Consumption Trend
- Shows global data center electricity consumption from 2022–2026
- Includes markers for each data point
- Grid lines for better readability
- *Note: 2025–2026 values are projections*

### 2. Bar Chart — AI Compute Growth
- Displays relative AI training compute growth (Index, 2022 = 1)
- Uses **logarithmic scale** to properly visualize exponential growth
- Grid lines on major and minor ticks

---

## 🎨 Design

The application features a **Neubrutalism** design aesthetic with:
- Bold borders and heavy drop shadows
- High-contrast color palette
- Clean, modern typography
- Vibrant accent colors (yellow, mint green, pink)

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── data.csv            # Dataset with yearly metrics
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/assignment-visualization.git
   cd assignment-visualization
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   ```
   http://localhost:8501
   ```

---

## 📊 Dataset

The `data.csv` file contains the following columns:

| Column | Description |
|--------|-------------|
| `year` | Year (2022–2026) |
| `DataCenter_Electricity_Twh` | Global data center electricity consumption in TWh |
| `Ai_Compute_Index` | Relative AI compute index (2022 = 1) |

### Data Preview

| Year | Electricity (TWh) | AI Compute Index |
|------|-------------------|------------------|
| 2022 | 331 | 1 |
| 2023 | 370.7 | 5 |
| 2024 | 415 | 25 |
| 2025 | 464.8 | 125 |
| 2026 | 520.6 | 625 |

---

## 📚 Data Sources & References

The data presented in this visualization is based on credible research sources:

### Data Center Electricity Consumption
- Data center electricity consumption values are based on the **International Energy Agency (IEA)** Energy and AI report
- The reported 2024 value (415 TWh) and an approximate 12% annual growth rate were used to estimate values for 2022–2023 and project values for 2025–2026

### AI Compute Growth
- AI training compute growth is represented using a relative index (2022=1), based on analyses from the **Stanford AI Index** and related studies reporting rapid exponential growth in AI training compute

### References

1. **International Energy Agency.** (2024). *Energy and AI: Energy demand from AI.*  
   https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai

2. **International Energy Agency.** (2024). *Electricity 2024: Analysis and forecast to 2026.*  
   https://www.iea.org/reports/electricity-2024

3. **Stanford University Human-Centered Artificial Intelligence Institute.** (2024). *AI Index Report 2024.*  
   https://hai.stanford.edu/ai-index/2025-ai-index-report

4. **Epoch AI.** (2023). *Key Trends and Figures in Machine Learning.*  
   https://epoch.ai/trends

5. **Microsoft Corporation.** (2023). *Advancing sustainability in data centers.*  
   https://datacenters.microsoft.com/sustainability

> ⚠️ **Note:** 2025–2026 values are projections based on historical growth rates and industry forecasts.

## 🚀 Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `app.py` as the main file
5. Click **Deploy**

---

## 📝 Assignment Requirements

This project fulfills the following requirements:

- ✅ Load dataset using `pandas.read_csv()`
- ✅ Display raw data table using `st.dataframe()`
- ✅ Create two separate figures (no subplots)
- ✅ Clear and descriptive titles
- ✅ Proper x-axis and y-axis labels
- ✅ Proper scaling (including log scale for exponential data)
- ✅ Grid lines for readability
- ✅ Clean, commented, submission-ready code

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Made with ❤️ for a university data visualization assignment.

---

<p align="center">
  <a href="https://assignment-visualization.streamlit.app/">
    <img src="https://img.shields.io/badge/View_Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="View Live Demo">
  </a>
</p>
