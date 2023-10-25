import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def total_t(xc):
    to = 0
    for t in xc:
        to += t
    return to


cond = True


while cond:

    if input("type 'y' to play: ").lower() == "y":
        # clear the terminal
        cond = True
    else:
        cond = False
        break

    ycards = []
    dcards = []

    ycards = random.choices(cards, k=2)
    dcards = random.choices(cards, k=2)

    ytotal = total_t(ycards)
    dtotal = total_t(dcards)

    print(f"Your cards: {ycards}, current score: {ytotal}")
    print(f"computer's first card: {dcards[0]}")

    cond2 = True
    while cond2:
        x = input("type 'y' to get another card, type 'n' to pass: ")

        if x == "y":
            ycards.append(random.choice(cards))
            ytotal = total_t(ycards)

            print(f"Your cards: {ycards}, current score: {ytotal}")
            print(f"computer's first card: {dcards[0]}")

            if ytotal > 21:
                print(
                    f"your final hand: {ycards}, final score: {ytotal}\ncomputer's final hand {dcards}, final score {dtotal}\nyou went over, you lost")
                cond2 = False

            else:
                if dtotal < 17:
                    dcards.append(random.choice(cards))
                    dtotal = total_t(dcards)
                    if dtotal > 21:
                        print(
                            f"you win, your cards: {ycards}, your total: {ytotal}\n computers cards: {dcards}, copmputers total: {dtotal}")
                        cond2 = False

        elif x == "n":
            cond2 = False
            if ytotal > dtotal:
                print(
                    f"you win, your cards: {ycards}, your total: {ytotal}\n computers cards: {dcards}, copmputers total: {dtotal}")
            elif ytotal == dtotal:
                print(
                    f"Draw, your cards: {ycards}, your total: {ytotal}\n computers cards: {dcards}, copmputers total: {dtotal}")
            else:
                print(
                    f"you lost, your cards: {ycards}, your total: {ytotal}\n computers cards: {dcards}, copmputers total: {dtotal}")
