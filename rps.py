from random import randint
game=['Rock','paper','Scissors']
Computer=game[randint(0,2)]
Computerpoints=0
Playerpoint=0
Player=False
while Player==False:
    Player=input('Rock,paper,Scissors?:')
    if Computer==Player:
        print('Tie')
    elif Player=='Rock':
        if Computer=='paper':
            print('Computer won you lost')
            Computerpoints=Computerpoints+1
        else:
            print('Hurrah! You won computer lost')
            Playerpoint=Playerpoint+1
    elif Player=='paper':
        if Computer=='Scissors':
            print('Computer won you lost:(')
            Computerpoints=Computerpoints+1
        else:
            print('Hippeeee!! You won')
            Playerpoint=Playerpoint+1
    elif Player=='Scissors':
        if Computer=='Rock':
            print('Computer won You lost')
            Computerpoints=Computerpoints+1
        else:
            print('You won computer lost')
            Playerpoint=Playerpoint+1
    else:
        print('Wrong option')
    Player=False
    Computer=game[randint(0,2)]
