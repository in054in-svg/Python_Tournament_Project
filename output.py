from validation_File import get_positive_integer


def show_menu() -> int:
    choice = get_positive_integer("""========== TOURNAMENT MANAGER ==========
1. Add team
2. Show all teams
3. Add match result
4. Show standings
5. Show leading team
6. Show best attacking team
7. Show team success rate
8. Show teams without wins
9. Show tournament summary
10. Check championship potential
0. Exit
Choose an option:
""")
    return choice


def show_team_details(teams: list) -> str:
    # לפרק לפונקציות
    team_details = ''
    for team in teams:
        team_details += 'id: ' + str(team['id']) + ' name: ' + team['name'] +' played: ' + str(team['played']) + ' points: ' + str(team['points']) + '\n'

    if team_details:
        return team_details
    else:
        return 'There are no teams in the system yet.'