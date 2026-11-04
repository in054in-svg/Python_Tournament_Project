from teams_input import get_team_name, get_team_id
from team_locating import team_search


def get_goals(teams: list) -> int:
    # לפרק לפונקציות של קבלת מספר ושל חיפוש
    while True:
        home_team_id = get_team_id('Enter home team id:')
        if not team_search(teams ,home_team_id):
            break
        print("The id doesn't exist")
    
    while True:
        away_team_id = get_team_name('Enter away team id:')
        if not team_search(teams ,away_team_id):
            break
        
        if away_team_id == home_team_id:
            print('You ')
            
        else:
            print("The id doesn't exist")