import random
import string

def get_one_ticket():
    ticket = ''
    my_list = []
    for i in range(99):
        rnd = random.randint(0, 9)
        if rnd == 0 and len(ticket) == 0:
            my_list.append(rnd)
        else:
            if len(ticket) != 7:
                ticket += str(rnd)
    return(ticket)

tickets = []
def get_100_tickets():
    for i in range(100):
        if get_one_ticket() not in tickets:
            tickets.append(get_one_ticket())
            print(get_one_ticket())

get_100_tickets()
