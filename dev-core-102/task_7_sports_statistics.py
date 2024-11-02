def calculate_team_performance (extra, won, lost = 0):
    score = won * 3
    return (score + extra) if won >= (won+lost)/2 else score

def player_performance(scores, bonus):
    return (sum(scores)+bonus)/len(scores) if sum(scores)>30 else sum(scores)/len(scores)

def final_report(extra, won, lost, scores, bonus, team_threshold=50, player_threshold=20):
    team_performance = calculate_team_performance(extra, won, lost)
    player_average = player_performance(scores, bonus)

    return "Good job" if team_performance > team_threshold and player_average > player_threshold else "You have to work harder"

