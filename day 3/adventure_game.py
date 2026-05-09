hook = "You look up at the mountainous refrigerator " \
"and hear a small whisper in your head, urging you to open the door. " \
"How do you open it? A. I don't B. Grab the sewing needle and thread from your belt " \
"and wind it around the handle C Try to climb and wedge in between the door frame and door. "

decision_a = "You decide to ignore the whisper and stay small forever, " \
"getting swuashed like a beetle by a giant ping pong paddle. Game over."

decision_b = "You grab the sewing needle and thread from your belt and wind it around the handle. " \
"You pull with all your might, the door cracks open, and you hear the crash of a glass viniagrette bottle. " \
"The viniagrette washes over you like a tsunami, what do you do? D. grab onto a shard of glass and surf " \
"E. drown F. flip the lid upside down and use it as a boat. "

decision_c = "You're able to wedge yourself in the crack and fall into the chilly mansion, seeing mold everywhere. " \
"You make a nice little home for youself and die a peaceful death due to the cold. Game over, but happily."

decision_d = "You rip through the current, cutting your hands in the process. One backflip after another, " \
"you wind your way to the lowest part of the house: the bathroom drain. " \
"You fall through the whole about 2 feet, but it's enough to crush your tiny body. Game over."

decision_e = "You die. Game over. "

decision_f = "You hop in the lid of the bottle and the viniagrette wave takes you to the bathroom drain, " \
"but the lid stops you from falling in, but you hear footsteps. What do you do? G. climb into the trash can " \
"H. hope they don't notice I. grab the blade from the razor and prepare to attack. "

decision = input(hook) #collect decision from user
decision = decision.upper()


if decision == "A":
    decision2 = input(decision_a)
elif decision == "B":
    decision2 = input(decision_b)
elif decision == "C":
    decision2 = input(decision_c)
else:
    print("Please enter a valid option (A, B, or C).")

if decision == "A" or decision == "B" or decision =="C":
    decision2 = decision2.upper()

    if decision2 == "D":
        decision3 = input(decision_d)
    elif decision2 == "E":
        decision3 = input(decision_e)
    elif decision2 == "F":
        decision3 = input(decision_f)
    else:
        print("You die a painful death.")

    if decision == "D" or decision == "E" or decision == "C":
        decision3 = decision3.upper()
