import helpers as hp
import time
from pyfiglet import Figlet

def printMessage(question, font='term', answer=None):
    #possible fonts: #term #threepoint
    f = Figlet(font=font)
    hp.clr()
    time.sleep(0.8)
    print("\n\n\n\n\n\n\n")
    for x in f.renderText(question).split("\n"):
        print(x.center(hp.terminal_size()), sep="\n")
        print("\n")
        time.sleep(0.6)

    if answer:
        ans = input("\t\t\t\t\t\t\t---> Enter your answer:")
        return ans

    return ""

def printAscii(ascii):
    for row in ascii.split("\n"):
        print(row.center(hp.terminal_size()))

def runAll():
    from termcolor import colored

    text1 = "He loves tea but he hates birthdays\n" \
            "So let's make this day fun with some prose\n" \
            "Now he must solve clues to get his gift\n" \
            "With the help of all the stuff that he knows..."
    printMessage(text1)
    printAscii(
        " (  )   (   )  ) \n"
        " ) (   )  (  ( \n"
        " ( )  (    ) ) \n"
        " _____________ \n"
        "   <_____________> ___ \n"
        "   |             |/ _ \ \n"
        "    |              | | | \n"
        "    |              |_| | \n"
        "___|             |\___/ \n"
        "/   \___________/    \ \n"
        "\_____________________/ \n"
    )
    time.sleep(7)

    text2 = "'Twas the year man landed on the moon\n" \
            "The world of software was given another boon\n" \
            "With the blessings of this Great God Linus,\n" \
            "Let's begin your birthday game, Your Highness!\n"
    printMessage(text2)
    printAscii(""
          "           .----.\n"
          ".---------. | == | \n"
          "|.-\"\"\"\"\"-.| |----| \n"
          "||       || | == | \n"
          "||       || |----| \n"
          "|'-.....-'| |::::| \n"
          "`\"\")---(\"\"` |___.| \n"
          "/:::::::::::\ \" _  \" \n"
          "/:::=======:::\`\`\ \n"
          "`\"\"\"\"\"\"\"\"\"\"\"\"\"`  '-'")
    time.sleep(7)

    text3 = "A cry for help he sent out to his fellow coders\n" \
            "To assist him in the birth of a new creation\n" \
            "It's your favourite OS, yes,\n" \
            "But to call it ____ was his original intention"
    answer = printMessage(text3, answer=1)
    while answer.lower() != "Freax".lower():
        answer = input("\n\t\t\t\t\tWrong Answer! Try Again:")
    print("\n")
    print(colored("Correct!".center(hp.terminal_size()), 'green'))
    time.sleep(1)

    text4 = "This goes by the name Super Daemon\n" \
            "The kernel, without it, is just hell\n" \
            "(sysinit, init, inetd, proc) \n" \
            "To get ahead, please choose well."
    answer = printMessage(text4, answer=1)
    while answer.lower() != "init".lower():
        answer = input("\n\t\t\t\t\tWrong Answer! Try Again:")
    print("\n")
    print(colored("Correct!".center(hp.terminal_size()), 'green'))
    time.sleep(1)

    text5 = "Linux is one of a kind, you say?\n" \
            "Well not quite, my man!\n" \
            "It's a Swiss brand too, and they make these\n" \
            "Tell the name of the product, if you can!"
    answer = printMessage(text5, answer=1)

    while(1):
        flag = False
        for word in answer.split(" "):
            if word.lower() in ["washing", "powder", "detergent", "laundry", "dishwasher", "wash"]:
                flag = True
                break
            else:
                answer = input("\n\t\t\t\t\tWrong Answer! Try Again:")
        if flag:
            break
    print("\n")
    print(colored("Correct!".center(hp.terminal_size()), 'green'))
    time.sleep(1)

    text6 = "Who doesn't love Linux's quirky commands?\n" \
            "You have love, sl, cowsay and ifup\n" \
            "Well, there's this one that prints large text\n" \
            "It's also where you go when you wake up :D"
    answer = printMessage(text6, answer=1)
    while answer != "toilet":
        answer = input("\n\t\t\t\t\tWrong Answer! Try Again:")
    print("\n")
    print(colored("Correct!".center(hp.terminal_size()), 'green'))
    time.sleep(1)

    text7 = "And now I reveal the final clue\n" \
            "It is naturally all about me!\n" \
            "The command refers to intermediate pipeline extraction\n" \
            "But also the one you love, you see... "
    answer = printMessage(text7, answer=1)
    while answer != "tee":
        answer = input("\n\t\t\t\t\tWrong Answer! Try Again:")
    print("\n")
    print(colored("Congratulations! You made it.".center(hp.terminal_size()), 'green'))
    time.sleep(1)