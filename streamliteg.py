import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
st.balloons()
#st.set_option('deprecation.showPyplotGlobalUse',False)
st.title("Tips_Dataset")
df=pd.read_csv('analytics.csv')
tips=df.head(30)
st.table(tips)
st.header("visualisation using seaborn")
st.subheader("BarPlot")
tips.plot(kind='bar')
st.pyplot()
#joinplot
st.subheader("joinplot")
sns.jointplot(x='Page Title',y='Pageviews',data=tips,kind='scatter')
st.pyplot()
#pairplot
st.subheader("pairplot")
sns.pairplot(tips,hue='Bounces',palette='rainbow')
st.pyplot()
#correation
st.subheader("heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()

