def rat_table(teams: list):
    sort_teams = sorted(teams, key= lambda team: (team['points'], team['goals_for'] - team['goals_against'], team['goals_for'], team['name']))
    for team in sort_teams:
        team.pop('id')
        team['difference'] = team['goals_for'] - team['goals_against']
        
    return sort_teams