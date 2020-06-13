class Coff:
    def __init__(self):
        self.rs = 550
        self.w = 400
        self.m = 540
        self.c = 120
        self.cup = 9

    def remaining(self):
        print("The coffee machine has:")
        print(self.w," of water")
        print(self.m," of milk")
        print(self.c," of coffee beans")
        print(self.cup," of disposable cups")
        print("$",self.rs," of money")
        
    def buy(self):
        #global self.rs,self.w,self.m,self.c,self.cup
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        n=input()
        if(n == '1'):
            if(self.w>=250 and self.m>=0 and self.c>=16):
                print("I have enough resources, making you a coffee!")
                
                self.w = self.w-250
                self.m = self.m
                self.c = self.c-16
                self.cup = self.cup-1
                self.rs = self.rs + 4

            if(self.w<250):
                print("Sorry, not enough water!")
            if(self.c<16):
                print("Sorry, not enough coffee beans!")
         
        elif(n == '2'):
            if(self.w>=350 and self.m>=75 and self.c>=20):
                print("I have enough resources, making you a coffee!")
                
                self.w = self.w-350
                self.m = self.m-75
                self.c = self.c-20
                self.cup = self.cup-1
                self.rs = self.rs + 7

            if(self.w<350):
                print("Sorry, not enough water!")
            if(self.m<75):
                print("Sorry, not enough milk!")
            if(self.c<20):
                print("Sorry, not enough coffee beans!")
            
        elif(n == 'back'):
            pass
    
        elif(n == '3'):
            if(self.w>=200 and self.m>=100 and self.c>=12):
                print("I have enough resources, making you a coffee!")
                
                self.w = self.w-200
                self.m = self.m-100
                self.c = self.c-12
                self.cup = self.cup-1
                self.rs = self.rs + 6
            
            if(self.w<200):
                print("Sorry, not enough water!")
            if(self.m<100):
                print("Sorry, not enough milk!")
            if(self.c<12):
                print("Sorry, not enough coffee beans!")

            
    def fill(self):
        #global self.rs,self.w,self.m,self.c,self.cup
        print("Write how many ml of water do you want to add:")
        add_w = int(input())
        print("Write how many ml of milk do you want to add:")
        add_m = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        add_c = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        add_cup = int(input())
        
        self.w += add_w
        self.m += add_m
        self.c += add_c
        self.cup += add_cup
        self.rs = self.rs
        
    def take(self):
        #global self.rs,self.w,self.m,self.c,self.cup
        print("I gave you $",self.rs)
        self.rs -= self.rs
        
print("Write action (buy, fill, take, remaining, exit):")   
g=input()
ad = Coff()
while(g != 'exit'):
    if(g == 'remaining'):
        ad.remaining()
    elif(g == 'buy'):
        ad.buy()
    elif(g == 'fill'):
        ad.fill()
    elif(g == "take"):
        ad.take()
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    g=input()
