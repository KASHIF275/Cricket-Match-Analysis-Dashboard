import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean dataset
data = pd.read_csv('ODI_Match_info.csv')
data_cleaned = data.dropna(subset=['toss_winner', 'winner'])

# App Title
st.title("ODI Cricket Insights Dashboard")

# Section: Team Toss Wins
st.subheader("Analysis of Toss Wins by Team")
toss_wins = data_cleaned['toss_winner'].value_counts().reset_index()
toss_wins.columns = ['Team', 'Toss Wins']
bar_chart1 = px.bar(toss_wins, x='Toss Wins', y='Team', orientation='h',
                    color='Toss Wins', color_continuous_scale='Viridis',
                    title="Number of Toss Wins per Team")
st.plotly_chart(bar_chart1)

# Section: Teams Winning Both Toss & Match
st.subheader("Teams Winning Both Toss and Match")
winning_teams = data_cleaned[data_cleaned['toss_winner'] == data_cleaned['winner']]
winning_counts = winning_teams['toss_winner'].value_counts().reset_index()
winning_counts.columns = ['Team', 'Wins After Toss Win']
bar_chart2 = px.bar(winning_counts, x='Wins After Toss Win', y='Team', orientation='h',
                    color='Wins After Toss Win', color_continuous_scale='Cividis',
                    title="Teams That Won Both Toss and Match")
st.plotly_chart(bar_chart2)

# Section: Teams Losing Toss but Winning Match
st.subheader("Teams Losing Toss but Winning Match")
losing_teams = data_cleaned[data_cleaned['toss_winner'] != data_cleaned['winner']]
losing_counts = losing_teams['winner'].value_counts().reset_index()
losing_counts.columns = ['Team', 'Wins After Toss Loss']
bar_chart3 = px.bar(losing_counts, x='Wins After Toss Loss', y='Team', orientation='h',
                    color='Wins After Toss Loss', color_continuous_scale='Plasma',
                    title="Teams Losing Toss but Winning Match")
st.plotly_chart(bar_chart3)

# Section: Team Winning Percentage
st.subheader("Winning Percentage Analysis")
matches_played = pd.concat([data_cleaned["team1"], data_cleaned["team2"]]).value_counts()
matches_won = data_cleaned['winner'].value_counts()
percentage_win = (matches_won / matches_played) * 100
percentage_win = percentage_win.reset_index()
percentage_win.columns = ['Team', 'Winning Percentage']
fig_line = px.line(percentage_win, x='Team', y='Winning Percentage', 
                   markers=True, title='Winning Percentage by Team')
st.plotly_chart(fig_line)

# Section: Toss Decisions by Teams
st.subheader('Toss Decisions Made by Teams')
toss_decisions = data_cleaned.groupby('toss_winner')['toss_decision'].value_counts().reset_index(name='Count')
toss_decision_chart = px.bar(toss_decisions, x='Count', y='toss_winner', color='toss_decision',
                             orientation='h', barmode='group', title='Teams and Their Toss Decisions')
st.plotly_chart(toss_decision_chart)

# Section: Matches at Different Venues
st.subheader('Match Distribution at Venues')
plt.figure(figsize=(10, 6))
sns.barplot(x=data_cleaned['venue'].value_counts().values, 
            y=data_cleaned['venue'].value_counts().index, palette='coolwarm')
plt.xlabel('Number of Matches')
plt.ylabel('Venue')
plt.title('Matches Distribution per Venue')
st.pyplot(plt)

# Additional Filter Options
st.sidebar.header('Display Options')
columns_to_show = st.sidebar.multiselect('Select Columns to Display:', data_cleaned.columns.tolist())

if columns_to_show:
    filtered_view = data_cleaned[columns_to_show]
    st.dataframe(filtered_view)
