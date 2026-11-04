import time
from output import show_menu, show_team_details
from teams_addition import add_new_team
from games_addition import add_new_game
from tournament_management import rat_table

if __name__ == "__main__":
    teams = [
  {
    "id": 1,
    "name": "Maccabi Tel Aviv",
    "played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0
  },
  {
    "id": 2,
    "name": "Maccabi Haifa",
    "played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0
  }
]

    matches = []
    while True:
        choice = show_menu()
        match choice:
            case 1:
                print(add_new_team(teams))
                
            case 2:
                print(show_team_details(teams))
                
            case 3:
                print(add_new_game(teams, matches))
                
            case 4:
                print(rat_table(teams))
                
            case 0:
                break
        print(teams)
        
        time.sleep(2)