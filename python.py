import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Loading
@st.cache_data
def load_data():
    # Loading the dataset - adjust the path according to your file location
    df = pd.read_csv('C:\\Users\\abc\\Desktop\\vscode\\ODI_Match_info.csv')
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header('Filter Options')
column_filter = st.sidebar.multiselect('Select Columns to Display:', df.columns.tolist())

# Dropdown to filter matches by season
season_filter = st.sidebar.selectbox('Filter by Season', df['season'].unique())

# Filter Data Based on User Input
filtered_data = df[df['season'] == season_filter]

# Apply column filter if selected
if column_filter:
    filtered_data = filtered_data[column_filter]

# Dashboard Layout
st.title("ODI Match Information Dashboard")
st.markdown("### Overview")
st.dataframe(filtered_data)

# Plotly Chart - Number of Matches per Team
st.markdown("### Matches Played by Each Team")
fig1 = px.histogram(filtered_data, x='team1', title='Number of Matches per Team')
st.plotly_chart(fig1)

# Seaborn Plot - Matches Won by Toss Decision
st.markdown("### Matches Won Based on Toss Decision")
if 'toss_decision' in filtered_data.columns and 'winner' in filtered_data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='toss_decision', hue='winner', data=filtered_data)
    plt.title('Matches Won by Toss Decision')
    st.pyplot(plt)
else:
    st.warning("Please check the column names for the Seaborn chart.")

# Matplotlib Plot - Scatter Plot of Toss Decision vs Venue
st.markdown("### Toss Decision vs Venue")
if 'toss_decision' in filtered_data.columns and 'venue' in filtered_data.columns:
    fig2, ax = plt.subplots()
    ax.scatter(filtered_data['toss_decision'], filtered_data['venue'])
    ax.set_title('Toss Decision vs Venue')
    st.pyplot(fig2)
else:
    st.warning("Please check the column names for the Matplotlib chart.")

