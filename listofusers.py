list_of_users = {}


def generate_list_of_users():

    with open("passwdlist.txt") as file:
        for line in file:
            line = line[:-1]
            key, value = line.split(":")
            list_of_users[key] = value
        return list_of_users



