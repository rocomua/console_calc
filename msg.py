# msg file for console calc

start = """Welcome to
Console calculator
"""
welcome = """Please type:
q    | quit app
reg  | register a new account
log  | login to your account
calc | use calculator"""

welcomereg = """shh  | to show history
clh  | clear history
off  | logoff"""

prompt = ">>> "

command_not_found = """Command not found."""

command_not_ath = """Login first to use this command"""

already_logged = """You are logged in"""

create_user = """Create new user profile."""

input_username = f"""Please input username. 
It should be: 
2 symbols or more
Latin lowercase
{prompt}"""

too_short = "Username too short"

user_exist = "User already registered. Try another name!"

login_username = f"""Please input username
{prompt}"""

login_passwd = f"""Please input password
{prompt}"""

new_passwd = f"""Please input New password. 
It should be 8+ symbols and have 2+ capitals 
{prompt}"""

user_registered = """User registered"""

operand1 = f"""Input first operand.
Numbers only!
{prompt}"""

operation = f"""Input operation
"""

wrong_operation = f"""Wrong operation. 
Please start over!
"""

wrong_operation_reg = f"""Wrong operation. 
YOU MUST BE REGISTERED AND LOGGED TO PERFORM THIS OPERATION
Please start over!
"""

dbz = "Division by Zero. INFINITY!"

operand2 = f"""Input second operand
{prompt}"""

counted = "Success:"

invalid_operation = "You are Evil!"

log = "Log for user:"
log_debug = "Log entries listed"

are_you_sure = f"""Are you really going to delete all logs? 
Type Y to clear logs or any key to return.
{prompt}"""

noop = "Logfile not found. Use calc and try again!"

clrd = "Log cleared. "

ret = "Back to main menu"

finish = """Thanks for using Console Calculator
©2021 ro.com.ua"""
