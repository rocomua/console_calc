import getpass
import math
from decimal import Decimal
import datetime
# project files
import commands
import listofusers
import msg

# EXTENDED CONSOLE INFO
DEBUG = False

# FLAGS
QUIT = False
LOGGED_IN = False
# log anonimous calc usage
LOG_ANONIMOUS = True

# constant for registered/logged username
USERNAME = ""

# localisation of vars
command_list = commands.command_list
reg_command_list = commands.reg_command_list
list_of_users = listofusers.generate_list_of_users()


# check pwd for req
def validate_pass(phrase):
    """
    check if passphrase meet req.

    :param phrase: string of symbols

    :return:
    None if OK
    ValueError with Description if Fail

    """

    try:

        pass_min_length = 8
        caps_in_phrase_limit = 2

        if len(phrase) < pass_min_length:
            raise ValueError("Length < 8")

        caps_in_phrase = 0
        for i in phrase:
            if "A" <= i <= "Z":
                caps_in_phrase += 1
        if caps_in_phrase < caps_in_phrase_limit:
            raise ValueError(f"Caps < {caps_in_phrase_limit}")

    except Exception as e:
        if DEBUG:
            print("Error: ", e)
        return False


    else:
        return True
    finally:
        pass


# create user account
def user_register():
    print(msg.create_user)
    while True:
        username = input(msg.input_username)
        if len(username) < 2:
            print(msg.too_short)
            continue
        elif username in list_of_users.keys():
            print(msg.user_exist)
            continue
        else:
            while True:
                passwd = getpass.getpass(msg.new_passwd)
                result = validate_pass(passwd)
                if result:
                    # print(result)
                    record_user = username + ":" + passwd + "\n"
                    with open("passwdlist.txt", 'a') as f:
                        f.write(record_user)
                    print(msg.user_registered)
                    listofusers.generate_list_of_users()
                    global LOGGED_IN
                    LOGGED_IN = True
                    global USERNAME
                    USERNAME = username
                    return
                else:
                    continue

    #   create user
    #       ask for username
    #       check if exist
    #       ask for password
    #       check if it OK
    #       update user_list

    pass


# log on and off
def user_login(logoff=False):
    global LOGGED_IN
    global USERNAME
    if logoff:
        LOGGED_IN = False
        USERNAME = ""
    else:
        while True:
            username = input(msg.login_username)
            # Replaced to hide symbols on typing
            # passwd = input(msg.login_passwd)
            # works in console only
            passwd = getpass.getpass(msg.login_passwd)
            # works in console only
            if DEBUG:
                print(list_of_users.get(username))
            if list_of_users.get(username) == passwd:

                LOGGED_IN = True
                USERNAME = username

                if DEBUG:
                    print("User logged:", username)
                break


# create list of allowed operations
def create_list_of_operation(reg):
    list_of_operation = ""
    signs = commands.signs
    if reg:
        signs = commands.signs + commands.reg_signs
    for command in signs:
        list_of_operation = list_of_operation + "'" + command + "'" + " "

    return list_of_operation


# record history of ops to file
def record_user_history(logentry):
    filename = f"{USERNAME}.log"
    if DEBUG:
        print(filename)

    now = str(datetime.datetime.now())
    newlogentry = now + ": " + logentry + "\n"

    with open(filename, 'a+') as f:
        f.write(newlogentry)

    if DEBUG:
        print("Log entry", newlogentry, "logged to file")


# calc with main func
def calculator():
    while True:
        try:
            list_of_operation = create_list_of_operation(LOGGED_IN)
            operand1 = Decimal(input(msg.operand1))
            operation = input(msg.operation + list_of_operation + msg.prompt).lower()
            if operation not in list_of_operation:
                print(msg.wrong_operation)
                continue
            elif operation in commands.reg_signs and not LOGGED_IN:
                print(msg.wrong_operation_reg)
                continue
            elif operation in commands.reg_signs and LOGGED_IN:
                if operation == 'sin':
                    result = Decimal(math.sin(math.radians(operand1)))
                elif operation == 'cos':
                    result = Decimal(math.cos(math.radians(operand1)))
                elif operation == 'tan':
                    result = Decimal(math.tan(math.radians(operand1)))
                else:
                    return
                output = f"{operation}({operand1}˚) = {result}"
                record_user_history(output)
                print(msg.counted)
                print(output)

                return
            else:
                # print("ask for second")
                operand2 = Decimal(input(msg.operand2))
                if operation == '+':
                    result = Decimal(operand1) + Decimal(operand2)
                elif operation == '-':
                    result = Decimal(operand1) - Decimal(operand2)
                elif operation == '*':
                    result = Decimal(operand1) * Decimal(operand2)
                elif operation == '/' and operand2 != 0:
                    result = Decimal(operand1) / Decimal(operand2)
                elif operation == '/' and operand2 == 0:
                    result = msg.dbz
                else:
                    return msg.invalid_operation
                output = f"""{operand1} {operation} {operand2} = {result}"""
                if LOG_ANONIMOUS is True or LOGGED_IN is True:
                    record_user_history(output)
                print(output)
                return


        except Exception as e:
            print("Error: ", e)


# clear log file
def clear_user_history():
    kill = input(msg.are_you_sure)
    if kill == "Y":
        filename = f"{USERNAME}.log"
        with open(filename, 'w') as f:
            f.write("")
            print(msg.clrd, msg.ret)
    else:
        print(msg.ret)
    if DEBUG:
        print("Log entries cleared")


# show file with log
def show_user_history():
    try:
        filename = f"{USERNAME}.log"
        if DEBUG:
            print(filename)

        with open(filename, 'r') as f:
            print(msg.log)
            print(f.read())

        if DEBUG:
            print(msg.log_debug)
    except Exception as e:
        print(msg.noop)


# ask user what to do
def user_prompt():
    for _ in command_list:
        print(msg.welcome)
        if LOGGED_IN:
            print(msg.welcomereg)
        choice = input(msg.prompt).lower()
        if choice not in command_list + reg_command_list:
            print(msg.command_not_found)
            continue
        if not LOGGED_IN and choice in reg_command_list:
            print(msg.command_not_ath)
            continue
        return choice


# run function based on user's selection
def main():
    selection = user_prompt()
    if DEBUG:
        print("User selected:", selection)
    if selection == "q":
        global QUIT
        QUIT = True
    elif selection == "reg":
        user_register()
    elif selection == "log":
        if LOGGED_IN:
            print(msg.already_logged)
            return
        user_login()
    elif selection == "calc":
        calculator()
    elif selection == "shh":
        show_user_history()
    elif selection == "clh":
        clear_user_history()
    elif selection == "off":
        user_login(logoff=True)
    else:
        return


#   show greeting
#   ask to choose
#       register
#       login
#       calc
#       if_logged TRUE
#           show_user_history()
#           clear_user_history()
#           logoff
#       quit

# print welcome message
print(msg.start)

# main loop
while not QUIT:
    main()

# print footer message
print(msg.finish)
