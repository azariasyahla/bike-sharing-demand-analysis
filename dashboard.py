from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Bike Sharing Demand", page_icon="🚲", layout="wide")
@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).resolve().parents[1] / "Bike-sharing-dataset" / "hour.csv", parse_dates=["dteday"])
df = load_data()
st.title("Bike Sharing Demand")
st.caption("Weather, holidays, and the rhythm of hourly rentals · Azaria Syahla Fitan Adibah")
st.sidebar.header("Explore the data")
years = st.sidebar.multiselect("Year", sorted(df.dteday.dt.year.unique()), default=sorted(df.dteday.dt.year.unique()))
sample = st.sidebar.radio("Analysis sample", ["Full sample", "Original IQR filter"])
if sample == "Original IQR filter":
    q1, q3 = df.cnt.quantile([.25, .75])
    df = df.loc[df.cnt.between(q1-1.5*(q3-q1), q3+1.5*(q3-q1))]
data = df.loc[df.dteday.dt.year.isin(years)]
if data.empty:
    st.info("Select at least one year to explore the data.")
    st.stop()
a,b,c = st.columns(3)
a.metric("Recorded hours", f"{len(data):,}")
b.metric("Total rentals", f"{data.cnt.sum():,}")
c.metric("Mean rentals / hour", f"{data.cnt.mean():.1f}")
st.caption("All figures reflect the selected years and analysis sample. IQR bounds are calculated on the full source dataset.")
left,right = st.columns(2)
for area, column, title, labels in [
    (left,"holiday","Rentals by holiday status",{0:"Non-holiday",1:"Holiday"}),
    (right,"weathersit","Rentals by weather",{1:"Clear / partly cloudy",2:"Mist / cloudy",3:"Light rain / snow",4:"Severe weather"})]:
    with area:
        st.subheader(title)
        summary = data.groupby(column).cnt.agg(["count","mean","median"])
        summary.index = summary.index.map(labels)
        fig,ax = plt.subplots(figsize=(7,4))
        summary["mean"].plot.bar(ax=ax,color="#ad6284",rot=20)
        ax.set(xlabel="",ylabel="Mean rentals per recorded hour")
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
        st.dataframe(summary.round(2),use_container_width=True)
st.info("Non-holidays include weekends. Group averages describe associations, not causal effects or statistical significance. Severe-weather observations are sparse.")
st.subheader("Hourly demand profile")
st.line_chart(data.groupby("hr").cnt.mean(),x_label="Hour",y_label="Mean rentals")
with st.expander("Explore the source records"):
    st.dataframe(data,use_container_width=True)
st.caption("Source: Bike Sharing Dataset · Fanaee-T & Gama · Capital Bikeshare, 2011–2012 · DOI: 10.1007/s13748-013-0040-3")
