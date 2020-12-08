#This is a bit of a complicated solution and is currently only set up for part 2 though the part 1 code was very similar
#Basically for part 2 we go until we get an infinite loop, then we keep rewinding through time until we find a solution that works

fin = open("input.txt", "r")
instruct = list(map(lambda x: x.strip(), fin.readlines()))

#A list that keeps track of how many times we visited everything, starts out with 0's
visits = [0 for i in range(len(instruct))]
#The accumulator
accu = 0
#Current index location
i = 0
#A list that will keep track of historical jmps and nops
history = []
#The current spot in history we have rewound to
currentRewind = -1
#If we need to swap a command or not
swap = False
#A flag to see if we have stopped because we can stop recording history then
swapped = False
#Loop through every instruction
while i < len(instruct):
    #Increment the visit counter for this spot
    visits[i] += 1
    #If this is a second visit we have failed and have a loop
    if visits[i] == 2:
        #Go to the last recored jmp or nop in the history
        if currentRewind == -1:
            currentRewind = len(history) - 1
        elif currentRewind == 0:
            print("Failed")
            break
        else:
            #Or just rewind back one spot
            currentRewind -= 1
        #And reset the values back to their historical position to continue
        i, accu, visits = history[currentRewind]
        #Swap the jmp with nop or nop with jmp
        swap = True
        #And stop recording history
        swapped = True
        #print("Infinite:", accu)
        #break
    command, value = instruct[i].split(" ")
    #Accumulates functions normally
    if command == "acc":
        accu += int(value)
        i += 1
    elif command == "jmp":
        #If we are swapping we do a nop instead
        if swap:
            i += 1
            swap = False
        else:
            #Only record history if we haven't swapped already
            if not swapped:
                history.append((i, accu, visits))
            i += int(value)
    #nop
    else:
        #If we are swapping do a jmp instead
        if swap:
            i += int(value)
            swap = False
        else:
            #Only record history if we haven't swapped already
            if not swapped:
                history.append((i, accu, visits))
            i += 1
print(accu)