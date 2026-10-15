# Bike Sharing Demand Analysis
### From weather patterns to practical rental insights

A reproducible exploratory analysis of hourly bike rentals, with a Streamlit dashboard for exploring weather conditions and holiday patterns.

**Author:** Azaria Syahla Fitan Adibah  
**Tools:** Python · pandas · Matplotlib · seaborn · Streamlit

## Project overview
How does bike rental demand vary with weather and holiday status? This project investigates historical Capital Bikeshare observations and compares the full dataset with the original IQR-filtered sample.

Originally created as a Dicoding final project, this portfolio revision adds portable file paths, reproducible outputs, sample-size reporting, and more precise statistical interpretation.

## Key findings
- Non-holiday hours average **190.43** rentals, compared with **156.87** on holidays.
- Clear or partly cloudy hours average **204.87** rentals; light rain or snow hours average **111.58**.
- Severe weather has only **3 recorded hours**, limiting interpretation.
- Removing high-demand hours changes the results; the notebook reports both samples.

These findings describe associations. They do not establish causation or statistical significance.

## Repository contents
- `bike_sharing_analysis.ipynb`: executed analysis, visualizations, and interpretation; works locally and supports Kaggle dataset discovery.
- `dashboard/dashboard.py`: interactive dashboard with year and sample filters.
- `Bike-sharing-dataset/`: original hourly and daily CSVs and supplied documentation. The analysis uses hourly data.
- `requirements.txt`: supported dependency ranges, not a locked environment.

## Run locally
Use Python 3.11 or newer. From the repository root:

```bash
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```bash
source .venv/bin/activate
```

Then install dependencies and start the dashboard:

```bash
python -m pip install -r requirements.txt
python -m streamlit run dashboard/dashboard.py
```

To run the notebook locally, install Jupyter separately (`python -m pip install notebook`) and open it from the repository root.

## Kaggle
1. Create or attach a dataset containing the supplied `hour.csv` (and optionally `day.csv`). Retain the dataset attribution.
2. Import `bike_sharing_analysis.ipynb` into a Kaggle notebook.
3. Attach the dataset and run all cells. The loader discovers `hour.csv` under `/kaggle/input`; if multiple matches exist, select the intended path explicitly.
4. Review the results and publish the notebook when ready.

The Streamlit dashboard is intended to run separately from the Kaggle notebook.

## Method and limitations
Data quality checks → descriptive statistics → grouped comparisons → visualizations → correlation summaries → IQR sensitivity analysis.

Valid demand peaks are retained in the primary analysis. The analysis is unadjusted for season, hour, and year; weather categories have unequal sample sizes. No formal significance tests or forecasting models are included. Non-holiday is not synonymous with working day.

## Data attribution
Dataset: **Bike Sharing Dataset**, Hadi Fanaee-T and Joao Gama. Capital Bikeshare, Washington, D.C., 2011–2012.

Fanaee-T, H. & Gama, J. (2013). *Event labeling combining ensemble detectors and background knowledge*. DOI: **10.1007/s13748-013-0040-3**.

See `Bike-sharing-dataset/Readme.txt` for the original source documentation and citation requirement. No new license is asserted for the supplied dataset.
