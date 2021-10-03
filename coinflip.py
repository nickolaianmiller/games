import random
import sys

correct = 0
total = 0



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
    global correct
    global total
    def coin_art():
        if coin == 'Heads':
            print("""
            _.-'~~`~~'-._
         .'`  B   E   R  `'.
        / I               T \\
      /`       .-'~"-.       `\\
     ; L      / `-    \      Y ;
    ;        />  `.  -.|        ;
    |       /_     '-.__)       |
    |        |-  _.' \ |        |
    ;        `~~;     \\\\        ;
     ;  INGODWE /      \\\\)P    ;
      \  TRUST '.___.-'`"     /
       `\                   /`
         '._   1 9 9 7   _.'
            `'-..,,,..-'`""")
        else:
            print("""
            _.-'~~`~~'-._
         .'`  A   I   L  `'.
        / T               S \\
      /`                     `\\
     ;        ________         ;
    ;        |__    __|         ;
    |           |  |            |
    |           |  |            |
    ;           |__|            ;
     ;  INGODWE           P    ;
      \  TRUST                /
       `\                   /`
         '._   1 9 9 7   _.'
            `'-..,,,..-'`
            """)
    guess = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChoose a side (H) or (T): ')
    if guess.upper() == 'H':
        guess = 'Heads'
    elif guess.upper() == 'T':
        guess = 'Tails'
    else:
        print('Invalid character please enter (H) or (T)')
        play()
    coin = random.choice(['Heads', 'Tails'])
    if guess == coin:
        correct += 1
        total += 1
        coin_art()
        print('Congrats it was ' + coin + '!')
        print(f'You guessed {correct}/{total} correct ({100*correct/total}%)')
        play_again()
    else:
        total += 1
        coin_art()
        print('Sorry it was ' + coin + '.')
        print(f'You guessed {correct}/{total} correct ({100*correct / total}%)')
        play_again()

play()