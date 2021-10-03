import random
import sys

user_score = 0
cpu_score = 0

def play_again():
    pa = ''
    while pa.upper() != 'Y' or pa.upper() != 'N':
        pa = input('Would you like to play again? (Y) (N)\n')
        if pa.upper() == 'Y':
            play()
        elif pa.upper() == 'N':
            print('It has been fun! See you again soon.')
            sys.exit()
        else:
            print('Invalid input, please enter either Y or N...')

def play():
    global user_score
    global cpu_score

    user = input("Pick one:\n'r' for rock\n'p' for paper\n's' for scissors\n")
    computer = random.choice(['rock', 'paper', 'scissors'])
    if user.lower() == 'r':
        user = 'rock'
    elif user.lower() == 'p':
        user = 'paper'
    elif user.lower() == 's':
        user = 'scissors'
    else:
        print('Invalid input, please enter either r, p, or s...')
        print(play())
    def rps_art():
        userlist = [
            """
██████╗░░█████╗░░█████╗░██╗░░██╗         _______
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝     ---'   ____)
██████╔╝██║░░██║██║░░╚═╝█████═╝░           (_____)
██╔══██╗██║░░██║██║░░██╗██╔═██╗░           (_____)
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗           (____)
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝     ---.__(___)
            """,
            """
██████╗░░█████╗░██████╗░███████╗██████╗░          _______
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗     ---'    ____)____
██████╔╝███████║██████╔╝█████╗░░██████╔╝                ______)
██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗               _______)
██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║              _______)
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝     ---.__________)
            """,
            """
░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗         _______
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝     ---'   ____)____
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░               ______)
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗            __________)
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝           (____)
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░     ---.__(___)
            """
        ]
        if user == 'rock':
            print(userlist[0])
        elif user == 'paper':
            print(userlist[1])
        else:
            print(userlist[2])
        print("""
██╗░░░██╗░██████╗
██║░░░██║██╔════╝
╚██╗░██╔╝╚█████╗░
░╚████╔╝░░╚═══██╗
░░╚██╔╝░░██████╔╝
░░░╚═╝░░░╚═════╝░
""")
        cpulist = ["""
  _______         ██████╗░░█████╗░░█████╗░██╗░░██╗
 (____   '---     ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
(_____)           ██████╔╝██║░░██║██║░░╚═╝█████═╝░
(_____)           ██╔══██╗██║░░██║██║░░██╗██╔═██╗░
 (____)           ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
  (___)__.---     ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
""",
                   """
       _______          ██████╗░░█████╗░██████╗░███████╗██████╗░
  ____(____    '---     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 (______                ██████╔╝███████║██████╔╝█████╗░░██████╔╝
(________               ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
  (_______              ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
    (__________.---     ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                   """,
                   """
       _______          ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
  ____(____   '---     ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
 (______               ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
(__________            ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
      (____)           ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
       (___)__.---     ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
                   """
        ]
        if computer == 'rock':
            print(cpulist[0])
        elif computer == 'paper':
            print(cpulist[1])
        else:
            print(cpulist[2])
    rps_art()
    if user == computer:
        print('tie...we both chose ' + user)
        user_score += 1
        cpu_score += 1
        print(f'The current score is {user_score} to you and {cpu_score} to me.')
        play_again()
    if is_win(user, computer):
        user_score += 1
        print('I picked ' + computer + '... You won! Cannot believe you picked ' + user + '!')
        print(f'The current score is {user_score} to you and {cpu_score} to me.')
        play_again()
    print('Muahahaha I chose ' + computer + '. You lose!')
    cpu_score += 1
    print(f'The current score is {user_score} to you and {cpu_score} to me.')
    play_again()

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

play()

