import art
import colors


def start():
    print(colors.yellow + art.chest + colors.reset)
    print("Welcome to Treasure Island.".center(80))
    print("Your mission is to find the treasure.".center(80))


def win(celebration, art):
    print(f"""{art.celebration}
                OOOOoooHuu! {colors.green}You win!{colors.reset}""")


left_right = input(f"""You're at a cross road. Where do you want to go?
        Type "left" or "right"\n """).strip().lower()

if left_right == "left":
    swim_boat = input(f"""You found a lake! 
        Do you want to "swim" or "wait" for a boat?\n""").strip().lower()

    if swim_boat in ("wait", "boat"):
        which_door = (
            input(f"""You got to the other side! In front of you there's three doors.
            {art.door}
            One {colors.red}red{colors.reset}, one {colors.yellow}yellow{colors.reset}
            and one {colors.green}green{colors.reset}.
            Which door do you choose?
            """).strip().lower()
        )

        if which_door == "red":
            print(f""" {art.cerberus}
                  Oh no! You found Cerberus.
                  {colors.red}Game over!{colors.reset}""")

        elif which_door == "yellow":
            print(f""" {art.celebration}
                  OOOOoooHuu! {colors.green}You win!{colors.reset}""")

        elif which_door == "green":
            print(f"""{art.goblin}
                  Eaten by goblins!
                  {colors.red}Game over!{colors.reset}""")

        else:
            print(f"""{art.snail}
                  {colors.red}Game over!{colors.reset}""")

    else:
        print(f"""{art.nessie}
              Attacked by Nessie!
              {colors.red}Game over!{colors.reset}""")

else:
    print(f"""{art.mary_poppins}
          You found Mary Poppins and she's not happy with you!
          {colors.red}Game over!{colors.reset}""")
