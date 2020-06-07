from random import randint
def createlist(n1,n2):
    if n1==n2:
        return n1
    else:
        res=[]
        while n1<n2+1:
            res.append(n1)
            n1=n1+1
        return res
n1,n2=0,100
no=createlist(n1,n2)
print(no)
#print(type(no))
Player=False
guess=no[randint(0,100)]
#print(type(guess))
while Player==False:
    Player=input('Guess the number b/w 0-100: ')
    p=int(Player)
    if p==guess:
        print('hurrah! your guess is correct')
        ans=input('Do yo want to continue Y/N?:')
        if ans=='Y'or ans=='y':
            Player=False
            continue
        else:
            print('Thank you for playing.Hope you enjoyed')
            Player=True
    else:
        print(':( Sorry your guess is wrong')
        ans=input('Do yo want to continue Y/N?:')
        if ans=='Y' or ans=='y':
            Player=False
            continue
        else:
            print('Thank you for playing.Hope you enjoyed')
            Player=True
