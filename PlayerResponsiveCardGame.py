###Dependencies
import random
Ace = 20
Jack = 11
Queen = 12
King = 13

###CardLists
Deck = [Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King]
###Functions
def main():
    while True:
        DecIn = input("Would you like to draw a card? Y/N?")
        uscore = 0
        nscore = 0
        if DecIn == "Y":
            ###RandomChoiceVars
            rNPC = random.choice(Deck)
            rUSER = random.choice(Deck)
            ###StartingScores
                    ``
            #ARGS
            if rNPC > rUSER:
                print(rNPC, ">" , rUSER)
                print("You lost, User!") 
                nscore += 1
                print("The score is: User: " + str(uscore) + " and NPC: " + str(nscore))
            elif rUSER > rNPC:
                print(rNPC, "<" , rUSER)
                print("You won, User!")
                uscore += 1
                print("The score is: User: " + str(uscore) + " and NPC: " + str(nscore))
            elif rUSER == rNPC:
                print(rNPC, "=" , rUSER)
                continue
        else:
            break
main()