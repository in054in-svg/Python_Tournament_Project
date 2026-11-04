from teams_input import get_team_id, get_team_name
from validation_File import team_search


def add_new_team(teams: list) -> str:
    # לפרק לפונקציות של קבלת מספר ושל חיפוש ולעשות ביחד עם הוספת משחקים
    while True:
        team_id = get_team_id('Enter team id:')
        if not team_search(teams ,team_id= team_id):
            break
        print('The id already exist')
        # for team in teams:
        #     if team['id'] == team_id:
        #         break
        # else:
        #     break

    while True:
        team_name = get_team_name('Enter team name:')
        if not team_search(teams ,team_name = team_name):
            break
        print('The name already exist')
        # for team in teams:
        #     if team['id'] == team_id:
        #         break
        # else:
        #     break


    teams.append({'id': team_id, 'name': team_name, 'played': 0,
                  'wins': 0, 'draws': 0, 'losses': 0,
                  'goals_for': 0, 'goals_against': 0, 'points': 0})
    
    
    return 'The team registered successfully!'