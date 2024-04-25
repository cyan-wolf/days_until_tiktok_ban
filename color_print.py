from enum import Enum

class Color(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    GRAY = 7

# Prints text of the specified color.
def color_print(text, color, end='\n'):
    print(color_str(text, color), sep='', end=end)

# Returns a string that, when printed, appears as the specified color.
def color_str(text, color):
    code = color_to_code(color)
    return f"\033[{code}m{text}\033[0m"

# Matches a color to its corresponding code for stdout colors.
def color_to_code(color) -> str:
    match color:
        case Color.BLACK:
            return '30'
        
        case Color.RED:
            return '31'
        
        case Color.GREEN:
            return '32'
        
        case Color.YELLOW:
            return '33'
        
        case Color.BLUE:
            return '34'
        
        case Color.MAGENTA:
            return '35'
        
        case Color.CYAN:
            return '36'
        
        case Color.GRAY:
            return '90'
        
        case _:
            return '30'
        