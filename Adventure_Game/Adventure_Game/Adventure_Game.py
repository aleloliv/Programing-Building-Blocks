#defined a function to compare the choices that the user makes with the options given to him and assign a variable with the choice made. inicialized a dictionary containing many variables to hold the choices made by the user. The story was improved but not finished.

def make_choice(options, choices): #The make_choice() function takes in two arguments: options, which is a list of strings representing the available options, and choices, which is a dictionary that maps the choices made so far to their corresponding option. The function returns the user's selected option.
    _choice = None #Initializes the _choice variable to None
    while not _choice: #enters a while loop that continues until a valid choice is made by the user
        user_input = input(f"Please select an option from {options}: ") #the function prompts the user to input a choice from the available options
        user_input = user_input.strip().lower() #strips and converts the input to lowercase
        if not user_input: #performs some checks to ensure that the input is valid
            continue
        if user_input in options: #If the input is valid, _choice is set to the user's input, and the function modifies the choices dictionary by setting the value to None for all keys that do not correspond to _choice
            _choice = user_input
            keys_to_modify = []
            for key, value in choices.items():
                if value != _choice:
                    keys_to_modify.append(key)
            for key in keys_to_modify:
                choices[key] = None
        else:
            print(f"Invalid choice. Please select from {options}.") #If the input is invalid, the function prints an error message and continues the loop
    return _choice

choices = {} #The choices dictionary is initialized as empty, and then populated with 50 keys ("choice1" to "choice50"), that are the number of possible choices in the game, all mapped to None
for j in range(1, 50):
    choices[f"choice{j}"] = None

print("Welcome to Choices, the Game!")

_restart = True

