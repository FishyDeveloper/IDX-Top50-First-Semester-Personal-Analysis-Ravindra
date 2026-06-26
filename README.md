# IDX-Top50-First-Semester-Personal-Analysis-Ravindra

![Python 3.13](https://img.shields.io/badge/Python-3.13-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202026-lightgrey?style=flat-square)

A comprehensive data analysis project examining the top 50 companies listed on Indonesia's stock exchange (IHSG) during the first semester of 2026. This project leverages Python for data processing and Excel for advanced analysis, combining quantitative insights with visual representations of market dynamics.

> ### ⚠️ Disclaimer
> This project was assisted by Gemini AI and this analysis is for **Informational Purposes Only**. I am not a financial advisor. Do your own research (DYOR) before making any investment decisions. All data and analysis are provided as educational material without guarantee of accuracy.

---

## 📑 Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Data Dictionary](#data-dictionary)
- [Analysis](#analysis)
  - [Macro Sector Dynamics](#macro-sector-dynamics)
  - [The Micro Leaderboard Drift](#the-micro-leaderboard-drift)
  - [Systemic Decentralization Metric](#systemic-decentralization-metric)
- [Data Methodology](#data-methodology)
- [Technical Setup](#technical-setup)
- [Project Structure](#project-structure)
- [Personal Take](#personal-take)

---

## Executive Summary

This analysis tracks market concentration and sector dynamics within Indonesia's top 50 listed companies (IHSG) from January to June 2026. Key findings reveal:

- 📈 **Financial sector dominance** continues to strengthen, growing from 24.3% to 26.8% index weight
- 📉 **Energy and Basic Materials** sectors face structural contraction, losing significant market position
- 🏦 **Banking heavyweights** ($BBCA, $BBRI) demonstrate resilience amid market volatility
- 💧 **Market decentralization** accelerates, with top 50 concentration declining from 71.87% to 67.29%
- 🔄 **Capital rotation** evident between mega-caps and broader market tiers

---

## Key Findings

| Finding | Impact | Implication |
|---------|--------|-------------|
| Financials grow from 24.3% → 26.8% | +2.5% concentration gain | Sector dominance solidifies, higher systemic risk if sentiment shifts |
| $BREN declines from 7.5% → 5.8% | -1.7% weight loss | Profit-taking and portfolio rebalancing by institutions |
| $BBCA & $BBRI maintain stability | Resilient performance | Defensive positioning favored; banks remain investor safe-haven |
| Top 50 concentration: 71.87% → 67.29% | -4.58% dilution | Healthy market breadth; capital flowing to mid/small-caps |
| Healthcare & Real Estate growth | Steady accretion | Emerging opportunities in defensive/real asset sectors |

---

## Data Dictionary

**Key Terms & Definitions:**

| Term | Definition |
|------|-----------|
| **IHSG** | Indonesia Composite Index - main stock market index on Indonesia Stock Exchange |
| **Top 50** | The 50 largest companies by market capitalization listed on IDX |
| **Concentration %** | Percentage of total market cap held by a stock or sector within the top 50 |
| **Market Share Decay** | The declining share of total market value held by mega-cap stocks |
| **Systemic Decentralization** | Capital redistribution away from concentrated holdings toward broader market participation |
| **Sector Dynamics** | Month-to-month shifts in sector-level market share and relative positioning |

---

## Analysis

### Macro Sector Dynamics
*Dynamic market share distribution tracking sector dominance shifting month-by-month.*

![Macro Sector Concentration](Visuals/sector_concentration.png)

#### 📊 Sector Performance Overview

**Gainers:**
- **Financials**: 24.3% (Jan) → 26.8% (Jun) | +2.5pp | ✅ Strengthening dominance
- **Healthcare**: 1.82% (Jan) → 2.36% (Jun) | +0.54pp | ✅ Steady growth trajectory
- **Real Estate**: 2.15% (Jan) → 2.58% (Jun) | +0.43pp | ✅ Structural accretion

**Stable:**
- **Technology**: 6.5% average | ±0.3pp | ➡️ Consistent defensive positioning

**Losers:**
- **Basic Materials**: 17.34% (Jan) → 15.2% (Jun) | -2.14pp | ❌ Pronounced contraction
- **Energy**: (similar significant decline) | ❌ Structural headwinds

#### 💡 Key Insights

The financial sector maintains the highest relative concentration within IHSG, exhibiting a strong upward trend throughout the semester. This growth reflects increased institutional capital allocation toward banking and financial services, driven by economic stability expectations.

A similar structural resilience is exhibited by the Technology sector. Despite maintaining a modest baseline footprint with 6.5% on average of the top 50 index weight, the sector consistently defended its market position with minimal volatility across the five-month window.

The lower-weight spectrum reveals a trajectory of steady structural accretion in both Healthcare and Real Estate. Healthcare successfully scaled its index footprint from 1.82% to 2.36% over the five-month period, while Real Estate grew from 2.15% to 2.58%, suggesting investor appetite for defensive and hard-asset plays.

Conversely, the Energy and Basic Materials sectors experienced a pronounced structural contraction within the top 50 hierarchy across the first semester. Basic Materials compressed from a 17.34% concentration in January to approximately 15.2% by June, reflecting significant capital rotation away from commodity-exposed equities.

---

### The Micro Leaderboard Drift
*Tracking the top index titans as capital flows between speculative infrastructure and defensive banking.*

![Top 5 Corporate Drivers](Visuals/top5_drivers.png)

#### 🏆 Top 5 Stocks Performance Summary

| Stock | Company | Jan Weight | Jun Weight | Change | Trend | Status |
|-------|---------|-----------|-----------|--------|-------|--------|
| $BREN | PT Barito Renewables Energy | 7.5% | 5.8% | -1.7pp | 📉 Declining | Profit-taking |
| $DSSA | Dian Swastatika Sentosa Tbk | 5.08% | 3.2% | -1.88pp | 📉 Contracting | Institutional outflows |
| $BBCA | Bank Central Asia Tbk | 4.2% | 4.5% | +0.3pp | 📈 Stable+ | Resilient |
| $BBRI | Bank Rakyat Indonesia | 3.8% | 4.1% | +0.3pp | 📈 Stable+ | Defensive favorite |
| $DCII | PT Dua Citra Investama | 3.17% | 3.8% | +0.63pp | 📈 Growing | Steady momentum |

#### 💡 Key Insights

**Volatile Movers ($BREN, $DSSA):**
The micro layer reveals that $BREN (PT Barito Renewables Energy) held the dominant position early in the semester, maintaining a peak concentration of around 7.5% across January and February. This dominance gradually eroded as the semester progressed, settling at approximately 5.8% by June—a clear signal of profit-taking and portfolio rebalancing.

Another component experiencing a severe structural contraction is $DSSA (Dian Swastatika Sentosa Tbk). While $DSSA maintained an initial relative concentration of 5.08% in January before adjusting downward to approximately 3.2% by mid-semester, suggesting significant institutional outflows and reduced investor confidence.

**Defensive Anchors ($BBCA, $BBRI):**
In stark contrast to the volatile contractions of $BREN and $DSSA, the banking heavyweights $BBCA (Bank Central Asia Tbk.) and $BBRI (Bank Rakyat Indonesia (Persero) Tbk.) exhibited highly resilient performance. Both maintained steady to slightly increasing weight throughout the semester—reflecting defensive positioning by institutional investors and retail confidence in financial system stability.

**Growth Play ($DCII):**
In contrast, $DCII maintained a slowly growing concentration throughout the semester. In January, they held a 3.17% weight, followed by a stable phase from February until April where they averaged around 3.4%, before accelerating to 3.8% by June. This trajectory suggests improving business fundamentals or positive market sentiment.

---

### Systemic Decentralization Metric
*The steady downward velocity proving money is migrating out of the mega-caps into broader market tiers.*

![Index Market Share Decay](Visuals/concentration_decay.png)

#### 📊 Concentration Trend Analysis

| Month | Top 50 Weight | Month-over-Month Change | Cumulative Decay |
|-------|---------------|------------------------|------------------|
| January | 71.87% | — | — |
| February | 71.52% | -0.35pp | -0.35pp |
| March | 70.14% | -1.38pp | -1.73pp |
| April | 68.95% | -1.19pp | -2.92pp |
| May | 67.58% | -1.37pp | -4.29pp |
| June | 67.29% | -0.29pp | -4.58pp |

#### 💡 Key Insights

The aggregate metric uncovers a steady dilution of concentration within the index, as the combined weight of the top 50 equities decelerated smoothly from 71.87% in January to 67.29% by the end of June. This systematic decentralization of -4.58 percentage points suggests capital flows are rotating from mega-cap stocks toward mid-cap and smaller-cap constituents.

**What this means:**
- ✅ **Healthier market breadth** - More companies contributing to index performance
- ✅ **Reduced systemic risk** - Less concentration risk from mega-cap volatility
- ✅ **Emerging opportunities** - Smaller companies gaining investor interest and liquidity
- ⚠️ **Market maturation** - Sign of a maturing market with improved participant diversification

This decentralization indicates improved market breadth and suggests investor confidence in the broader economy beyond the mega-cap tier.

---

## Data Methodology

### Data Sources
- **Primary Source**: [IDX Official Statistical Reports](https://idx.co.id/en/market-data/statistical-reports/digital-statistic/monthly/) - Monthly market capitalization data
- **Secondary Source**: [Wikipedia - Listed Companies on IDX](https://id.wikipedia.org/wiki/Daftar_perusahaan_yang_tercatat_di_Bursa_Efek_Indonesia) - Sector classification (2024 baseline)

### Calculation Methods
- **Sector Concentration**: Sum of all company weights within each sector / total top 50 weight
- **Stock Weight**: Individual company market cap / total top 50 market cap
- **Monthly Changes**: Current month value - previous month value (percentage points)
- **Cumulative Decay**: Compounded month-over-month changes in top 50 concentration

### Data Limitations & Assumptions
- Wikipedia sector data is from 2024; some classifications may have shifted in 2026
- Analysis focuses on top 50 companies; doesn't represent full market dynamics
- Monthly snapshots taken at period-end; intra-month volatility not captured
- External events (political, economic) may impact results beyond data scope

### Quality Assurance
- Data cross-referenced with official IDX reports
- Python scripts validate data integrity during processing
- Excel pivot tables manually verified for accuracy
- Visualizations spot-checked against raw data

---

## Technical Setup

### Prerequisites
- **Python 3.13** or compatible version
- **Required Libraries:**
  - `pandas` - Data manipulation and analysis
  - `openpyxl` - Excel file handling
  - `pathlib` - File path operations
  - `csv` - CSV data processing

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/FishyDeveloper/IDX-Top50-First-Semester-Personal-Analysis-Ravindra.git
   cd IDX-Top50-First-Semester-Personal-Analysis-Ravindra
   ```

2. **Install Dependencies**
   ```bash
   pip install pandas openpyxl
   ```

3. **Data Preparation**
   - Download market capitalization data from [IDX Official Statistical Reports](https://idx.co.id/en/market-data/statistical-reports/digital-statistic/monthly/biggest-market-capitalization-most-active-stocks/biggest-market-capitalization)
   - Reference company sector data: [Wikipedia - Listed Companies on IDX](https://id.wikipedia.org/wiki/Daftar_perusahaan_yang_tercatat_di_Bursa_Efek_Indonesia) *(2024 data - may require additional research)*
   - Place raw data files in the `Raw Files/` directory

### Execution Workflow

Follow these steps **in sequential order**:

1. **Run Rename Script**
   ```bash
   python "Python Files/rename_script.py"
   ```
   Standardizes and renames raw data files for consistent processing.

2. **Extract Master Asset to CSV**
   ```bash
   python "Python Files/master_asset_to_csv.py"
   ```
   Converts master asset data into CSV format for analysis.

3. **Merge Monthly Lists**
   ```bash
   python "Python Files/merged_list.py"
   ```
   Consolidates all monthly data (January-June) into a single unified dataset.

4. **Generate Analysis & Visualizations**
   - Excel pivot tables and analysis files are generated in the `Processed/` folder
   - Final visualizations and charts are saved to the `Visuals/` folder

### IDE & Configuration
- Recommended: **PyCharm** (automatically manages Python path configuration)
- No external configuration files required; standard Python environment setup is sufficient

---

## Project Structure

```
IDX-Top50-First-Semester-Personal-Analysis-Ravindra/
├── Raw Files/              # Source data from IDX and Wikipedia
├── Python Files/           # Python scripts for data processing
│   ├── rename_script.py           # Standardizes raw file naming
│   ├── master_asset_to_csv.py     # Extracts & converts master data
│   └── merged_list.py             # Consolidates monthly datasets
├── Processed/              # Excel files with analysis and pivot tables
│   └── [Generated analysis files]
├── Visuals/                # Final charts, graphs, and pivot table exports
│   ├── sector_concentration.png
│   ├── top5_drivers.png
│   └── concentration_decay.png
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules

```

---

## Personal Take
*[To be completed by project author]*

---

**Last Updated:** June 2026 | **Contact:** [Your GitHub Profile](https://github.com/FishyDeveloper)
