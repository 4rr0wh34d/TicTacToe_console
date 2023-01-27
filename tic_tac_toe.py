import random


def display(result, player):

    print(f'''-------------------------------
|         |         |         |
|{pos[(0, 0)]}        |{pos[(0, 1)]}        |{pos[(0, 2)]}        |
|         |         |         |
-------------------------------
|         |         |         |
|{pos[(1, 0)]}        |{pos[(1, 1)]}        |{pos[(1, 2)]}        |
|         |         |         |
-------------------------------
|         |         |         |
|{pos[(2, 0)]}        |{pos[(2, 1)]}        |{pos[(2, 2)]}        |
|         |         |         |
-------------------------------''')

    if result > 0:
        if player == "user":
            print("\nYou have won. Congrats")
            return False

        elif player == "computer":
            print("\nYou have lost. Best of luck next time")
            return False
    else:
        return True
        # if turn:
        #
        # else:
        #     choice = input("\nEnter the number in the box")
        #     print("choice : ", choice)
        #     main_game(choice)


def check_game(get_key, sign):

    count = 0
    x = get_key[0]
    y = get_key[1]

    if x == 0:
        if y == 0:
            if pos[(x, y)] == sign and pos[(x, y + 1)] == sign and pos[(x, y + 2)] == sign:
                count += 1
                print("match1")

            if pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x + 2, y)] == sign:
                count += 1
                print("match2")

            if pos[(x, y)] == sign and pos[(x + 1, y + 1)] == sign and pos[(x + 2, y + 2)] == sign:
                count += 1
                print("match3")

        if y == 1:
            if pos[(x, y)] == sign and pos[(x, y - 1)] == sign and pos[(x, y + 1)] == sign:
                count += 1
                print("match4")

            if pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x + 2, y)] == sign:
                count += 1
                print("match5")

        if y == 2:
            if pos[(x, y)] == sign and pos[(x, y - 1)] == sign and pos[(x, y - 2)] == sign:
                count += 1
                print("match6")

            if pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x + 2, y)] == sign:
                count += 1
                print("match 7")

            if pos[(x, y)] == sign and pos[(x + 1, y - 1)] == sign and pos[(x + 2, y - 2)] == sign:
                count += 1
                print("match 8")

    if x == 1:
        if y == 1:
            if (pos[(x, y)] == sign and pos[(x, y + 1)] == sign and pos[(x, y - 1)]) == sign:
                count += 1
                print("match9")

            if (pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x - 1, y)]) == sign:
                count += 1
                print("match10")

            if pos[(x, y)] == sign and pos[(x - 1, y - 1)] == sign and pos[(x + 1, y + 1)] == sign:
                count += 1
                print("match11")

            if pos[(x, y)] == sign and pos[(x - 1, y + 1)] == sign and pos[(x + 1, y - 1)] == sign:
                count += 1
                print("match12")

        if y == 0:
            if pos[(x, y)] == sign and pos[(x, y + 1)] == sign and pos[(x, y + 2)] == sign:
                count += 1
                print("match13")

            if pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x - 1, y)] == sign:
                count += 1
                print("match14")

        if y == 2:
            if pos[(x, y)] == sign and pos[(x, y - 1)] == sign and pos[(x, y - 2)] == sign:
                count += 1
                print("match15")

            if pos[(x, y)] == sign and pos[(x + 1, y)] == sign and pos[(x - 1, y)] == sign:
                count += 1
                print("match16")

    if x == 2:
        if y == 0:
            if pos[(x, y)] == sign and pos[(x, y + 1)] == sign and pos[(x, y + 2)] == sign:
                count += 1
                print("match17")

            if pos[(x, y)] == sign and pos[(x - 1, y)] == sign and pos[(x - 2, y)] == sign:
                count += 1
                print("match18")

            if pos[(x, y)] == sign and pos[(x - 1, y + 1)] == sign and pos[(x - 2, y + 2)] == sign:
                count += 1
                print("match19")

        if y == 1:
            if pos[(x, y)] == sign and pos[(x, y - 1)] == sign and pos[(x, y + 1)] == sign:
                count += 1
                print("match20")

            if pos[(x, y)] == sign and pos[(x - 1, y)] == sign and pos[(x - 2, y)] == sign:
                count += 1
                print("match21")

        if y == 2:
            if pos[(x, y)] == sign and pos[(x, y - 1)] == sign and pos[(x, y - 2)] == sign:
                count += 1
                print("match22")

            if pos[(x, y)] == sign and pos[(x - 1, y)] == sign and pos[(x - 2, y)] == sign:
                count += 1
                print("match23")

            if pos[(x, y)] == sign and pos[(x - 1, y - 1)] == sign and pos[(x - 2, y - 2)] == sign:
                count += 1
                print("match24")

    return count


def main_game(position_number):
    global turn
    global pos
    game_status = True
    # print(position_number)
    for key in pos.keys():
        # print(key)
        if pos[key] == position_number:
            # print(f"{key} : {position_number}")
            if turn:
                pos[key] = '#'
                turn = False
                result = check_game(key, '#')
                game_status = display(result, "computer")

            else:
                pos[key] = 'x'
                turn = True
                result = check_game(key, 'x')
                print(result)
                game_status = display(result, "user")
    return game_status


def reset():
    global pos
    global turn
    pos = {(0, 0): '1', (0, 1): '2', (0, 2): '3',
           (1, 0): '4', (1, 1): '5', (1, 2): '6',
           (2, 0): '7', (2, 1): '8', (2, 2): '9'}
    turn = True  # If true it's the game of computer else it is user's game turn


def game_init():
    # game_status = True

    used_number = []
    while True:
        game_count = 1

        if turn:
            game_count += 1
            print(game_count)
            while True:
                position_number = random.randint(1, 9)
                if position_number in used_number:
                    continue
                used_number.append(position_number)
                break
            game_status = main_game(str(position_number))

        else:
            print(game_count)
            game_count += 1
            choice = input("Enter the box number to print X")
            game_status = main_game(choice)

        if not game_status:
            print("Game Over")
            choice = input("Do you want to continue? Enter 'y' to continue or any key to exit : ")
            if choice == 'y':
                reset()
            else:
                break
        else:
            if game_count == 9:
                print("It's a draw")
                choice = input("Do you want to continue? Enter 'y' to continue or any key to exit : ")
                if choice == 'y'
                    reset()
                else:
                    break

            else:
                continue


pos = {(0, 0): '1', (0, 1): '2', (0, 2): '3',
       (1, 0): '4', (1, 1): '5', (1, 2): '6',
       (2, 0): '7', (2, 1): '8', (2, 2): '9'}
turn = True  # If true it's the game of computer else it is user's game turn


game_init()
