import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from utils.loader import load_csv
from analysis.batting import batting_stats
from analysis.bowling import bowling_stats
from analysis.teamanalysis import (
    matches_played_per_team,
    win_percentage_per_team
)
from config import DATA_PATH
st.set_page_config(page_title="Cricket Analysis",layout="wide")
st.title("🏏 Cricket Data Analysis Dashboard")
matches_df=load_csv(DATA_PATH+"matches.csv")
ball_df=load_csv(DATA_PATH+"deliveries.csv")
tab1,tab2,tab3=st.tabs(["Batting","Bowling","Teams"])

with tab1:
    st.header("🏏 Batting Analysis")

    batting = batting_stats(ball_df)
    top_batting = batting.head(10).reset_index()

    st.subheader("Top 10 Batsmen by Runs")

    fig = px.bar(
        top_batting,
        x="Runs",
        y="batter",
        orientation="h",
        color="Runs",
        color_continuous_scale="viridis",
        labels={
            "batter": "Batsman",
            "Runs": "Total Runs"
        },
        title="Top 10 Batsmen by Runs"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=500,
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
with tab2:
    st.header("🎯 Bowling Analysis")

    bowling = bowling_stats(ball_df)
    top_bowling = bowling.head(10).reset_index()
    top_bowling.rename(columns={"index": "bowler"}, inplace=True)

    st.subheader("Top 10 Bowlers by Wickets")

    fig = px.bar(
        top_bowling,
        x="Wickets",
        y="bowler",
        orientation="h",
        color="Wickets",
        color_continuous_scale="plasma",
        labels={
            "bowler": "Bowler",
            "Wickets": "Total Wickets"
        },
        title="Top 10 Bowlers by Wickets"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=500,
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)


with tab3:
        st.header("Team Performance Analysis")

        team_counts = matches_played_per_team(matches_df)
        win_pct = win_percentage_per_team(matches_df)

        st.subheader("Matches Played per Team")
        st.bar_chart(team_counts)

        st.subheader("Win Percentage per Team")
        st.bar_chart(win_pct)
