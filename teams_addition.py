from teams_input import get_team_id, get_team_name
from team_locating import team_search


def get_new_team(teams: list) -> None:
    # לפרק לפונקציות של קבלת מספר ושל חיפוש
    while True:
        team_id = get_team_id('Enter team id:')
        if not team_search(teams ,team_id):
            break
        print('The id already exist')
        # for team in teams:
        #     if team['id'] == team_id:
        #         break
        # else:
        #     break

    while True:
        team_name = get_team_name('Enter team name:')
        if not team_search(teams ,team_id):
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