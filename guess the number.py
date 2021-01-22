# while(True):
#     n=81
#     print("The number which you have to guess is between 'a' and 'b'")
#     print("player Three will give u 'a' and 'b' and player1 and player2 will have to guess the number ")
#     a=int(input("Enter 'a'"))
#     b=int(input("Enter 'b'"))
#     print("player Three work has been done")
#     print("Now its player One turn to guess the number")
#     print(f"The number is between {a} and {b}")
#     print("The no of chances are only 10")
#
#
#     i=1
#     while i<=10:
#
#         p_one=int(input("Guess the number"))
#         if p_one<a:
#             print(f"abe chutiye ho ka ....jab player Three ne bola hai ki number is between {a} and {b},toh {a} se chota number kaahe daal rahe be")
#         elif p_one>b:
#             print(f"abe chutiye ho ka ....jab player Three ne bola hai ki number is between {a} and {b},toh {b} se bada number kaahe daal rahe be")
#         elif p_one<n:
#             print("The number you have entered is smaller than the number you have to guess.....Try agian")
#         elif p_one>n:
#             print("The number you have entered is biggeer than the number you have to guess......Try again")
#         else:
#             print("you have guessed the right number")
#             p_one_chances=f"you used {i} chances"
#             print(p_one_chances)
#             break
#
#         p_one_chances=f"you used {i} chances"
#         print(p_one_chances)
#         print(f"The no of chances left is {10-i}")
#         if i>=10:
#             print(f"player one was unable to guess the number ,player one has used all his {i} chances")
#
#             break
#
#         i=i+1
#
#
#     print(".......")
#     print(".......")
#     print(".......")
#     print(".......")
#     print(".......")
#
#
#
#
#     print("Now its player Two turn to guess the number")
#     i=1
#     while i<=10:
#         p_two=int(input("Guess the number"))
#         if p_two<a:
#             print(f"abe chutiye ho ka ....jab player Three ne bola hai ki number is between {a} and {b},toh {a} se chota number kaahe daal rahe be")
#         elif p_two>b:
#             print(f"abe chutiye ho ka ....jab player Three ne bola hai ki number is between {a} and {b},toh {b} se bada number kaahe daal rahe be")
#         elif p_two<n:
#             print("The number you have entered is smaller than the number you have to guess.....Try agian")
#         elif p_two>n:
#             print("The number you have entered is biggeer than the number you have to guess......Try again")
#         else:
#             print("you have guessed the right number")
#             p_two_chances=f"you used {i} chances"
#             print(p_two_chances)
#             break
#
#         p_two_chances = f"you used {i} chances"
#         print(p_two_chances)
#         print(f"You have used {i} chances")
#         print(f"The no of chances left is {10-i}")
#         if i>=10:
#             print(f"player Two was unable to guess the number ,player Two has used all his {i} chances")
#
#             break
#
#         i=i+1
#     # print(f"player Two was unable to guess the number ,player two have used {i-1} chances")
#
#
#     if p_one_chances>p_two_chances:
#         print("congrats, player Two, you have won the game")
#     elif p_two_chances>p_one_chances:
#         print("congrats,player One has won the game")
#     else:
#         print("its a tie_breaker......do you want to play one more game")
#     print("To continue the game press 'c',to quit the game press any key other than c")
#     game=input("Enter your choice")
#     if game=="c":
#         continue
#     else:
#         break





















import random


def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g1 > g2:
        print("Player 2 won the match!\n")

    else:
        print("Its a Tie!\n")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")