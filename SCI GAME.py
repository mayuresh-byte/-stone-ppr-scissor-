import random
def SPSG():
    lst = ["STONE" , "PAPER" , "SCISSOR"]
    user_score = 0
    computer_score = 0
    for i in range(0,11):
        comp = random.choice(lst)
        user = input("enter one of the choice from STONE/PAPER/SCISSOR TO GIVE DEFEAT TO COMPUTER ").capitalize()
        if (comp == user):
            print("OOOOOOPS !!! TRY AGAIN MATCH DRAWN ")

        elif(comp == "STONE" and user == "PAPER"):
            print("YOU WON THIS ROUND ")
            user_score = user_score + 1

        elif(comp == "STONE" and user == "SCISSOR"):
            print("OOOOOOPS !!! COMPUTER WON THIS ROUND ")
            computer_score = computer_score + 1

        elif(comp == "PAPER" and user == "STONE"):
            print("OOOOOOPS !!! COMPUTER WON THIS ROUND ")
            computer_score = computer_score + 1

        elif(comp == "PAPER" and user == "SCISSOR"):
            print("YOU WON THIS ROUND ")
            user_score = user_score + 1

        elif(comp == "SCISSOR" and user == "PAPER"):
            print("OOOOOOPS !!! COMPUTER WON THIS ROUND ")
            computer_score = computer_score + 1

        elif(comp == "SCISSOR" and user == "STONE"):
            print("YOU WON THIS ROUND ")
            user_score = user_score + 1
        else:
            print("ENETER VALID KEY")

        while(i==5):
            if(computer_score>user_score):
                print("you are going to loose")
            else:
                print('KEEP IT UP CHAMP')


    print("10 ROUNDS OF THE GAME ARE OVER ....AND THE RESULT IS HERE...")
    print("THE TOTAL SCORE OF THE COMPUTER IS ", computer_score)
    print("THE TOTAL SCORE OF THE USER IS ", user_score)
    if(computer_score>user_score):
        print("OOOPSSS !!! SORRY YOU LOST THE MATCH....\n BETTER LUCK NEXT TIME CHAMP!!")

    elif(computer_score == user_score):
        print("OOOPSSS !!! SORRY YOU TIED THE  MATCH....\n BETTER LUCK NEXT TIME CHAMP!!")

    else:
        print("wohoooo !!! CONGRATS YOU WON THE MATCH...")

SPSG()





