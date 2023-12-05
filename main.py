#     With this code, you'll be using 5 coins to keep track of 5
# consecutive accurate run throughs of the excerpt of music you're
# practicing. If you succeed, the tempo increases. If you fail, the
# coins flip and you restart.
#
#     Run this code when you have your instrument and a metronome. Know
# what tempo you can accurately play the section of music you're
# practicing.

import os
import msvcrt

num_coins = 5
coins = ['heads'] * num_coins
correct_attempts = 0

current_tempo = int(input("What tempo would you like to start at? "))
tempo_increase = int(input("How many beats per minute would you like to increase the metronome when the coins reset? "))
os.system('cls')

print(f"Your current tempo is {current_tempo} bpm. Flip all 5 coins to increase the tempo by {tempo_increase} bpm.")
print("Press any key to continue...")
msvcrt.getch()
os.system('cls')

def play_section():
    print(coins)
    played_correctly = input("Did you play the section correctly? Type 'Y' or 'N'.").upper()
    if played_correctly == "Y":
        return True
    else:
        return False


def flip_coin(coin_index):
    coins[coin_index] = 'tails'


def reset_coins():
    for i in range(num_coins):
        coins[i] = 'heads'


def main():
    global correct_attempts, current_tempo
    while True:
        if all(coin == 'tails' for coin in coins):
            current_tempo += tempo_increase
            correct_attempts = 0
            reset_coins()
            print(f"Success! Increase tempo to {current_tempo} bpm.")
            print("Press any key to continue...")
            msvcrt.getch()
            os.system('cls')

        if play_section():
            correct_attempts += 1
            print('Correct!')
            flip_coin(correct_attempts - 1)
            os.system('cls')

        else:
            os.system('cls')
            print('Mistake! Starting over.')
            correct_attempts = 0
            reset_coins()


if __name__ == "__main__":
    main()

# Good musicians practice until they can play it right. Great musicians practice until they can't play it wrong.
