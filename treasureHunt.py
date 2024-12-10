print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

#choose a direction to go 
                   
direction = input("Which direction do you want to go? (left, right) ")

if direction.lower() == "left":
    print("Good you have cleared the first level.....!!")
    
    #choose a option to go further
    direction_further = input("Now you have a lake in front of you you need to cross it to reach the next level so what do you wnat to do ..?(1.if you want to swim give \"swim\" \n 2.if you want to wait for boat give \"boat\" )")
    
    if direction_further.lower() == "boat":
        print("Congratulations, you have succesfully crossed the lake!")
    else:
        print("You chose swim so.\nYou encounter a water monster.")
        print("Game Over!")

    doorSelect=input("you have 3 doors in front of you which you want to select(red,blue,green) : ")
    
    if doorSelect.lower() == "red":
        print("Congratulations, you have found the treasure!")
    elif doorSelect.lower() == "blue":
        print("Game Over!")
    elif doorSelect.lower() == "green":
        print("Game Over!")
    else:
        print("Invalid Option!")
elif direction.lower() == "right":
    print("You chose to go Right.\nYou encounter a monster.")
    print("Game Over!")
else:
    print("You chose to go Someother Way.\nYou encounter a monster.")
    print("Game Over!")