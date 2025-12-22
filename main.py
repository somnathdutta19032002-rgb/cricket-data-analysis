import logging
import matplotlib.pyplot as plt

from utils.loader import load_csv
from utils.validate import validate_ball_data
from analysis.batting import batting_stats
from analysis.bowling import bowling_stats
from analysis.teamanalysis import (
    matches_played_per_team,
    win_percentage_per_team
)

from config import DATA_PATH, OUTPUT_PATH, PLOTS_PATH

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Cricket Analysis Started")

# Load datasets
matches_df = load_csv(DATA_PATH + "matches.csv")
ball_df = load_csv(DATA_PATH + "deliveries.csv")

validate_ball_data(ball_df)

# ---------------- BATTTING ANALYSIS ----------------
batting = batting_stats(ball_df)
top_batting = batting.head(10)

top_batting.to_csv(OUTPUT_PATH + "top_10_batting_stats.csv")

plt.figure(figsize=(10, 6))
plt.bar(top_batting.index, top_batting["Runs"])
plt.title("Top 10 Batsmen by Runs")
plt.xlabel("Batsman")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_PATH + "top_10_batsmen_runs.png")
plt.close()

# ---------------- BOWLING ANALYSIS ----------------
bowling = bowling_stats(ball_df)
top_bowling = bowling.head(10)

top_bowling.to_csv(OUTPUT_PATH + "top_10_bowling_stats.csv")

plt.figure(figsize=(10, 6))
plt.bar(top_bowling.index, top_bowling["Wickets"])
plt.title("Top 10 Bowlers by Wickets")
plt.xlabel("Bowler")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_PATH + "top_10_bowlers_wickets.png")
plt.close()

# ---------------- TEAM ANALYSIS ----------------
team_counts = matches_played_per_team(matches_df)

plt.figure(figsize=(10, 6))
team_counts.plot(kind="bar")
plt.title("Matches Played by Each Team")
plt.xlabel("Team")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_PATH + "matches_per_team.png")
plt.close()

logging.info("Cricket Analysis Completed Successfully")
