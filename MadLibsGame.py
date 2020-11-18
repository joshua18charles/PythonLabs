#Mad Libs Game
#The purpose of this script is to have the user input the different data and have it append to a roster

#Roster must be entered in this order: Name, Postion, Height, Weight
roster = []
name = ''
postion = ''
height = 0.0
weight = 0


patrickMahomes = ['Patrick Mahomes', 'QB', 6.4, 225]
roster.append(patrickMahomes)
#print(roster)

def userInput ():
    name = input("Enter your the name of the player: ")
    position = input('Enter your two letter position: ')
    height = float(input("(ex. 6'2 = 6.2) Enter your height : "))
    weight = int(input("(ex. 125lbs = 125) Enter your weight : "))

def playerstats(n, p, h, w):
    print("Coach: Who's next?")
    print("Player: " + n)
    print("Coach: What position do you play?")
    print("Player: I'm a " + p + ', coach.')
    print("Coach: Step on the scale, "+ n + ', we are going to measure your height and weight')
    print("Assistant coach: " + h, w)
    print('Thanks,' + n + ', get your pads and head to the locker room.')


#playerstats(name, position, height, weight)
#print(playerstats)

#def main():
userInput()
print("Today we are going to gather our roster information for the team website.\n Once you get your height and weight recorded, head to the locker room")
print(name)
    #playerstats(n = name, p = position, h = height, w = weight)
#main()


