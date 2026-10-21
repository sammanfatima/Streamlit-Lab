import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# add title
st.title('Data Analysis Application')
st.subheader('This is a simple data analysis application created by Samman')

# create a dropdown list to choose a dataset
dataset_options = ['tips', 'titanic', 'iris', 'diamonds']

# load the data
#df = sns.load_dataset('tips')
selected_dataset = st.selectbox('select a dataset', dataset_options)

# load the selected dataset
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':  
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df = sns.load_dataset('tips')
elif selected_dataset == 'diamonds':    
    df = sns.load_dataset('diamonds')

# button to upload custom dataset
uploaded_file = st.file_uploader("Choose a custom dataset", type=['csv', 'xlsx'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# display the dataset
st.write(df.head())    

# display the number of rows and columns from the selected data
st.write('Number of rows:', df.shape[0])
st.write('Number of columns:', df.shape[1])

# display the column of selected data with thir datatype
st.write('Column names and data types:', df.dtypes)                                     

# print the null values if those are > 0
if df.isnull().sum().sum() > 0:
    st.write('Null values:', df.isnull().sum())
else:
    st.write('No null')    

# display the summary statistics of the selected data    
st.write('Summary statistic:', df.describe())

# create a pairplot
st.subheader('Pairplot')

# select the column to be used as hue in pairplot
hue_column = st.selectbox('Selcet a column to be used as hue', df.columns)
st.pyplot(sns.pairplot(df, hue=hue_column))

# create a heatmap
st.subheader('Heatmap')
# select the columns which are numeric and then create a corr_matix
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr()

from plotly import graph_objects as go
# convert the seaborn heatmap plot to a plotly figure
heatmap_fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
x=corr_matrix.columns,
y=corr_matrix.columns,
colorscale='Viridis'))
st.plotly_chart(heatmap_fig)