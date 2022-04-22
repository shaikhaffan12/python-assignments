position = 0 #initial position is 0

for i in range(4):
    get_inp = input("Enter Movement: ") # get movement from user
    mov = get_inp.split(" ")
    if mov[0] == 'up':
        position += int(mov[1]) # if input is up then add the next argument to position
    elif mov[0] == 'down':
        position -= int(mov[1]) # if input is down the minus the next argument from position
    elif mov[0] == 'right':
        position += int(mov[1]) # if input is right then add the next argument to position
    elif mov[0] == 'left':
        position -= int(mov[1]) # if input is left the minus the next argument from position


print(position)