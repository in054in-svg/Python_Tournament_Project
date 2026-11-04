def get_positive_integer(message: str) -> int:
    while True:
            try:
                num = int(input(message))
                if num > 0:
                    return num
                print('Enter positive number only!')
    
            except ValueError as err:
                print('Enter numbers only!')


def get_valid_name(message: str) -> str:
    while True:
            name = input('Enter team name:').strip().lower()
            if name:
                return name