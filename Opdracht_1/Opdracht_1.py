#Create an object called Player
class Player:
    #Initialize the variables.
    def __init__(self, Health, Strength, Defense, Magic, Resistance):    
        self.Health = Health
        self.Strength = Strength
        self.Defense = Defense
        self.Magic = Magic
        self.Resistance = Resistance

    #Break the game if the Player's Health equals 0.    
    def Death(self):    
        if(self.Health < 1):
            print("You died.")
        elif(self.Health > 1):
            print("Status: Alive")
                  
    #Subtract your Strength value from the Enemy's Health and add the Enemy's Defense to their Health after.       
    def Attack(self):
        enemy.Health - self.Strength + enemy.Defense
        Damage = self.Strength - enemy.Defense
        print("You attack the enemy!")
        print("The enemy takes " + str(Damage) + " damage!")

    #Subtract your Magic value from the Enemy's Health and add the Enemy's Resistnce to their Health after.
    def magicAttack(self):
        enemy.Health - self.Magic + enemy.Resistance
        MagicDamage = self.Magic - enemy.Resistance
        print("You cast a spell on the enemy!")
        print("The enemy takes " + str(MagicDamage) + " damage!")

#Create a variable called player and let it take over the values of the class Player    
player = Player(50, 15, 3, 4, 20)


        
class Enemy(Player):
    def enemyAttack(self):
        player.Health - self.Strength + player.Defense
        playerDamage = self.Strength - player.Defense
        print("The enemy attacks!")
        print("You take " + str(playerDamage) + " damage!")

    def enemyMagicAttack(self):
        player.Health - self.Magic + player.Resistance
        playerMagicDamage = self.Magic - player.Resistance
        print("The enemy casts a spell on the player!")
        print("You take " + str(playerMagicDamage) + " damage!")

enemy = Enemy(30, 10, 5, 4, 1)

player.magicAttack()
enemy.enemyMagicAttack()
