def get_positive_integer(message: str) -> int:
    while True:
            try:
                num = int(input(message))
                if num >= 0:
                    return num
                print('Enter positive number only!')
    
            except ValueError as err:
                print('Enter numbers only!')


def get_valid_name(message: str) -> str:
    while True:
            name = input('Enter team name:').strip().lower()
            if name:
                return name
            
            
def team_search(teams: list, team_id: int = None, team_name: str = None) -> dict|bool:
    for team in teams:
        if team['id'] == team_id or team['name'] == team_name:
            return team
    return False


def games_search(matches: list, home_team_id: int, away_team_id: int) -> bool:
    for match in matches:
        if match['home_team_id'] == home_team_id and match['away_team_id'] == away_team_id\
        or match['away_team_id'] == home_team_id and match['home_team_id'] == away_team_id:
            return True