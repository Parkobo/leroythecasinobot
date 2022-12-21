import rand

def make_ticket(ticket_numbers):
    t_full = []
    for(i=0;i<5;i++):
        if (i < 4):
            t_full[i] = rand(1,10)
        elif (i == 4):
            t_full[i] = rand(1,8)
        else:
            throw exception
                print ('Value out of bounds.')
    return t_full


def match_tickets(wt, t):
    matches = [0, 0]
    win_four = wt[:3]
    for(i=0;i<4;i++):
        if(t[i] in win_four):
            matches[0] += 1
    if (t[4] == wt[4]):
        matches[1] = 1
    return matches


def win_checker(m):
    payout = 0
    if(m[1] == 1):
        if(m[0] == 4):
            return globals.jackpot
        elif(m[0] == 3):
            payout = 25000
        elif(m[0] == 2):
            payout = 2500
        elif(m[0] == 1):
            payout = 500
        else:
            payout = 100
    else:
        if(m[0]==4):
            payout = 50000
        else:
            payout = 10000

    if(matches[2] > 0):
        return(payout * global.pwr_number)

    return payout


def run_lottery(player):
    pwr_number = rand(2,3,4,5,10)
    win_ticket = []
    win_ticket = make_ticket(win_ticket)
    for p in players_db_file():
        payout = 0
        pwr_plays = p.pwr_plays
        for (p.tickets > 0):
            p.tickets = p.tickets - 1
            ticket = []
            ticket = make_ticket(ticket)
            matches = [0,0,pwr_plays]
            matches = match_tickets(win_ticket, ticket)
            if (matches[0] > 0 || matches[1] > 0):
                payout += win_checker(matches)
            pwr_plays = pwr_plays - 1




