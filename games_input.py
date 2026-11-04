from teams_input import get_team_id
from validation_File import get_positive_integer
from team_locating import team_search


def get_home_team_id(teams: list) -> int:
    # להוציא את החיפוש לפונקציה נפרדת
    while True:
        home_team_id = get_team_id('Enter home team id:')
        if not team_search(teams ,home_team_id):
            return home_team_id
        print("The id doesn't exist")
        
        
def get_away_team_id(teams: list, home_team_id: int) -> int:
    # להוציא את החיפוש לפונקציה נפרדת
    while True:
        away_team_id = get_team_id('Enter away team id:')
        if not team_search(teams ,away_team_id):
            return away_team_id
    
        if away_team_id == home_team_id:
            print("You've already inserted this id for home team")
    
        else:
            print("The id doesn't exist")
            
            
def get_team_goals(team_type: str) -> int:
    return get_positive_integer(f'Enter {team_type} team goals:')


def get_goals(teams: list, matches: list) -> int:    
    home_team_id = get_home_team_id(teams)
    away_team_id = get_away_team_id(teams, home_team_id)
    
    for match in matches:
        if match['home_team_id'] == home_team_id and match['away_team_id'] == away_team_id\
            or match['away_team_id'] == home_team_id and match['home_team_id'] == away_team_id:


           
    home_goals = get_positive_integer('Enter home goals amount:')
    away_goals = get_positive_integer('Enter away goals amount:')