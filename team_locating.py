def team_search(teams: list, team_id: int = None, team_name: str = None) -> dict|bool:
    for team in teams:
        if team['id'] == team_id or team['name'] == team_name:
            return team
    return False