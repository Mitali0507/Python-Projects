import random #to get random numbers from computer

'''
snake= 1
water=-1
gun=0
'''
computer=random.choice([-1,0,1])
youstr=input("enter= ")
youdict={
    's':1,
    'w':-1,
    'g':0
}
revdict={1:"snake",
        -1:"water",
         0:"gun" }

you=youdict[youstr]

print(f"you chose {revdict[you]} and computer chose {revdict[computer]}")

if (computer==you):
    print('its a draw')
else:
    if (computer == -1 and you ==1):
        print("you win!")
    elif(computer==1 and you == -1):
        print("you lose")
    elif(computer== 0 and you ==1):
        print("you lose")
    elif(computer== 1 and you== 0):
        print("you win")
    elif(computer==0 and you == -1):
        print("you lose")
    elif(computer == -1 and you == 0):
        print('you win')                    
        


     


