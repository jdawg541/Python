import uutil
import json
from pprint import pprint
from json import JSONEncoder
from json import JSONDecoder

class FantasyTeamJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
    
class FantasyTeamJSONDecoder(JSONDecoder):
    def decode(self, s, **kwargs):
        obj = super().decode(s, **kwargs)
        return FantasyTeam(**obj)    

class FantasyTeam:
    def __init__(self):
        # self.name = name
        # self.__players = {} # This becomes _FantasyTeam__players as the key in the payload which is not ideal
        self.players = {}
    
    def add_player(self, player=None):
        if player is None:
            raise Exception("Player is required")
        
        self.players[player.get_player_key()] = player        
    
    def remove_player(self, player=None):
        if player is None:
            raise Exception("Player is required")
        
        try:
            self.players.pop(player.player_name.upper())

            print(f"{player.player_name} has been successfully removed from your team.")
        except:
            print(f"{player.player_name} could not be removed from your team.")
    
    def get_player(self, key):
        if len(self.players) == 0:
            print("You have no players on your team.")
        else:
            return self.players.get(key)
            # for player in self.players.values():
            #     print(player.player_name)
    
    def get_players(self):
        return self.__players
    
    # def __str__(self):
    #     return f"{self.__players}"
    
    # def __iter__(self):
    #     return iter(self.__players)

    # def __dict__(self):
    #     return {
    #         "team_name": self.name,
    #         "players": self.__players
    #     }
    
    # def to_dict(self):
    #     return {
    #         "team_name": self.name,
    #         "players": self.__players
    #     }

# def function_selection(functions, function_number):
#     functions[function_number]()

# def manage_fantasy_team():
#     mollys_team = FantasyTeam()
#     functions = {"1": mollys_team.add_player,
#         "2": mollys_team.remove_player,
#         "3": mollys_team.get_player_details,
#         "4": mollys_team.get_player_names}
    
#     while True:
#         user_action = input("""\n What would you like to do?
#     1 - Add Player
#     2 - Remove Player
#     3 - Show Player Info
#     4 - Show All Players
#     5 - Quit \n""")
        
#         if user_action == "5":
#             break
#         else:
#             try:
#                 function_selection(functions, user_action)
#             except:
#                 print("Invalid selection. Please try again.")

class Player:    
    # def __init__(self, player_name, player_team=None, player_position=None, player_number=None):
    def __init__(self):
        self.player_name = None
        self.player_team = None
        self.player_position = None
        self.player_number = None
        self.player_stats = {}

    def add_stat(self, stat):
        if stat == None:
            return
        
        if uutil.is_blank(stat.stat_name):
            return
        
        self.player_stats[stat.stat_name.upper()] = stat

    def get_stat(self, stat_name):
        if uutil.is_blank(stat_name):
            return  

        return self.player_stats[stat_name.upper()]
    
    def get_player_key(self):        
        return uutil.get_player_key(self.player_team, self.player_number)
        # return self.player_team + '-' + self.player_number
            
            
    def __str__(self):
        return f"{self.player_name}, number {self.player_number}, plays {self.player_position} for {self.player_team} stats: {self.player_stats}"
    
    # @classmethod
    # def post_player_file(players):
    #     players = Player.all_players
    #     players_dict = {name: player.to_dict() for name, player in players.items()}
    #     # UUtil.debug_print(players_dict)
        
    #     # Serializing json
    #     json_object = json.dumps(players_dict, indent=4)

    #     # Writing to json file
    #     with open("allplayers.json", "w") as outfile:
    #         outfile.write(json_object)
    
    # @classmethod
    # def load_players(cls,filename="allplayers.json"):
    #     with open(filename, "r") as player_file:
    #         player_data = json.load(player_file)
    #         for name, details in player_data.items():
    #             name_parameter = details["player_name"]
    #             new_player = Player(name_parameter)
    #             new_player.player_name=details["player_name"] 
    #             new_player.player_team=details.get("player_team") 
    #             new_player.player_number=details.get("player_number") 
    #             new_player.player_position=details.get("player_position")
    #             new_player.all_players[name.lower()] = new_player

class PlayerStat:
    def __init__(self, stat_name, stat_display_name=None, stat_value=None, datatype=None):
        self.stat_name = stat_name
        self.stat_display_name = stat_display_name
        self.stat_value = stat_value
        self.datatype = datatype
            
    def __str__(self):
        return f"{self.stat_name} has a display value of {self.stat_display_name}, The value is {self.stat_value} and the datatype is {self.datatype}"
    
    # "statName": "totalAssists",
    #         "statDisplayName": "Total Assists",
    #         "statValue": 2,
    #         "datatype": "INTEGER"