def print_field(_field):
    print("---------")
    print("| {} |".format(' '.join(_field[0])))
    print("| {} |".format(' '.join(_field[1])))
    print("| {} |".format(' '.join(_field[2])))
    print("---------")

def checking():            
    #winner
    variants = [ [reprfield[0][0],reprfield[0][1],reprfield[0][2]],
             [reprfield[1][0],reprfield[1][1],reprfield[1][2]],
             [reprfield[2][0],reprfield[2][1],reprfield[2][2]],
             [reprfield[0][0],reprfield[1][0],reprfield[2][0]],
             [reprfield[0][1],reprfield[1][1],reprfield[2][1]],
             [reprfield[0][2],reprfield[1][2],reprfield[2][2]],
             [reprfield[0][0],reprfield[1][1],reprfield[2][2]],
             [reprfield[0][2],reprfield[1][1],reprfield[2][0]] ]
    for myvar in variants:
        if myvar.count('X') == 3:
            return 'X wins'
        elif myvar.count('O') == 3:
            return  'O wins'
    #game not finished
    for myvar in variants:
        if myvar.count('_') > 0:
            return 'Continue' 
    #draw
    return 'Draw'

def newfield():
    global side
    global reprfield
    global check    
    for point in mystep:
        if not point.isdigit():
            print("You should enter numbers!")
            return False
        elif int(point) not in range(1,4):
            print("Coordinates should be from 1 to 3!")
            return False
    if mystep[1] == '1':
        mystep[1] = '2'
    elif mystep[1] == '2':
        mystep[1] = '1'
    elif mystep[1] == '3':
        mystep[1] = '0'
    if reprfield[int(mystep[1]) ][int(mystep[0]) - 1] =='_':
        reprfield[int(mystep[1])][int(mystep[0]) - 1]  = side
        if side == 'X':
            side = 'O'
        else:
            side = 'X'       
        check = checking()
        return True        
    else:
        print("This cell is occupied! Choose another one!")
        return False

#start game
reprfield = [['_','_','_'],['_','_','_',],['_','_','_']]
print_field(reprfield)
side='X'
check = 'Continue'

while check == 'Continue':
    flag = False
    while flag == False:
        mystep = input('Enter the coordinates:').split()
        flag = newfield()
        print_field(reprfield)
      
print(check)
