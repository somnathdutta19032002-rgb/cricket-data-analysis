import  pandas as pd
df=pd.read_csv("../data/matches.csv")
df=df[["team1","team2","toss_winner","winner"]]
df.dropna(inplace=True)
df["team_wins"]=(df["winner"]==df["team1"]).astype(int)
print(df.head())
teams=pd.concat([df["team1"],df["team2"]]).unique()
team_map={team:idx for idx,team in enumerate(teams)}
df["team1_code"]=df["team1"].map(team_map)
df["team2_code"]=df["team2"].map(team_map)
df["toss_winner_code"]=df["toss_winner"].map(team_map)
print(team_map)
x=df[["team1_code","team2_code","toss_winner_code"]]
y=df["team_wins"]
split_index=int(0.8*len(df))
X_train= x.iloc[:split_index]
X_test=x.iloc[split_index:]
Y_train=y.iloc[:split_index]
Y_test=y.iloc[split_index:]
def simple_predict(row):
    return 1 if row["toss_winner_code"] == row["team1_code"] else 0
predictions = X_test.apply(simple_predict, axis=1)
accuracy = (predictions == Y_test).mean()
print("Model Accuracy:", accuracy)
