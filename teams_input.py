from validation_File import get_positive_integer, get_valid_name

def get_team_id(message: str) -> int:
    return get_positive_integer(message)

def get_team_name(message: str) -> str:
    return get_valid_name(message)
        