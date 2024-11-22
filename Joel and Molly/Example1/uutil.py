debug_log_level = 1
debug_log_level_dict = {
    "ERROR": 1,
    "INFO": 2,
    "DEBUG": 3,
    "1": 1,
    "2": 2,
    "3": 3
}        

def get_player_key_by_player(player=None):        
    # return player.player_team + '|' + player.player_number
    return get_player_key(player.player_team, player.player_number)

def get_player_key(team_name=None, player_number=None):        
    if team_name is None:
        return    

    if player_number is None:
        return

    return team_name + '-' + player_number

# def print_debug(value):
#     print_debug_by_log_level(value, "ERROR")

def print_debug(value, log_level):
    log_level = debug_log_level_dict[str(log_level).upper()]

    if is_blank(log_level):
        log_level = 1

    if log_level > debug_log_level:
        return

    print(f"#### {value}")

def set_debug_level(value):    
    if not is_blank(value):
        debug_level = debug_log_level_dict[str(value).upper()]

        global debug_log_level

        debug_log_level = debug_level
    else:
        raise Exception("Allowed values are error, info, debug, 1, 2 or 3")         

def is_blank(value=None):
    if value == None or str(value).strip() == "":
        return True
    else:
        return False
    
def is_blank_to_value(value, default_value):
    if is_blank(value):
        return default_value
    else:
        return value    
