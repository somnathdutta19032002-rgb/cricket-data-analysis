import numpy as np
import pandas as pd

def batting_stats(ball_df):
    runs = ball_df.groupby("batter")["batsman_runs"].sum()
    balls = ball_df.groupby("batter").size()

    outs = (
        ball_df[ball_df["player_dismissed"] == ball_df["batter"]]
        .groupby("batter")
        .size()
    )

    outs = outs.reindex(runs.index, fill_value=0)

    average = runs / outs.replace(0, np.nan)
    strike_rate = (runs / balls) * 100

    stats = pd.DataFrame({
        "Runs": runs,
        "Balls": balls,
        "Outs": outs,
        "Average": average,
        "Strike_Rate": strike_rate
    })

    return stats.sort_values("Runs", ascending=False)
