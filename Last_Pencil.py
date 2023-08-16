from random import randint


def play_turn(num_pens, player):
    while num_pens > 0:
        print('|' * num_pens)
        if player == 1:
            choice = bot(num_pens)
            print(choice)
        else:
            while True:
                try:
                    choice = int(input(f"{players[0]}'s turn:"))
                    if choice not in [1, 2, 3]:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    if choice > num_pens:
                        print('Too many pencils were taken')
                        continue
                    break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
        num_pens -= choice

        if num_pens <= 0:
            print(f'{players[1 - player]} won!')
            break

        player = 1 - player


def bot(pencils_left):
    print(f"{players[1]}'s turn:")
    if pencils_left in list(range(4, 500, 4)):
        return 3
    elif pencils_left in list(range(3, 500, 4)):
        return 2
    elif pencils_left in list(range(2, 500, 4)):
        return 1
    elif pencils_left in list(range(5, 500, 4)):
        return randint(1, 3)
    else:
        return 1


while True:
    try:
        start_num_p = int(input('How many pencils would you like to use:'))
        if 0 < start_num_p:
            break
        print('The number of pencils should be positive')
    except ValueError:
        print('The number of pencils should be numeric')

players = ['John', 'Jack']

print(f'Who will be the first ({", ".join(players)}):')
while True:
    player_1 = str(input())
    if player_1 in players:
        break
    print(f"Choose between '{players[0]}' and '{players[1]}'")

player_idx = players.index(player_1)

play_turn(start_num_p, player_idx)