while _restart:

    print("Part I\nAnd so it begins...")

    print("You see yourself on the third street again, not far from where you started this journey.")
    print("You reach to your pocket and find your PHONE and your WALLET. Which one do you pick? ")
    options = ["phone", "wallet"]
    choice = make_choice(options, choices)
    choices[choice] = choice

    _phase1 = True

    while _phase1:
        if (_restart == False):
            _phase1 = False
        if (choice.lower() == "phone"):
            print("You reach for your phone and see the time, it's already 12:10 a.m., you see there are no messages, you put the phone back into your pocket, then suddenly a strange man asks you if you have seen his daughter, a redhead girl wearing a yellow scarf. What will you say YES or NO?")
            options = ["yes", "no"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase1 = False
        elif (choice.lower() == "wallet"):
            print("You reach for your wallet and when you open it, you see there is your bus card with your picture on it, suddenly you hear the bus arriving at the bus stop, at the same moment you see a redhead girl wearing a yellow scarf running down the street, what do you do? Do you GET ON the bus or do you FOLLOW the girl?")
            options = ["get on", "follow"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase1 = False
        else:
            print("Please select PHONE or WALLET")
            options = ["phone", "wallet"]
            choice = make_choice(options, choices)
            choices[choice] = choice

    _phase2 = True

    while _phase2:
        if (_restart == False):
            _phase2 = False
        if (choice.lower() == "yes"):
            print("The man smiles and asks where have have you seen her? Was it DOWN the street or at the NEXT city?\n")
            options = ["down", "next"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase2 = False
        elif (choice.lower() == "no"):
            print("The man says 'If you see her, please call me.' and then he handles you a piece of paper with a phone number written on it. Suddenly, your phone starts ringing, do you ANSWER the phone or NOT?")
            options = ["answer", "not"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase2 = False
        elif (choice.lower() == "get on" or choice.lower() == "follow"):
            if (choice.lower() == "get on"):
                print("You enter the bus and use your bus card to go to the next city. When you arrive you bump into a girl, when you look at her you see that she has a red hair and wears a yellow scarf. What do you say, 'SORRY' or 'HOW did you get here?")
                options = ["sorry", "how"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase2 = False
            elif (choice.lower() == "follow"):
                print("You follow the girl. She turns a corner and you follow her, but when you turn and look at the street, you cannot see her anymore. You stop and try to look for her, but you don't find her anywhere. What will you do? KEEP searching, go BACK, or just STAY there?")
                options = ["keep", "back", "stay"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase2 = False
            else:
                print("Please select GET ON or FOLLOW.")
                options = ["get on", "follow"]
                choice = make_choice(options, choices)
                choices[choice] = choice
        else:
            print("Please select YES or NO")
            options = ["yes", "no"]
            choice = make_choice(options, choices)
            choices[choice] = choice

    print ("Part II\n")

    _phase3 = True

    while _phase3:
        if (_restart == False):
            _phase3 = False
        if (choice.lower() == "down"):
            print("You say she went down the street. The man thanks you and starts walking down the street. When he turns his back to you, you notice a strange symbol on his coat: a broken hourglass in the center of a gear. What will you do? FOLLOW the man, STAY where you are, or PUNCH the man?")
            options = ["follow", "stay", "punch"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase3 = False
        elif (choice.lower() == "next"):
            print("You tell the man the girl is in the next city. He thanks you and waits by your side for the bus to arrive. What will you do? WAIT for the bus in silence, GO down the street, or TALK to the man?")
            options = ["wait", "go", "talk"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase3 = False
        elif (choice.lower() != "down" or choice.lower() != "next"):
            if (choice.lower() == "answer"):
                print("You answer the phone and hear a feminine voice saying, 'Don't trust him!' What will you do? Say WHO's there? Say WHY not? Say OK?")
                options = ["who", "why", "ok"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase3 = False
            elif (choice.lower() == "not"):
                print("You don't answer the phone and wait for it to stop ringing. The man asks, 'Will you answer that?' What will you do? ANSWER or NOT?")
                options = ["answer", "not"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase3 = False
            elif (choice.lower() != "answer" or choice.lower() != "not"):
                if (choice.lower() == "sorry"):
                    print("The girl smiles and says 'No problem.' Suddenly, she hands you a piece of paper with an address written on it and says 'She's there, please help her.' What will you do? Go to the ADDRESS or NOT GO?")
                    options = ["address", "not go"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
                    _phase3 = False
                elif (choice.lower() == "how"):
                    print("You say 'How did you get here?'. She says 'There is no time, please come.' What will you do? Go WITH her or will you STAY THERE?")
                    options = ["with", "stay there"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
                    _phase3 = False
                elif (choice.lower() != "sorry" or choice.lower() != "how"):
                    if (choice.lower() == "keep"):
                        print("You keep looking for the girl. You look at the buildings arround you a see one with an open window, through the window you see there is a symbol on the wall, a broken hourglass in the middle of a gear. What will you do? Go INSIDE the building or KEEP searching?")
                        options = ["inside", "keep"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase3 = False
                    elif (choice.lower() == "back"):
                        print("You decide to go back where you were. When you get to the bus stop you see the girl there, waiting for the bus. What will you do? TALK TO the girl or FOLLOW HER?")
                        options = ["talk to", "follow her"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase3 = False
                    elif (choice.lower() == "stay"):
                        print("You decide to stay. Suddenly you hear a voice coming from your back 'Did you find her?' You turn arround and see a man runing in your direction. What will you do? Say NO, say YES and point to the building with an open window or say Why are you FOLLOWING her?")
                        options = ["no", "yes", "following"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase3 = False
                    else:
                        print("Please select KEEP, BACK or STAY")
                        options = ["keep", "back", "stay"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                else:
                    print("Please select SORRY or HOW")
                    options = ["sorry", "how"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
            else:
                print("Please select ANSWER or NOT")
                options = ["answer", "not"]
                choice = make_choice(options, choices)
                choices[choice] = choice
        else:
            print("Please select DOWN or NEXT")
            options = ["down", "next"]
            choice = make_choice(options, choices)
            choices[choice] = choice

    _phase4 = True

    while _phase4:
        if (_restart == False):
            _phase4 = False
            break
        if (choice.lower() == "follow"):
            print("You begin following the man. He turns at the corner, when you follow him you see the man entering a building with an open window, What will you do? Go IN or NOT?")
            options = ["in", "not"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase4 = False
        elif (choice.lower() == "stay"):
            print("You decide to stay at the bus stop. When the bus arrive you see a redheaded girl getting out of the bus. What will you do? TALK to her or try to CALL the man?")
            options = ["talk", "call"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase4 = False
        elif (choice.lower() == "punch"):
            print("You punch the man in the head and he falls to the ground, unconsious. What will you do? SEARCH in his pockets or RUN away?")
            options = ["search", "run"]
            choice = make_choice(options, choices)
            choices[choice] = choice
            _phase4 = False
        elif (choice.lower() != "follow" or choice.lower() != "stay" or choice.lower() != "punch"):
            if (choice.lower() == "wait"):
                print("You decide to wait for the bus in silence. The man says 'Don't worry, we will find her.' What do you do? Say I hope you FIND her, or Why are you AFTER her?")
                options = ["find", "after"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase4 = False
            elif (choice.lower() == "go"):
                print("You decide to go down the street. When you turn the corner you see the same man as before waiting for you, he has some sort of a baton with a glowing light on the tip. He says: 'Why did you lie to me?' and he hits you with his baton, when the tip touches you, you see a great light blinding you totally.")
                _phase4 = False
            elif (choice.lower() == "talk"):
                print("You decide to talk to the man. What will you say? WHO are you? Who IS SHE? How can she BE everywhere at the same time?")
                options = ["who", "is she", "be"]
                choice = make_choice(options, choices)
                choices[choice] = choice
                _phase4 = False
            elif (choice.lower() != "wait" or choice.lower() != "go" or choice.lower() != "talk"):
                if (choice.lower() == "who"):
                    print("You say Who's there? And the girl replyes: 'My name is Alice, please meet me down the street and turn the corner.' She hangs up. What will you do? Go SEE her, or TELL the man about the call?")
                    options = ["see", "tell"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
                    _phase4 = False
                elif (choice.lower() == "why"):
                    print("You say Why not? And the girl replyes: 'Because he's trying to catch me, he may also try to harm you. Please meet me down the street and turn the corner.' She hangs up. What will you do? Go SEE her, or TELL the man about the call?")
                    options = ["see", "tell"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
                    _phase4 = False
                elif (choice.lower() == "ok"):
                    print("You say ok. The girl says 'Thank you. Meet me down the street and turn the corner.' She hangs up. What will you do? TELL the man about the call or TAKE the bus?")
                    options = ["tell", "take"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
                    _phase4 = False
                elif (choice.lower() != "who" or choice.lower() != "why" or choice.lower() != "ok"):
                    if (choice.lower() == "answer"):
                        print("You answer the phone and hear a feminine voice saying, 'Don't trust him!' What will you do? Say WHO's there? Or HANG up the phone?")
                        options = ["who", "hang"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase4 = True
                    elif (choice.lower() == "not"):
                        print("You ignore the phone and the man just walks away looking at his phone and calling someone. What will you do now? FOLLOW THE MAN or GO DOWN the street")
                        options = ["follow the man", "go down"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase4 = False
                    elif (choice.lower() != "answer" or choice.lower() != "not"):
                        if (choice.lower() == "address"):
                            print("You decide to go to the address. When you arrive at the building, you see it's a restaurant with a sign that reads 'The Timekeeper's Table'. As you approach the entrance, you notice two men in brown coats standing outside. They look at you suspiciously. What will you do? ENTER the building, try to enter through the SIDE?")
                            options = ["enter", "side"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                            _phase4 = False
                        elif (choice.lower() == "not go"):
                            print("You decide to not go to the address. You decide it's just best to go to your apartment and leave all this.\nTHE END")
                            _phase4 = False
                            _restart = False
                            break
                        elif (choice.lower() != "address" or choice.lower() != "not go"):
                            if (choice.lower() == "with"):
                                print("You decide to go with the girl. She brings you to an abandoned building. When you enter, the girl says: 'Thanks for coming with me, here take a seat.' She points you to a chair, you sit down and ask her what is happening and who she is. She responds: 'My name is Alice, and I'm a time traveler trying to find my father. But there's an organization after me, and I need your help.' What will you say? Will you offer to HELP her, ask about her FATHER, or GIVE UP?")                                
                                options = ["help", "father", "give up"]
                                choice = make_choice(options, choices)
                                choices[choice] = choice
                                _phase4 = False
                            elif (choice.lower() == "stay there"):
                                print("You hesitate between going with her or not, the girl looks at you and says, 'I thought you were going to help me.' Before you can respond, a man in a brown coat comes sprinting in your direction, yelling 'Gotcha!' He pulls a baton from his coat, and the tip of the baton starts to glow ominously.\nAs you watch in shock, the girl quickly reaches into her pocket and pulls out a small clock. With a deft click, she disappears into thin air. The man, in his frenzy, tries to strike at the girl with his baton, but she vanishes just in time, causing him to accidentally hit you instead.\nAs you reel from the blow, everything around you suddenly becomes a blinding white light.")
                                _phase4 = False
                            elif (choice.lower() != "with" or choice.lower() != "stay there"):
                                if (choice.lower() == "inside"):
                                    print("You make the decision to enter the building, and as you step inside, you immediately notice that there are a lot of people wearing brown coats adorned with a peculiar symbol - a broken hourglass in the middle of a gear. You try to move stealthily, but suddenly one of them catches sight of you and pulls out his baton, which begins to emit a blinding glow. Before you can react, the baton strikes you and everything around you is enveloped in a bright, blinding white light.")
                                    _phase4 = False
                                elif (choice.lower() == "keep"):
                                    print("You keep searching for a while longer, looking in every direction, trying to find any trace of the girl. As you turn a corner, you notice a dark alleyway that catches your attention. It seems like an unusual place for someone to go, but you decide to investigate. As you approach the alleyway, you see a strange man in a brown coat walking in your direction. He looks suspicious and starts to pick up his pace as he gets closer to you. What will you do? CONFRONT the man or HIDE in the shadows?")
                                    options = ["confront", "hide"]
                                    choice = make_choice(options, choices)
                                    choices[choice] = choice
                                    _phase4 = False
                                elif (choice.lower() != "inside" or choice.lower() != "keep"):
                                    if (choice.lower() == "talk to"):
                                        print("You approach the girl and strike up a conversation. She tells you that her name is Alice and she's a time traveler who's looking for her father. Apparently, he's been lost somewhere in the timestream, and she's been following clues to try and find him. But there's an organization out there that's been trying to catch her and reset her to her correct timeline. She thinks they might be onto her, and she needs your help. Will you HELP HER or NOT HELP HER?")
                                        options = ["help her", "not help her"]                                        
                                        choice = make_choice(options, choices)
                                        choices[choice] = choice
                                        _phase4 = False
                                    elif (choice.lower() == "follow her"):
                                        print("You decide to follow the girl once again. This time she seems to be aware of your presence and leads you to a hidden alleyway. She turns to you and says: 'Thanks for following me, I need your help. My name is Alice and I'm a time traveler trying to find my father. There is an organization after me, they want to reset me to my correct timeline, but that means I'll never be able to find my father. Will you help me?' What will you do? HELP HER or NOT HELP HER?")
                                        options = ["help her", "not help her"]
                                        choice = make_choice(options, choices)
                                        choices[choice] = choice
                                        _phase4 = False
                                    elif (choice.lower() != "talk to" or choice.lower() != "follow her"):
                                        if (choice.lower() == "no"):
                                            print("You say 'No, I didn't find her, sorry' to the man. He looks at you suspiciously and says 'Alright then, I'll keep looking' and runs past you. You watch him go. What will you do? FOLLOW THE MAN or GO HOME?")
                                            options = ["follow the man", "go home"]
                                            choice = make_choice(options, choices)
                                            choices[choice] = choice
                                            _phase4 = False
                                        elif (choice.lower() == "yes"):
                                            print("You say 'Yes, I saw her go in there' and point to the building with the open window. The man nods and runs towards the building. What will you do? Follow him into the BUILDING or GO HOME")
                                            options = ["building", "go home"]
                                            choice = make_choice(options, choices)
                                            choices[choice] = choice
                                            _phase4 = False
                                        elif (choice.lower() == "following"):
                                            print("You say 'Why are you following her?' The man stops in front of you and says 'That's none of your business. Just tell me where she went.' What will you do? Say she went into the BUILDING and when he goes in you follow him, or say No and try to PUNCH the man?")
                                            options = ["building", "punch"]
                                            choice = make_choice(options, choices)
                                            choices[choice] = choice
                                            _phase4 = False
                                        else:
                                            print("Please select NO, YES or FOLLOWING")
                                            options = ["no", "yes", "following"]
                                            choice = make_choice(options, choices)
                                            choices[choice] = choice
                                    else:
                                        print("Please select TALK TO or FOLLOW HER")
                                        options = ["talk to", "follow her"]
                                        choice = make_choice(options, choices)
                                        choices[choice] = choice
                                else:
                                    print("Please select INSIDE or KEEP")
                                    options = ["inside", "keep"]
                                    choice = make_choice(options, choices)
                                    choices[choice] = choice
                            else:
                                print("Please select WITH or STAY THERE")
                                options = ["with", "stay there"]
                                choice = make_choice(options, choices)
                                choices[choice] = choice
                        else:
                            print("Please select ADDRESS or NOT GO")
                            options = ["address", "not go"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                    else:
                        print("Please select ANSWER or NOT")
                        options = ["answer", "not"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                else:
                    print("Please select WHO, WHY or OK")
                    options = ["who", "why", "ok"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
            else:
                print("Please select WAIT, GO or TALK")
                options = ["wait", "go", "talk"]
                choice = make_choice(options, choices)
                choices[choice] = choice
        else:
            print("Please select FOLLOW, STAY or PUNCH")
            options = ["follow", "stay", "punch"]
            choice = make_choice(options, choices)
            choices[choice] = choice

    _phase5 = True

    while _phase5:
        if (_restart == False):
            _phase5 = False
            break
        if (choice.lower() == "stay there" or choice.lower() == "go" or choice.lower() == "inside"):
            _phase5 = False
            break
        if (choice.lower() == "in"):
            print("You make the decision to enter the building, and as you step inside, you immediately notice that there are a lot of people wearing brown coats adorned with a peculiar symbol - a broken hourglass in the middle of a gear. You try to move stealthily, but suddenly one of them catches sight of you and pulls out his baton, which begins to emit a blinding glow. Before you can react, the baton strikes you and everything around you is enveloped in a bright, blinding white light.")
            _phase5 = False
        elif (choice.lower() == "not"):
            print("You decide to not enter the building. But when you turn around to see where you are, you see another man wearing a brown coat holding a baton, he sayes: 'You shouldn't have come here.' Before you can react, the baton strikes you and everything around you is enveloped in a bright, blinding white light.")
            _phase5 = False
        elif (choice.lower() != "in" or choice.lower() != "not"):
            if (choice.lower() == "talk"):
                print("You approach the girl and introduce yourself. She tells you her name is Alice and that she's looking for her father. You ask her if she needs any help, and she nods her head. Suddenly, a man in a brown coat appears behind you and says, 'Come with me, Alice.' What will you do? STAND UP for Alice or LET her go with the man?")
                options = ["stand up", "let"]
                choice = make_choice(options, choices)
                choices[choice] = choice
            elif (choice.lower() == "call"):
                  print("You try to call the man but you only hear static. Suddenly, you see the same man in a brown coat approaching the bus stop. He sees the girl and start sprinting to your direction. He pulls a baton from his coat, and the tip of the baton starts to glow ominously.\nAs you watch in shock, the girl quickly reaches into her pocket and pulls out a small clock. With a deft click, she disappears into thin air. The man, in his frenzy, tries to strike at the girl with his baton, but she vanishes just in time, causing him to accidentally hit you instead.\nAs you reel from the blow, everything around you suddenly becomes a blinding white light.")
                  _phase5 = False
            elif (choice.lower() != "talk" or choice.lower() != "call"):
                if (choice.lower() == "search"):
                    print("You search in his pockets and you fund a baton in one of them. You see there is a button on the baton, when you press it the tip of the baton starts glowing. You touch the man with it and suddenly the man disappears. After that you see the bus ariving at the bus stop, you see a redhead girl dropping out of the, shw sees you and says: 'Thank you, I knew I could count on you!' You give her the baton and she pulls a small clock from her pocket. With a deft click, she disappears into thin air. Now all you have to do is go home.\n Congratulations!\nTHE END")
                    _phase5 = False
                    _restart = False
                elif (choice.lower() == "run"):
                    print("You decide to run away. You run so fast and so desperatly that you find yourself by your apartment, you are so tired that you only want to go in and sleep.\nTHE END")
                    _phase5 = False
                    _restart = False
                    break
                elif (choice.lower() != "search" or choice.lower() != "run"):
                    if (choice.lower() == "find"):
                        print("You decide to ask the man why he is after his daughter. The man looks at you with a stern expression and says, 'I'm not just 'after' her, I'm trying to protect her. She possesses unique powers that allow her to manipulate time, and there are forces that seek to exploit her abilities. I need to bring her back to her timeline to keep her safe and prevent any misuse of her powers.' I only want what's best for my daughter. Time travel is a dangerous ability, and if it falls into the wrong hands, it could have catastrophic consequences. Help me protect her and set things right. Will you HELP him or DECLINE to help him?")
                        options = ["help","decline"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase5 = False
                    elif (choice.lower() == "after"):
                        print("You contemplate your options and then ask him, 'Why are you after her? What's going on?' The man looks at you with a mix of desperation and determination in his eyes. He hesitates for a moment, but then decides to trust you. He takes a deep breath and starts explaining, 'My name is John. That girl you saw, she's my daughter, Alice. She possesses a unique ability to travel through time. But there's an organization, the one with the symbol of the broken hourglass and the men in brown coats, they're after her. They want to reset her to her correct timeline and erase her time-traveling abilities.' You listen intently, trying to absorb the gravity of the situation. John continues, 'Alice is on a mission to find me, her father, who got lost in time. She needs my help to navigate through different eras and reunite our family. But this organization is relentless in their pursuit, and we need to stay one step ahead of them.' He looks at you, his eyes filled with hope, and asks, 'Will you help us? Will you join us in this quest to find my daughter and bring our family back together?' What will you do? Will you HELP him, or DECLINE the offer?")
                        options = ["help","decline"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                        _phase5 = False
                    elif (choice.lower() != "find" or choice.lower() != "after"):
                        if (choice.lower() == "who"):
                            print("You decide to ask the man who he is. He looks at you and say, my name is John, I'm just a man looking for his daughter. What will you do? Ask who SHE is or CONFRONT the man?")
                            options = ["she","confront"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                            _phase5 = False
                        elif (choice.lower() == "is she"):
                            print("As you inquire about the girl's identity, the man responds with a cryptic smile. 'Her name is Alice, but you already know that, don't you?' His words send a chill down your spine, and you begin to question how he could have known about your knowledge of the next city. Before you can come up with an explanation, the man's movements become alarmingly swift. In a blink of an eye, he withdraws a peculiar-looking baton with a glowing tip and strikes you with a sudden, jolting force.")
                            _phase5 = False
                        elif (choice.lower() == "be"):
                            print("You inquire about the perplexing ability of the girl to be present in multiple places simultaneously. The man locks eyes with you, his expression filled with intrigue. 'Ah, so you're aware of her secret. Impressive,' he remarks. 'I'll give you an opportunity to prove yourself. She is a time traveler, evading the clutches of justice. Our organization is dedicated to capturing her and restoring order. Given your encounters with her, I offer you a chance to aid us in apprehending her. What do you say?' Will you HELP or will you DECLINE the offer?.")
                            options = ["help","decline"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                            _phase5 = False
                        elif (choice.lower() != "who" or choice.lower() != "she" or choice.lower() != "be"):
                            if (choice.lower() == "see"):
                                print("Intrigued by the mysterious girl's warning, you decide to follow her instructions. As you make your way down the street and turn the corner, you spot an abandoned building. Without hesitation, you enter the building and find the girl waiting for you inside. Her name is Alice. She begins to explain her story as a time traveler in search of her lost father who is trapped in time. She shares her fears, struggles, and the importance of finding her father to restore the timeline. At the end of her story, she looks at you and asks for your help. What will you do? Will you HELP HER or NOT HELP her?")
                                options = ["help her","not help"]
                                choice = make_choice(options, choices)
                                choices[choice] = choice
                                _phase5 = False
                            elif (choice.lower() == "tell"):
                                print("Feeling a sense of duty, you decide to inform the man about the unexpected call. You explain to him about the warning and what the girl said. The man's expression changes, but he remains composed. 'She's a clever one,' he mutters. 'But I assure you, she's running from the truth.' He thanks you for the information and his expression turns sinister. Suddenly, with a menacing look, he swiftly pulls out a baton with a glowing tip and strikes you with it. The impact sends a surge of pain through your body, and your vision begins to blur. As darkness envelops you, you realize you've fallen into the man's trap.")
                                _phase5 = False
                            elif (choice.lower() != "see" or choice.lower() != "tell"):
                                if (choice.lower() == "take"):
                                    print("Feeling overwhelmed by the strange events and the warning you received, you decide that it's best to leave this all behind. Taking the bus seems like the simplest way to distance yourself from the situation. You make your way to the nearest bus stop and board the bus that arrives shortly after. As the bus departs, you can't help but wonder about the mysteries that unfolded before you. However, for now, you choose to return to the comfort of your home and leave the enigmatic occurrences of this night behind. The bus ride is uneventful, and soon you find yourself safely back at your residence. You enter your home, close the door, and reflect on the strange encounters you had. Perhaps one day you will uncover the truth, but for now, it remains a mystery left behind on the streets you traversed.")
                                    _phase5 = False
                                    _restart = False
                                    break
                                elif (choice.lower() != "tell" or choice.lower() != "take"):
                                    if (choice.lower() =="hang"):
                                        print("Feeling overwhelmed by the strange events and the warning you received, you decide that it's best to leave this all behind. Taking the bus seems like the simplest way to distance yourself from the situation. You make your way to the nearest bus stop and board the bus that arrives shortly after. As the bus departs, you can't help but wonder about the mysteries that unfolded before you. However, for now, you choose to return to the comfort of your home and leave the enigmatic occurrences of this night behind. The bus ride is uneventful, and soon you find yourself safely back at your residence. You enter your home, close the door, and reflect on the strange encounters you had. Perhaps one day you will uncover the truth, but for now, it remains a mystery left behind on the streets you traversed.")
                                        _phase5 = False
                                        _restart = False
                                        break
                                    elif (choice.lower() != "who" or choice.lower() != "hang"):
                                        if (choice.lower() == "follow the man"):
                                            print("As you followed the man cautiously, staying hidden and observing his every move, he led you to an abandoned building. Intrigued, you decided to enter as well, stepping into its dimly lit interior. Inside, the atmosphere was thick with an eerie silence, broken only by the echo of your footsteps. Suddenly, the man emerged from the shadows, his face contorted with anger and determination. Without warning, he struck you with his baton, leaving you dazed and disoriented.")
                                            _phase5 = False
                                        elif (choice.lower() == "go down"):
                                            print("After deciding not to follow the man, you chose to go down the street in search of Alice, determined to offer your help. As you reached the building where you believed she might be, a sense of anticipation filled the air. However, to your surprise and dismay, the man was already waiting for you inside. His expression turned cold and menacing as he uttered, 'You shouldn't have come here.' Without hesitation, he struck you with his baton, leaving you disoriented and overwhelmed by the unexpected turn of events.")
                                            _phase5 = False
                                        elif (choice.lower() != "follow the man" or choice.lower() != "go down"):
                                            if (choice.lower() == "enter"):
                                                print("You decide to go to the address provided by the girl. As you arrive at the building, you see it's a restaurant called 'The Timekeeper's Table,' its name intriguing and mysterious. Stepping closer to the entrance, you notice two men in brown coats stationed outside, their gaze fixed upon you with suspicion. Undeterred by their scrutiny, you make up your mind. You take a deep breath and confidently enter the building, determined to uncover the truth and help the girl, Alice. The door creaks as it opens, and the ambiance inside is filled with a sense of secrecy and anticipation. The aroma of delicious food wafts through the air, mingling with a subtle air of mystery. However, before you can take another step, the same man who had been pursuing you appears from the shadows within the restaurant. His eyes meet yours, and a sinister smile spreads across his face. 'You shouldn't have come here.' he declares ominously. In an instant, he raises his baton and swiftly strikes you with its glowing tip, leaving you disoriented and unable to comprehend the unfolding events. Darkness engulfs your senses as you slip into unconsciousness, unaware of what awaits you next.")
                                                _phase5 = False
                                            elif (choice.lower() == "side"):
                                                print("You decide to take a risk and enter the building through the side entrance. As you make your way stealthily through the dimly lit corridors, you hear hushed voices coming from a nearby room. Curiosity getting the better of you, you inch closer and overhear a conversation between the man and another person.\nIn a hushed tone, they discuss the recent discovery of a hidden vault located precisely where Alice had agreed to meet you in the abandoned building. This vault contains a mysterious artifact with the power to reset the timeline and eliminate all traces of time travel. However, there's a catch—the one who wields the artifact would be forever lost in the fabric of time, just like Alice's father.\nThis newfound knowledge intensifies your determination. You realize that securing the artifact is crucial not only for Alice's father but for unraveling the nefarious plans of a secret organization known as The Timekeepers. They have manipulated time for their own gain and threaten to disrupt the balance of the world.\nAs you absorb every word, a sudden chill runs down your spine. Before you can react or retreat, the door creaks open, and the man stands before you, a sinister smile on his face. With a swift motion, he raises his baton, poised to strike. The realization hits him like a blow, momentarily paralyzing him with shock and disbelief.\nUsing this momentary advantage, you swiftly take action, incapacitating the man and disarming him of his glowing tip baton. With newfound confidence, you stand tall, knowing that you possess the knowledge to resist the manipulations of the Timekeepers.\nHowever, the triumph is short-lived. Just as you prepare to move forward and secure the artifact, a powerful force strikes your body. The man's baton connects with a force that sends a surge of pain through you, causing you to stagger and fall to the ground. Dazed and disoriented, you struggle to regain your senses.\nThe man stands over you with a triumphant sneer. 'You shouldn't have meddled in the affairs of The Timekeepers.' he sneers. 'Now you'll pay the price for your curiosity.' The world around you blurs as darkness engulfs your vision, leaving you with a lingering sense of defeat.")
                                                _phase5 = False
                                            elif (choice.lower() != "enter" or choice.lower() != "side"):
                                                if (choice.lower() == "help"):
                                                    print("You join Alice in her relentless search for her missing father, determined to unravel the mystery that led her to the abandoned building. Together, you explore its decaying corridors, guided by the trail left behind by her father's enigmatic message.\nAs you delve deeper, fragments of his research reveal the existence of a hidden vault within the building, rumored to house an artifact with the power to reset time itself. Intrigued and filled with a mix of awe and trepidation, you press on, overcoming challenges and uncovering hidden passages along the way.\nThe building seems to come alive, whispering echoes of the past as you draw closer to the heart of the mystery. At last, you stand before the grand chamber, where the vault awaits. Symbolic representations of time adorn the imposing door, setting the stage for a moment of truth.\nAlice's eyes meet yours, mirroring both hope and apprehension. With a shared sense of determination, you step forward, ready to face the final phase of your quest. Your goal is clear: to unveil the truth and retrieve the artifact that could potentially restore her father and safeguard the delicate balance of time.\nHowever, as you approach the vault, a palpable stillness descends upon the chamber, sending a chill down your spine. An ominous voice pierces the silence, foretelling the challenges that await. Just then, the man who had eluded you emerges, his eyes revealing a mix of surprise and recognition. Standing beside him, the Timekeepers, enforcers of temporal order, observe your every move.\nCaught off guard by the man's sudden appearance, you take a moment to gather your thoughts. His relentless pursuit and knowledge of the situation become apparent, emphasizing the gravity of the choices before you.\nWith unwavering determination, you steel yourself for the impending confrontation. The fate of Alice's father, the power contained within the artifact, and the very course of time itself hang in the balance. This pivotal moment demands a decision—one that will shape the outcome of your extraordinary journey.\nWill you take the risk and reach out to touch the artifact, braving the unknown consequences? Will you entrust its power to Alice, placing your hope in her ability to wield it wisely and find her father? Or will you dare to place it in the hands of the man before you, hoping against all odds that he can be swayed to the path of righteousness?\nThe room pulsates with tension as the weight of your choice bears down upon you. The lives of all intertwined in this intricate web of time depend on your judgment. Choose wisely, for the threads of time wait for no one. Will you TOUCH the artifact, or let ALICE touch the artifact or let the MAN touch the artifact?")
                                                    options = ["touch", "alice", "man"]
                                                    choice = make_choice(options, choices)
                                                    choices[choice] = choice
                                                    _phase5 = False
                                                elif (choice.lower() == "father"):
                                                    print("You ask Alice about her father and why she is looking for him. Alice hesitates for a moment and then begins to speak.\nShe tells you that her father, Dr. Samuel Johnson, was a brilliant scientist who invented a time machine.\nBut one day, while testing the time machine, something went wrong and her father disappeared.\nSince then, Alice has been traveling through time, trying to locate her father and bring him back.\nShe doesn't know who is after her or why they want to stop her, but she believes they are a powerful organization.\nAlice pleads with you to help her in her quest to find her father and unravel the mystery behind the organization. What will you do HELP HER, or NOT HELP her?")
                                                    options = ["help her", "not help"]
                                                    choice = make_choice(options, choices)
                                                    choices[choice] = choice
                                                    _phase5 = False
                                                elif (choice.lower() == "give up"):
                                                    print("Feeling overwhelmed by the situation and uncertain about the consequences, you decide to give up.\nYou express your doubts to Alice and tell her that you're not willing to get involved.\nAlice's face drops, disappointment evident in her eyes.\nShe thanks you for considering it but understands your decision.\nYou part ways with Alice, watching her disappear into the depths of the abandoned building.\nAs you step out onto the street, you can't shake off the feeling that you missed out on a great adventure.\nHowever, you continue with your normal life, wondering what could have been.\nSometimes, choices are not just about what you gain, but also about what you might lose.")
                                                    _phase5 = False
                                                    _restart = False
                                                    break
                                                elif (choice.lower() != "help" or choice.lower() != "fater" or choice.lower() != "give up"):
                                                    if (choice.lower() == "confront"):
                                                        print("Feeling a surge of determination, you decide to confront the mysterious man.\nYou stand your ground as he approaches, his gaze locked on you.\nThe man stops a few feet away, sizing you up with a cold, calculating stare.\nYou demand answers from him, asking who he is and what he wants.\nThe man smirks and reveals a small device in his hand, pressing a button.\nSuddenly, the surroundings begin to blur and distort, as if reality itself is being manipulated.\nYou feel a strange sensation, like being pulled in different directions at once.\nIn a disorienting flash, you find yourself transported to an unfamiliar location.\nAs the disorientation subsides, you realize you're standing in a dimly lit room.\nThe man stands before you, now wearing a triumphant expression.\nHe introduces himself as a member of 'The Timekeepers,' an organization tasked with maintaining the integrity of the timeline.\nHe explains that Alice, the girl you were following, is a rogue time traveler who poses a threat to the fabric of reality.\nThe man offers you a choice: join the Timekeepers and help capture Alice, or face the consequences of interfering with the timeline.\nWhat will you do? Will you JOIN the Timekeepers or DECLINE their offer?")
                                                        options = ["join", "resist"]
                                                        choice = make_choice(options, choices)
                                                        choices[choice] = choice
                                                        _phase5 = False
                                                    elif (choice.lower() == "hide"):
                                                        print("You quickly hide in the shadows as the man approaches. Seizing the opportunity, you snatch the baton from his belt.\nThe man continues walking, unaware of his missing possession.\nExamining the baton, you notice a faint glow. With a surge of adrenaline, you strike the man with his own weapon.\nIn a blinding flash, he disappears, leaving behind only a white glow.\nYou stand there, stunned by what just happened.\nWhat will you do next? KEEP searching for the girl of go BACK to the bus stop?")
                                                        options = ["keep", "back"]
                                                        choice = make_choice(options, choices)
                                                        choices[choice] = choice
                                                        _phase5 = False
                                                    elif (choice.lower() != "confront" or choice.lower() != "hide"):
                                                        if (choice.lower() == "help her"):
                                                            print("You decide to help Alice, and together you embark on a journey to find her missing father. Following the trail, you arrive at an eerie abandoned building on the desolate street. Its weathered facade and mysterious aura create an atmosphere of anticipation.\nAs you step inside, the air is heavy with the scent of history. Alice's eyes meet yours, reflecting determination and a glimmer of hope. Together, you begin your search for clues, unraveling fragments of her father's research. It leads you deeper into the building, where whispers of forgotten tales and hidden passages beckon you forward.\nThe building seems alive, resonating with echoes of the past as you approach the heart of the mystery. Finally, you stand before the grand chamber, where the fabled vault awaits. Adorned with symbols of time, the imposing door hints at the secrets it guards.\nA moment of stillness envelops the chamber as you prepare to confront the final phase of your quest. Your mission is clear: to unveil the truth and retrieve the artifact capable of resetting time. This artifact holds the key to restoring Alice's father and safeguarding the delicate balance of the temporal realm.\nHowever, as you approach the vault, a hushed silence descends, sending shivers down your spine. An ominous voice reverberates, foretelling the challenges ahead. Suddenly, the man you've been pursuing emerges, his eyes betraying surprise and recognition. Standing beside him are the Timekeepers, enforcers of temporal order, watching your every move.\nCaught off guard by the man's appearance, you pause to gather your thoughts. The gravity of the situation dawns on you as his relentless pursuit and knowledge become evident. The choices before you carry immense consequences.\nWith unwavering resolve, you brace yourself for the impending confrontation. The fate of Alice's father, the power held within the artifact, and the very fabric of time itself hang in the balance. This pivotal moment demands a decision—one that will shape the outcome of your extraordinary journey.\nWill you take the risk and touch the artifact, defying the unknown consequences? Will you entrust its power to Alice, believing in her ability to wield it wisely and find her father? Or will you dare to place it in the hands of the man before you, hoping against all odds that he can be swayed towards righteousness?\nThe room crackles with tension as the weight of your choice bears down upon you. The lives of those intertwined in the tapestry of time depend on your judgment. Choose wisely, for the threads of destiny wait for no one. Will you TOUCH the artifact, let ALICE touch it, or extend it to the MAN before you?")
                                                            options = ["touch", "alice", "man"]
                                                            choice = make_choice(options, choices)
                                                            choices[choice] = choice
                                                            _phase5 = False
                                                        elif (choice.lower() == "not help"):
                                                            print("In the hidden alleyway, Alice opens up to you, revealing her desperate quest to find her father. She seeks your help, but you hesitate. After careful consideration, you decide not to assist her.\nWith a heavy heart, you bid farewell to Alice, knowing that her journey will continue without your support. The weight of your choice lingers in your mind as you move forward on your own path.\n THE END")
                                                            _phase5 = False
                                                            _restart = False
                                                            break
                                                        elif (choice.lower() != "help her" or choice.lower() != "help her"):
                                                            if (choice.lower() == "go home"):
                                                                print("You decide to listen to your fatigue and make your way back home. The streets familiarize themselves once more as you retreat from the enigmatic journey you briefly embarked upon. The allure of the unknown gives way to the solace of your own sanctuary.\nAs you close the door behind you, the echoes of adventure fade into the background. Your decision to go home brings a mix of relief and curiosity. Perhaps the choices made and the paths not taken will forever remain as whispers of what could have been.\nIn the comfort of your familiar surroundings, you find respite and a moment of introspection. The mysteries of the redhead girl and the man who pursued her become fragments of a story left untold. Life continues its steady rhythm, and you find contentment in the simplicity of your everyday existence.\nThe streets outside may hold secrets and extraordinary tales, but for now, you embrace the quietude of your own world. The journey may have ended prematurely, but the memories of what could have been linger in the recesses of your imagination.")
                                                                _phase5 = False
                                                                _restart = False
                                                                break
                                                            elif (choice.lower() == "building"):
                                                                print("Without hesitation, you point towards the building with the open window and say, 'She went into that building over there.' The man narrows his eyes and, seemingly satisfied with your answer, rushes towards the entrance of the building.\nAs he disappears inside, you seize the moment to assess the situation. From your vantage point, you witness the man making a call on his communication device. Moments later, several figures materialize out of thin air, dressed in the same brown robes as the man.\nA plan begins to form in your mind. Swiftly and stealthily, you move towards one of the agents, taking advantage of their distraction. With a well-timed strike, you incapacitate the agent and snatch his baton. The brown robe now in your possession, you quickly slip it on, disguising yourself as one of the enigmatic timekeepers.\nConfident in your guise, you silently trail the group of agents through the building. Each step brings you closer to unraveling the mystery surrounding the girl and the artifact that lies within the vault. The tension in the air grows palpable as you approach a room bathed in an ethereal glow.\nPeering inside, your heart skips a beat as you see yourself and the girl standing near a grand vault, its contents shrouded in mystery. The man who pursued the girl begins to monologue, attempting to sway the other version of you to allow him to touch the artifact.\nRealizing the critical moment at hand, you seize the opportunity. With a surge of adrenaline, you swing your baton, striking the man with precision. A fierce battle ensues as each blow from your baton causes the agents to dissolve into wisps of light, disappearing from existence.\nYou fight valiantly, prevailing against the overwhelming odds. Victory seems within your grasp as you prepare to deliver the final blow to the last remaining agent. However, in a desperate counterattack, the agent manages to strike you with his baton, causing a blinding burst of light.")
                                                                _phase5 = False
                                                            else:
                                                                print("Please select GO HOME or BUILDING")
                                                                options = ["go home", "building"]
                                                                choice = make_choice(options, choices)
                                                                choices[choice] = choice
                                                        else:
                                                            print("Please select HELP HER or NOT HELP")
                                                            options = ["help her", "not help"]
                                                            choice = make_choice(options, choices)
                                                            choices[choice] = choice
                                                    else:
                                                        print("Please select CONFRONT or HIDE")
                                                        options = ["confront", "hide"]
                                                        choice = make_choice(options, choices)
                                                        choices[choice] = choice
                                                else:
                                                    print("Please select HELP, FATHER or GIVE UP")
                                                    options = ["help", "father", "give up"]
                                                    choice = make_choice(options, choices)
                                                    choices[choice] = choice
                                            else:
                                                print("Please select ENTER or SIDE")
                                                options = ["enter", "side"]
                                                choice = make_choice(options, choices)
                                                choices[choice] = choice
                                        else:
                                            print("Please select FOLLOW THE MAN or GO DOWN")
                                            options = ["follow the man", "go down"]
                                            choice = make_choice(options, choices)
                                            choices[choice] = choice
                                    else:
                                        print("Please select WHO or HANG")
                                        options = ["who", "hang"]
                                        choice = make_choice(options, choices)
                                        choices[choice] = choice
                                else:
                                    print("Please select TELL or TAKE")
                                    options = ["tell", "take"]
                                    choice = make_choice(options, choices)
                                    choices[choice] = choice
                            else:
                                print("Please select SEE or TELL")
                                options = ["tell", "see"]
                                choice = make_choice(options, choices)
                                choices[choice] = choice
                        else:
                            print("Please select WHO, SHE or BE")
                            options = ["who", "she", "be"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                    else:
                        print("Please select FIND or AFTER")
                        options = ["find", "after"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                else:
                    print("Please select SEARCH or RUN")
                    options = ["search", "run"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
            else:
                print("Please select TALK or CALL")
                options = ["talk", "call"]
                choice = make_choice(options, choices)
                choices[choice] = choice
        else:
            print("Please select IN or NOT")
            options = ["in", "not"]
            choice = make_choice(options, choices)
            choices[choice] = choice
    
    _phase6 = True

    while _phase6:
        if (_restart == False):
            _phase6 = False
            break
        if (choice.lower() == "stay there" or choice.lower() == "go" or choice.lower() == "inside" or choice.lower() == "in" or choice.lower() == "not" or choice.lower() == "call" or choice.lower() == "is she" or choice.lower() == "tell" or choice.lower() == "follow the man" or choice.lower() == "go down" or choice.lower() == "enter" or choice.lower() == "side" or choice.lower() == "building"):
            _phase6 = False
            break
        if (choice.lower() == "stand up"):
            print("")
            _phase6 = False
        elif (choice.lower() == "let"):
            print("")
            _phase6 = False
        elif (choice.lower() != "stand up" or choice.lower() != "let"):
            if (choice.lower() == "help"):
                print("")
                _phase6 = False
                _restart = False
            elif (choice.lower() == "decline"):
                print("")
                _phase6 = False
            elif (choice.lower() != "help" or choice.lower() != "decline"):
                if (choice.lower() == "she"):
                    print("")
                    _phase6 = False
                elif (choice.lower() == "confront"):
                    print("")
                    _phase6 = False
                elif (choice.lower() != "she" or choice.lower() != "confront"):
                    if (choice.lower() == "help her"):
                        print(" ")
                        options = ["touch", "alice", "man"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                    elif (choice.lower() == "not help"):
                        print()
                        _phase6 = False
                        _restart = False
                    elif (choice.lower() != "help her" or choice.lower() != "not help"):
                        if (choice.lower() == "touch"):
                            print("")
                            _phase6 = False
                            _restart = False
                        elif (choice.lower() == "alice"):
                            print("")
                            _phase6 = False
                            _restart = False
                        elif (choice.lower() == "man"):
                            print("")
                            _phase6 = False
                            _restart = False
                        elif (choice.lower() != "touch" or choice.lower() != "alice" or choice.lower() != "man"):
                            if (choice.lower() == "join"):
                                print("")
                                _phase6 = False
                            elif (choice.lower() == "resist"):
                                print("")
                                _phase6 = False
                            elif (choice.lower() != "join" or choice.lower() != "refuse"):
                                if (choice.lower() == "keep"):
                                    print("")
                                    _phase6 = False
                                elif (choice.lower() == "back"):
                                    options = ["touch", "alice", "man"]
                                    choice = make_choice(options, choices)
                                    choices[choice] = choice
                                else:
                                    print("Please select KEEP or BACK")
                                    options = ["keep", "back"]
                                    choice = make_choice(options, choices)
                                    choices[choice] = choice
                            else:
                                print("Please select JOIN or RESIST")
                                options = ["join", "resist"]
                                choice = make_choice(options, choices)
                                choices[choice] = choice
                        else:
                            print("Please select TOUCH, ALICE or MAN")
                            options = ["touch", "alice", "man"]
                            choice = make_choice(options, choices)
                            choices[choice] = choice
                    else:
                        print("Please select HELP HER or NOT HELP")
                        options = ["help her", "not help"]
                        choice = make_choice(options, choices)
                        choices[choice] = choice
                else:
                    print("Please select SHE or CONFRONT")
                    options = ["she", "confront"]
                    choice = make_choice(options, choices)
                    choices[choice] = choice
            else:
                print("Please select HELP or DECLINE")
                options = ["help", "decline"]
                choice = make_choice(options, choices)
                choices[choice] = choice
        else:
            print("Please select STAND UP or LET")
            options = ["stand up", "let"]
            choice = make_choice(options, choices)
            choices[choice] = choice