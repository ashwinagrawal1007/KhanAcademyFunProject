import random

user_base = {   0 : [1, 2, 3, 4, 8],
                1 : [0, 2, 5, 6, 7],
                2 : [0, 1, 4, 8, 9],
                3 : [0, 4, 5, 6, 9],
                4 : [0, 2, 3, 5, 7],
                5 : [1, 3, 4, 6, 9],
                6 : [1, 3, 5, 7, 8],
                7 : [1, 4, 6],
                8 : [0, 2, 6, 9],
                9 : [2, 3, 5, 8],
                10 : [11],
                11 : [10]
}

infected = []
to_be_infected = []

def total_infection_pass():
    global to_be_infected
    select_user_to_start()
    while len(to_be_infected) > 0:
        node = to_be_infected.pop(0)
        infect(node)
        to_be_infected = to_be_infected + [user for user in user_base[node] if user not in infected and user not in to_be_infected]

def infect(element):
    infected.append(element)

def select_user_to_start():
    user_to_start_with = random.choice([user for user in user_base.keys() if user not in infected])
    to_be_infected.append(user_to_start_with)

def total_infection():
    while len(infected) != len(user_base):
        total_infection_pass()
        if len(infected) != len(user_base):
            proceed = raw_input("infected " + str(len(infected)) + " users, left with " + str(len(user_base) - len(infected)) + " more users, proceed furthur? [yes/no] ")
            if proceed == "no":
                break
    print "infected " + str(len(infected) * 100.0/len(user_base)) + "%" + " users"

total_infection()