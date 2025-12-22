def validate_ball_data(df):
    required_cols = {
        "batter",
        "bowler",
        "batsman_runs",
        "is_wicket",
        "player_dismissed"
    }

    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in dataset: {missing}")
