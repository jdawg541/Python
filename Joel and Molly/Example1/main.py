import uutil
import json
import os
import pickle
from wrappers import Player
from wrappers import FantasyTeam
from wrappers import FantasyTeamJSONEncoder
from wrappers import FantasyTeamJSONDecoder
from wrappers import PlayerStat

filename = "data.json"
teams = {}

def load_data():    
    try:
        os.stat(filename).st_size

        with open(filename, "r") as f:
            # Do something with the file
            data = f.read()
            print("data: ", data)

            if data != "":
                uutil.print_debug("No teams defined")

            teams_data = json.load(data)
    
            uutil.print_debug("teams: " + teams_data)

            # for record in teams_data.items():                
            #     team = FantasyTeam(name_parameter)
            #     new_player.player_name=details["player_name"] 
            #     new_player.player_team=details.get("player_team") 
            #     new_player.player_number=details.get("player_number") 
            #     new_player.player_position=details.get("player_position")
            #     new_player.all_players[name.lower()] = new_player
    except FileNotFoundError:
        print("File not found!")

        return None
    except Exception as e:
        print("An error occurred:", e)

        return None

# def save_record(record):
#     save_data(data + "," + json.dumps(record.to_dict(), indent=4))


def save_data():
    # uutil.print_debug("teams: " + json.dumps(teams, cls=FantasyTeamJSONEncoder), "error")
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(teams, cls=FantasyTeamJSONEncoder, indent=4))

# If filename is blank or none, then bail out since we have nothing to work with
# def load_players(filename=None):
#     if uutil.is_blank(filename):
#         return
    
#     data = None

#     try:
#         data = get_file_contents(filename)
#     except:
#         print("An exception occurred while getting the player data")

#     player_data = json.load(data)
    
#     for name, details in player_data.items():
#         name_parameter = details["player_name"]
#         new_player = Player(name_parameter)
#         new_player.player_name=details["player_name"] 
#         new_player.player_team=details.get("player_team") 
#         new_player.player_number=details.get("player_number") 
#         new_player.player_position=details.get("player_position")
#         new_player.all_players[name.lower()] = new_player

def add_team():
    print('Please input details for your new team')
    team_name = input('Team Name: ')
    team = FantasyTeam()

    team.name = team_name
    team.key = team_name
    
    teams[team_name.upper()] = team    
    

def add_player():
    print('Please input details for your new player')
    team_name = input('Team Name: ')

    team = teams.get(team_name.upper())

    uutil.print_debug("teams: " + str(team), "error")

    if team is None:
        print('Team not found')

        return
    
    # teamObj = json.loads(str(team), cls=FantasyTeamJSONDecoder)

    player = Player()
    player.player_name = input('Player\'s Name: ')
    player.player_team = team.name
    player.player_position = input('Player\'s Position: ')
    player.player_number = input('Player\'s Number: ')

    team.add_player(player)    

def remove_player():
    return    

def show_team():
    return

def show_player():
    return

def show_all_players():
    return

def print_teams():
    uutil.print_debug("teams: " + json.dumps(teams, cls=FantasyTeamJSONEncoder), "error")

def run():
    uutil.set_debug_level("info")

    uutil.print_debug("Test", "debug")

    filename = "allPlayers.json"
    data = load_data()

    functions = {
        "1": add_team,
        "2": add_player,
        "3": remove_player,
        "4": show_player,
        "5": show_all_players,
        "S": save_data,
        "SAVE": save_data,
        "P": print_teams,
        "PRINT": print_teams
    }

    while True:
        user_action = input("\nWhat would you like to do?\n" +
        "1 - Add Team\n" +
        "2 - Add Player\n" +
        "3 - Remove Player\n" +
        "4 - Show Player Info\n" +
        "5 - Show All Players\n" +
        "P or Print - Print\n" +
        "S or Save - Save\n" +
        "Q - Quit \n")
        
        # if user_action.upper() == "Q":
        #     break
        # else:
        uutil.print_debug("user_action: " + user_action, "error")

        # try:                
        #     # function_selection(functions, user_action)
        func = functions[user_action.upper()]

        if func is not None:
            func()
            # except:
            #     print('Invalid selection. Please try again.')

run()