rs,w,m,c,cup= 550, 400, 540, 120, 9 

def remaining():
    print("The coffee machine has:")
    print(w," of water")
    print(m," of milk")
    print(c," of coffee beans")
    print(cup," of disposable cups")
    print(rs," of money")
    
def buy():
    global rs,w,m,c,cup
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    n=input()
    if(n == '1'):
        if(w>=250 and m>=0 and c>=16):
            print("I have enough resources, making you a coffee!")
            w=w-250
            m=m
            c=c-16
            cup=cup-1
            rs=rs+4

        if(w<250):
            print("Sorry, not enough water!")
        if(c<16):
            print("Sorry, not enough coffee beans!")

        
    elif(n == '2'):
        if(w>=350 and m>=75 and c>=20):
            print("I have enough resources, making you a coffee!")
            w=w-350
            m=m-75
            c=c-20
            cup=cup-1
            rs=rs+7
        if(w<350):
            print("Sorry, not enough water!")
        if(m<75):
            print("Sorry, not enough milk!")
        if(c<20):
            print("Sorry, not enough coffee beans!")
        
    elif(n == 'back'):
        pass

    
    elif(n == '3'):
        if(w>=200 and m>=100 and c>=12):
            print("I have enough resources, making you a coffee!")
            w=w-200
            m=m-100
            c=c-12
            cup=cup-1
            rs=rs+6
        if(w<200):
            print("Sorry, not enough water!")
        if(m<100):
            print("Sorry, not enough milk!")
        if(c<12):
            print("Sorry, not enough coffee beans!")

        
def fill():
    global rs,w,m,c,cup
    print("Write how many ml of water do you want to add:")
    add_w = int(input())
    print("Write how many ml of milk do you want to add:")
    add_m = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    add_c = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    add_cup = int(input())
    
    w=w+add_w
    m=m+add_m
    c=c+add_c
    cup=cup+add_cup
    rs=rs


def take():
    global rs,w,m,c,cup
    print("I gave you $",rs)
    rs=rs-rs
    
g=input()
while(g != 'exit'):
    print("Write action (buy, fill, take, remaining, exit):")

    if(g == 'remaining'):
        remaining()
    elif(g == 'buy'):
        buy()
    elif(g == 'fill'):
        fill()
    elif(g == "take"):
        take()
    g=input()
