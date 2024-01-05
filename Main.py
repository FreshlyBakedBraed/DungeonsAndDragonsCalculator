import random
print("Welcome to DND Statistics calculator. Here you can set the hp of an enemy and you and it will calculate the chances of you winning")
print("You can enter the Hp of your character, enemy and how many times you want the calculations to occur")
print("Code is by freshlybakedbread on discord :3 ")
print("WARNING : Since computers are never fully random take these results with a grain of salt")
print("")
print("")
print("")
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#                                  Variable Declaring // Class Declaration
class Player:
    id = "player"
    def __init__(self, health,turn,dice,wincount):
        self.Hp = health
        self.OriginHp = health
        self.isTurn = turn
        self.HitRate = dice
        self.WinCount = wincount

class Enemy:
    id = "enemy"
    def __init__(self, health,turn,dice,wincount):
        self.Hp = health
        self.OriginHp = health
        self.isTurn = turn
        self.HitRate = dice
        self.WinCount = wincount
MainPlayer = Player(int(input("What is Player Hp ")),False,int(input("What is the least number the Player can roll to land an Attack from a D20? ")),0)
Enemy1 = Enemy(int(input("What is Enemy Hp ")),False,int(input("What is the least number the Enemy can roll to land an Attack from a D20? ")),0)
CallTimes = int(input("How many times shall the simulation should be run? "))
FirstHit = int(input("Who Should Attack First (1 for you , 0 for enemy) "))
isBattling = True




#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#                                    Functions 

def RollD20():
    result20 = random.randrange(1,20) 
    return result20

def RollD6():
    result6 = random.randrange(1,6)
    return result6

def Restart(x,y):
    x.Hp = x.OriginHp
    y.Hp = y.OriginHp 
    x.isTurn = True
    y.isTurn = True


def CheckDead(PersonWhoHit,PersonWhoGotHit):
    if(PersonWhoGotHit.Hp<=0):
        print(f"{PersonWhoGotHit.id} has died {PersonWhoHit.id} has won")
        PersonWhoHit.WinCount +=1
        return False
    else:
        return True


def Hit(Attacker,Victim):
    if(RollD20()>= Attacker.HitRate):
        DamageDealt = RollD6()
        print(f"{DamageDealt} damage has been dealt to {Victim.id}")
        Victim.Hp -= DamageDealt    
    else:
        print("Attack Has Missed! ")
    
    
def WinRateCalculator(x,y,z):
    print(f"Player has won {x} times! ")
    print(f"Enemy has won {y} times! ")
    print(f"Winrate is {x/z} !!! ")

#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#                               Actual Code



for x in range(CallTimes):
    isBattling = True
    Restart(MainPlayer,Enemy1)
    print(f"This is the {x}th time the simulation has been run")
    while(isBattling): 
        if(FirstHit == 1): #You are Hitting First
        
            Hit(MainPlayer,Enemy1)
            if(CheckDead(MainPlayer,Enemy1) == False):
                break
            
            Hit(Enemy1,MainPlayer)
            if(CheckDead(Enemy1,MainPlayer)== False):
                break
            
            

        elif(FirstHit == 0): #Enemy is Hitting First
            Hit(Enemy1,MainPlayer)
            if(CheckDead(Enemy1,MainPlayer)== False):
                break
            Hit(MainPlayer,Enemy1)
            if(CheckDead(MainPlayer,Enemy1) == False):
                break
        

        else:
            print("ERROR : You have not chosen who will hit first correctly")
    isBattling = False
    
WinRateCalculator(MainPlayer.WinCount,Enemy1.WinCount,CallTimes)





