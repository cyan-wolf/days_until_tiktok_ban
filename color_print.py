
def print_black(text, end='\n'):
    print('\033[30m', text, '\033[0m', sep='', end=end)

def print_red(text, end='\n'):
    print('\033[31m', text, '\033[0m', sep='', end=end)

def print_green(text, end='\n'):
    print('\033[32m', text, '\033[0m', sep='', end=end)

def print_yellow(text, end='\n'):
    print('\033[33m', text, '\033[0m', sep='', end=end)

def print_blue(text, end='\n'):
    print('\033[34m', text, '\033[0m', sep='', end=end)

def print_magenta(text, end='\n'):
    print('\033[35m', text, '\033[0m', sep='', end=end)

def print_cyan(text, end='\n'):
    print('\033[36m', text, '\033[0m', sep='', end=end)

def print_gray(text, end='\n'):
    print('\033[90m', text, '\033[0m', sep='', end=end)
