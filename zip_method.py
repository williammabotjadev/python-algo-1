# Zip Mehtod

teams = [
    "Los Angeles Lakers",
    "Chicago Bulls",
    "Charlotte Hornets",
    "Detroit Pistons",
    "DC Wizards",
    "San Antonio Spurs"
]

points = [
    23,
    10,
    40,
    24,
    35,
    14
]

score_board = list(zip(teams, points))

for k, v in score_board:
    print(k, v)