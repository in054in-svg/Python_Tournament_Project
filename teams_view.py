def show_team_details(teams: list) -> str:
    # לפרק לפונקציות
    team_details = ''
    for team in teams:
        team_details += 'id: ' + team['id'] + 'name: ' + team['name'] +'played: ' + team['played'] + 'points: ' + team['points'] + '\n'

    if team_details:
        return team_details
    else:
        return 'There are no teams in the system yet.'