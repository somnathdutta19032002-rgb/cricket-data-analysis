import pandas as pd

def bowling_stats(ball_df):
    wickets = (
        ball_df[ball_df["is_wicket"] == 1]
        .groupby("bowler")
        .size()
    )

    runs_conceded = ball_df.groupby("bowler")["batsman_runs"].sum()
    balls = ball_df.groupby("bowler").size()

    economy = (runs_conceded / balls) * 6

    stats = pd.DataFrame({
        "Wickets": wickets,
        "Runs_Conceded": runs_conceded,
        "Economy": economy
    }).fillna(0)

    return stats.sort_values("Wickets", ascending=False)

