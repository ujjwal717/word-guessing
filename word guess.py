import random

user_name = input("Please Enter your name :- ")

print(f"Hello {user_name} ")

word_basket = ['banana', 'apple', 'orange', 'pineapple', 'grapes']
rand = random.choice(word_basket)

print(f"{user_name}, The word is {len(rand)} characters long and is a fruit ")

chances = len(rand)

print(f'You have {chances} chances to guess the correct word! Best of Luck :) ')


failed_attempt = 0

if __name__ == '__main__':

    while chances > 0:

        guess = input("\nEnter the character that you guess will be in the word :- ")


        if guess in rand[::1]:
            chances -= 1
            print(f"You guessed a correct character and is present at {rand.index(guess)} position of the word ")

        else:
            chances -= 1
            print("You guessed a wrong character, try again :) ")
            failed_attempt += 1

    if failed_attempt == 0:
        print(f"\n\nCongratulations {user_name}, you guess the correct word that is {rand} :)")
    else:
        print(f"\n\nYou guessed wrong word, Better luck next time {user_name} :) ")

