from games_input import get_home_team_id, get_away_team_id, get_team_goals
from validation_File import games_search

def add_new_game(teams: list, matches: list) -> str:
    home_team_id = get_home_team_id(teams)
    away_team_id = get_away_team_id(teams, home_team_id)
    
    if games_search(matches, home_team_id, away_team_id):
        return 'The game already registered'
        
    home_goals = get_team_goals('home')
    away_goals = get_team_goals('away')
    
    matches.append(
        {"home_team_id": home_team_id, "away_team_id": away_team_id,
        "home_goals": home_goals, "away_goals":away_goals}
    )
    
    if home_goals > away_goals:
        result = 1
    elif away_goals > home_goals:
        result = 2
    else:
        result = 0
   
    for team in teams:
        if result == 0:
            if team['id'] == home_team_id or team['id'] == away_team_id:
                team['played'] += 1 
                team['draws'] += 1
                team['goals_for'] += home_goals
                team['goals_against'] += away_goals
                team['points'] += 1
        
        else:
            if team['id'] == home_team_id:
                team['played'] += 1 
                team['wins'] += 1 if result == 1 else 0
                team['losses'] += 0 if result == 1 else 1
                team['goals_for'] += home_goals 
                team['goals_against'] += away_goals
                team['points'] += 3 if result == 1 else 0
            
            elif team['id'] == away_team_id:
                team['played'] += 1
                team['wins'] += 1 if result == 2 else 0
                team['losses'] += 0 if result == 2 else 1
                team['goals_for'] += away_goals
                team['goals_against'] += home_goals
                team['points'] += 3 if result == 2 else 0
                
    return 'The game registered successfully'