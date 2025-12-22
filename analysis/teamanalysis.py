import pandas as pd


def matches_played_per_team(matches_df):
    """
    Returns number of matches played by each team
    """
    teams = pd.concat([matches_df["team1"], matches_df["team2"]])
    return teams.value_counts()


def matches_won_per_team(matches_df):
    """
    Returns number of matches won by each team
    """
    return matches_df["winner"].value_counts()


def win_percentage_per_team(matches_df):
    """
    Calculates win percentage for each team
    """
    played = matches_played_per_team(matches_df)
    won = matches_won_per_team(matches_df)

    win_pct = (won / played) * 100

    stats = pd.DataFrame({
        "Matches_Played": played,
        "Matches_Won": won,
        "Win_Percentage": win_pct
    }).fillna(0)

    return stats.sort_values("Win_Percentage", ascending=False)


def home_vs_away_performance(matches_df):
    """
    Analyzes home vs away wins (venue-based)
    """
    home_wins = matches_df[
        matches_df["team1"] == matches_df["winner"]
    ]["winner"].value_counts()

    away_wins = matches_df[
        matches_df["team2"] == matches_df["winner"]
    ]["winner"].value_counts()

    stats = pd.DataFrame({
        "Home_Wins": home_wins,
        "Away_Wins": away_wins
    }).fillna(0)

    return stats.sort_values("Home_Wins", ascending=False)
