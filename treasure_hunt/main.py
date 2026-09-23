import art
import colors


def ask_choice(prompt):
    return input(prompt).strip().lower()


def game_over(message, artwork):
    print(f"""
{artwork}
{message}
{colors.red}Game over!{colors.reset}
""")


def show_intro():
    print(colors.yellow + art.chest + colors.reset)
    print("Welcome to Treasure Island.".center(80))
    print("Your mission is to find the treasure.\n".center(80))


def choose_door():
    which_door = ask_choice(
        f"""You got to the other side! In front of you there's three doors.
{art.door}
One {colors.red}red{colors.reset}, one {colors.yellow}yellow{colors.reset}
and one {colors.green}green{colors.reset}.
Which door do you choose? """
    )

    if which_door == "red":
        game_over("Oh no! You found Cerberus.", art.cerberus)

    elif which_door == "yellow":
        print(f"""
{art.celebration}
OOOOoooHuu! {colors.green}You win!{colors.reset}
""")

    elif which_door == "green":
        game_over("Eaten by goblins!", art.goblin)

    else:
        game_over("You opened a strange door and vanished.", art.snail)


def choose_lake_action():
    swim_boat = ask_choice("""You found a lake!
Do you want to "swim" or "wait" for a boat? """)

    if swim_boat in ("wait", "boat"):
        choose_door()
    elif swim_boat == "swim":
        game_over("Attacked by Nessie!", art.nessie)
    else:
        game_over("You hesitated for too long.", art.nessie)


def choose_path():
    left_right = ask_choice("""You're at a cross road. Where do you want to go?
Type "left" or "right": """)

    if left_right == "left":
        choose_lake_action()
    elif left_right == "right":
        game_over(
            "You found Mary Poppins and she's not happy with you!",
            art.mary_poppins,
        )
    else:
        game_over("You got lost because you chose an invalid path.", art.mary_poppins)


def main():
    show_intro()
    choose_path()


if __name__ == "__main__":
    main()
