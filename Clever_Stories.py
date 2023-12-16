#added while loop, added decision to continue or not the program
active = True
while (active == True):
    adjective = input("Plase type an adjective: ")
    animal = input("Please type an animal: ")
    verb1 = input("Please type a verb: ")
    exclamation = input("Please type an exclamation: ")
    verb2 = input("Please type another verb: ")
    verb3 = input("Please type another verb: ")
    profession = input("Please type a profession: ")
    if (profession[0]=="a" or profession[0]=="A" or profession[0]=="e" or profession[0]=="E" or profession[0]=="i" or profession[0]=="I" or profession[0]=="u" or profession[0]=="U"):
        arcticle = "an"
    else:
        arcticle = "a"
    phrase = input("Please type a short phrase: ")
    verbing = input("Please type a verb in gerund (ing): ")
    print('\nYour story is: \n')
    print('The other day, I was really in trouble. It all started when I saw a very')
    print(adjective.lower(), animal.lower(), verb1.lower(),'down the hallway."'+exclamation.capitalize()+'!" I yelled. But all') 
    print('I could think to do was to',verb2.lower(),'over and over. Miraculously,')
    print('that caused it to stop, but not before it tried to',verb3.lower()) 
    print('right in front of my family. Suddenly',arcticle.lower(), profession.lower(),'entered right in')
    print('and sayed: "'+phrase.capitalize()+'!" And we all started',verbing.lower())
    decision = input("\nDo you wish to continue? ")
    if (decision == "Yes" or decision == "yes"):
        active = True
    elif (decision == "No" or decision == "no"):
        active = False
    else:
        print("Sorry you didn't choose")
        active = False
