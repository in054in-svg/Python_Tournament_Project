from teams_input import get_team_id
from validation_File import get_positive_integer
from validation_File import team_search


def get_home_team_id(teams: list) -> int:
    # להוציא את החיפוש לפונקציה נפרדת
    while True:
        home_team_id = get_team_id('Enter home team id:')
        if team_search(teams ,home_team_id):
            return home_team_id
        print("The id doesn't exist")
        
        
def get_away_team_id(teams: list, home_team_id: int) -> int:
    # להוציא את החיפוש לפונקציה נפרדת
    while True:
        away_team_id = get_team_id('Enter away team id:')
        if team_search(teams ,away_team_id):
            return away_team_id
    
        if away_team_id == home_team_id:
            print("You've already inserted this id for home team")
    
        else:
            print("The id doesn't exist")
            
            
def get_team_goals(team_type: str) -> int:
    return get_positive_integer(f'Enter {team_type} team goals:')