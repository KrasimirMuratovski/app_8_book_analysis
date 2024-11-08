import streamlit as st
# import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import glob
import plotly.express as px


filepaths = glob.glob("diary/*.txt")

analyzer = SentimentIntensityAnalyzer() ## instantiating the class

positivity = []
negativity = []
# directory = "diary"
for filepath in filepaths:
     with open(filepath, 'r') as f:
         content = f.read()
         scores = analyzer.polarity_scores(content)
         positivity.append(scores['pos'])
         negativity.append(scores['neg'])

dates = [filepath.strip(".txt").strip("diary\\") for filepath in filepaths]
print(dates)
print(positivity)
print(negativity)

st.title("Diary tone")
## TODO
pos_figure = px.line(x = dates, y = positivity, labels = {"x": "Date", "y":"Positivity"})
st.header("Positivity")
st.plotly_chart(pos_figure)

neg_figure = px.line(x = dates, y = negativity, labels = {"x": "Date", "y":"Negativity"})
st.header("Negativity")
st.plotly_chart(neg_figure)

