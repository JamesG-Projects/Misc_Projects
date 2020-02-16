"""Final.py: A Text Adventure"""
__author__ = "James Garrett"
__credits__ = ["James Garrett"]
__email__ = "garretjb@mail.uc.edu"

#A Text-Based Adventure

################################################################################
# Game Config ##################################################################
################################################################################
try:
    import readline
except ImportError:
    pass

try:
    from random import randint
except ImportError:
    pass

try:
    from random import choice
except ImportError:
    pass

################################################################################
# Player Object ################################################################
################################################################################
class Player(object):
    def __init__(self, name, place, health):
        self.name = name
        self.place = place
        self.health = health
        self.max_health = health
        self.backpack = []
        #self.items = {item.name: item for item in self.backpack}
        Player.tookbackpack = False
        Player.wonComp = False
        Player.wonBear = False
        Player.wonFinal = False
        self.turn = False


    def look(self):
        self.place.look()

    def tookbackpack(self):
        if self.tookbackpack:
            return True
        else:
            return False

    def go_to(self, direction):
        self.place = self.place.exit_to(direction)

################################################################################
# Player/Enemy Combat ##########################################################
################################################################################

    def fight(self, person):
        enemy = self.place.enemies[person]
        strt = ''
        strt = input('')
        print('%s started a fight with you!!'% (enemy.name))
        strt = input('')
        print(chr(27) + "[2J")

        EName = enemy.name
        #print("EName: ", EName)
        if EName in 'Computer':
            itemsPlayer = {'heal': randint(10,25),                              #Player's attacks
                           'punch' : 10}
            itemsEnemy = {'whip': randint(5,15)}                                #Enemy's attacks
            if keyboard in self.backpack:
                itemsPlayer['keyboard'] = 30
                #itemsPlayer.update(keyboard = randint(1,5))                    #Also works
            if blowgun in self.backpack:
                if blowdart in self.backpack:
                    itemsPlayer['blowgun'] = randint(5,10)
            if sword in self.backpack:
                itemsPlayer['sword'] = randint(50,100)
        if EName in 'Giant bear':
            itemsPlayer = {'heal': randint(30,60),
                           'punch' : 35}
            itemsEnemy = {'claws': randint(15,30),
                          'smack': randint(10,20),
                          'roar': randint(20,35)}
            if keyboard in self.backpack:
                itemsPlayer['keyboard'] = randint(1,5)
            if blowgun in self.backpack:
                if blowdart in self.backpack:
                    itemsPlayer['blowgun'] = randint(15,30)
            if sword in self.backpack:
                itemsPlayer['sword'] = randint(40,50)
        if EName in 'Sentient computer':
            itemsPlayer = {'heal': randint(65,125),
                           'punch': 20}
            itemsEnemy = {'whip': randint(20,35),
                          'glare': randint(30,45),
                          'virus': randint(40,80)}
            if keyboard in self.backpack:
                itemsPlayer['keyboard'] = randint(100,999)
            if blowgun in self.backpack:
                if blowdart in self.backpack:
                    itemsPlayer['blowgun'] = randint(50,150)
            if sword in self.backpack:
                itemsPlayer['sword'] = randint(300,500)

        play = True                                                             #Start Fight
        while play:
            winner = None
            turn = randint(1,2)                                                 #Determine who starts
            print('Your health: ', self.health)
            print("%s's health: %d"% (enemy.name, enemy.health))
            if turn == 1:
                self.turn = True
                enemy.turn = False
                print('%s, attack it!' % (self.name))
            else:
                self.turn = False
                enemy.turn = True
                print('%s is attacking you!' % (enemy.name))

            # Fighting loop=====================================================
            while (self.health != 0 or enemy.health != 0):

                heal = False
                miss = False                                                    #Attack will miss
                incMiss = False                                                 #Increase chance attack misses
                if self.turn:
                    if self.health <= 0:
                        self.health = 0
                        winner = enemy.name
                        break
                    elif enemy.health <= 0:
                        enemy.health = 0
                        winner = self.name
                        break

                    print("\nYour health: %d \n%s's health: %d" % (self.health, enemy.name, enemy.health))
                    print('Select your attack:')
                    for key in itemsPlayer:
                        print("     ", key)
                    #print(itemsPlayer.keys())
                    player_fight = input(">> ").lower()
                    print('Selected attack: ', player_fight)
                    attack_miss = randint(1,15)                                 #Chance the attack misses

                    if heal:
                        miss = False
                    elif attack_miss == 1:
                        miss = True
                    else:
                        miss = False

                    if miss:
                        player_fight = 0                                        #Player missed
                        print("Your attack missed!")
                        miss = False
                    else:
                        if player_fight in ('blowgun'):
                            incMiss = True
                            player_fight = itemsPlayer['blowgun']
                            print("\nYou used the blowgun. It dealt ", player_fight, " damage.")
                            print("\n%s has a higher chance of missing!"% (enemy.name))
                        elif player_fight in ('keyboard'):
                            player_fight = itemsPlayer['keyboard']
                            print("\nYou smacked", enemy.name, "with the keyboard. It dealt ", player_fight, " damage.")
                        elif player_fight in ('punch'):
                            player_fight = itemsPlayer['punch']
                            print("\nYou punched %s for %d damage!" % (enemy.name, player_fight))
                        elif player_fight in ('sword'):
                            if EName in 'Sentient computer':
                                print('The shining sword blinded the Sentient computer!')
                                player_fight = itemsPlayer['sword']
                                miss = True
                            else:
                                player_fight = itemsPlayer['sword']
                                print("\nThe sun glinted off the shining sword into %s's eye. It dealt %d damage." % (enemy.name, player_fight))
                        elif player_fight in ('heal'):
                            if self.health is 100:
                                print('Health is 100, can\'t heal any more!')
                                heal = True
                            else:
                                heal = True
                        else:
                            print("\nThat is not a valid move. Please try again.")
                            continue

                else:                                                           #Enemy's turn to attack
                    if self.health <= 0:
                        self.health = 0
                        winner = enemy.name
                        break
                    elif enemy.health <= 0:
                        enemy.health = 0
                        winner = self.name
                        break

                    if incMiss:
                        attack_miss = randint(1,2)
                    else:
                        attack_miss = randint(1,6)

                    if heal:
                        miss = False
                    elif attack_miss == 1:
                        miss = True
                    else:
                        miss = False

                    if miss:
                        enemy_fight = 0                                         #Enemy missed
                        print("\n%s's attack missed!" % enemy.name)
                        miss = False
                    else:
                        if EName in 'Computer':
                            if enemy.health > 30:
                                if self.health < 200 and self.health > 0:
                                    enemy_fight = itemsEnemy['whip']
                                    print("\nThe %s whipped you with a wire. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                            else:                                               #If computer.health < 30, 50% chance of healing
                                heal_or_fight = randint(1,2)
                                if heal_or_fight == 1:
                                    heal = True
                                    healAmt = randint(20,40)
                                    print("\n%s used heal. It healed for %d health" % (enemy.name, healAmt))
                                else:
                                    enemy_fight = itemsEnemy['whip']
                                    print("\nThe %s whipped you with a wire. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                        if EName in 'Giant bear':
                            if enemy.health > 30:
                                if self.health < 40 and self.health >= 20:
                                    enemy_fight = itemsEnemy['roar']
                                    print("\nThe %s roared at you. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                                elif self.health < 100 and self.health >= 80:
                                    enemy_fight = itemsEnemy['claws']
                                    print("\nThe %s clawed at you. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                                elif self.health < 80 and self.health >= 40:
                                    atk = ["claws","smack","roar"]
                                    atk = choice(atk)
                                    enemy_fight = itemsEnemy[atk]
                                    print("\nThe %s used %s. It dealt %d damage." % (enemy.name, atk, enemy_fight))
                                    cont = ''
                                    cont = input('')
                                else:
                                    enemy_fight = itemsEnemy['smack']
                                    print("\nThe %s smacked you with its paw. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                            else: #Heal
                                heal_or_fight = randint(1,2)
                                if heal_or_fight == 1:
                                    heal = True
                                    healAmt = randint(30,45)
                                    print("\n%s used heal. It healed for %d health" % (enemy.name, healAmt))
                                else:
                                    atk = ["claws","smack"]
                                    atk = choice(atk)
                                    enemy_fight = itemsEnemy[atk]
                                    print("\nThe %s used %s. It dealt %d damage." % (enemy.name, atk, enemy_fight))
                                    cont = ''
                                    cont = input('')
                        if EName in 'Sentient computer':
                            if enemy.health > 600:
                                if self.health <= 75 and self.health > 35:
                                    enemy_fight = itemsEnemy['whip']
                                    print("\nThe %s whipped you with a wire. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                                elif self.health >= 180:
                                    enemy_fight = itemsEnemy['virus']
                                    print("\nThe %s infected you with a virus. It dealt %d damage." % (enemy.name, enemy_fight))
                                    cont = ''
                                    cont = input('')
                                elif self.health > 75 and self.health < 180:
                                    atk = ["whip","glare"]
                                    atk = choice(atk)
                                    enemy_fight = itemsEnemy[atk]
                                    print("\nThe %s used %s. It dealt %d damage." % (enemy.name, atk, enemy_fight))
                                    cont = ''
                                    cont = input('')
                            else: #Heal
                                heal_or_fight = randint(1,2)
                                if heal_or_fight == 1:
                                    heal = True
                                    healAmt = randint(100,350)
                                    print("\n%s used heal. It healed for %d health" % (enemy.name, healAmt))
                                else:
                                    atk = ["whip"]
                                    atk = choice(atk)
                                    enemy_fight = itemsEnemy[atk]
                                    print("\nThe %s used %s. It dealt %d damage." % (enemy.name, atk, enemy_fight))
                                    cont = ''
                                    cont = input('')

                if heal:
                    if self.turn:
                        player_fight = itemsPlayer['heal']
                        print("%s healed" % self.name)
                        self.health += player_fight
                        if self.health > self.max_health:
                            self.health = self.max_health                       #Can't over heal
                    else:
                        enemy.health += healAmt
                        print("%s healed" % enemy.name)
                        if enemy.health > enemy.max_health:
                            enemy.health = enemy.max_health
                    heal = False
                    miss = False
                    print("\nYour health: %d\n%s's health: %d" % (self.health, enemy.name, enemy.health))
                else:
                    if self.turn:
                        enemy.health -= player_fight
                        if enemy.health < 0:
                            enemy.health = 0                                    #Minimum health is 0
                            winner = self.name
                            break
                    else:
                        self.health -= enemy_fight
                        if self.health < 0:
                            self.health = 0
                            winner = enemy.name
                            break
                    heal = False
                    miss = False

                #print("\nYour health: %d\n%s's health: %d" % (self.health, enemy.name, enemy.health))

                self.turn = not self.turn                                       #Turns switch
                enemy.turn = not enemy.turn

            #Determine winner===================================================
            if winner == self.name:
                print("\nYour health: %d \n%s's health: %d" % (self.health, enemy.name, enemy.health))
                print("\nYou defeated %s!!" % enemy.name)
                del self.place.enemies[person]
                if enemy.name == 'Computer':
                    Player.wonComp = True
                    print('You gained +50 max health!')
                    if self.health < self.max_health:
                        print('You have been healed!')
                    self.max_health = 100
                    self.health = self.max_health
                    if check_win_state(self):
                        print(WIN_MESSAGE)
                        strt = ''
                        strt = input('Press any key to continue...')
                        print(CREDITS)
                        exit()
                if enemy.name == 'Giant bear':
                    Player.wonBear = True
                    print('You gained +100 max health!')
                    if self.health < self.max_health:
                        print('You have been healed!')
                    self.max_health = 200
                    self.health = self.max_health
                    if check_win_state(self):
                        print(WIN_MESSAGE)
                        strt = ''
                        strt = input('Press any key to continue...')
                        print(CREDITS)
                        exit()
                if enemy.name == 'Sentient computer':
                    Player.wonFinal = True
                    if check_win_state(self):
                        print(WIN_MESSAGE)
                        strt = ''
                        strt = input('Press any key to continue...')
                        print(CREDITS)
                        exit()
                    else:
                        check_win_state(self)
                        if self.health < self.max_health:
                            print('You have been healed!')
                        self.max_health = 200
                        self.health = self.max_health
                play = False
                cont = ''
                cont = input('')
                print('What should we do now?')
                break
            else:
                enemy.health = enemy.max_health
                print("\nYour health: %d\n%s's health: %d" % (self.health, enemy.name, enemy.health))
                print("\nSorry %s, you were killed by the %s." %(self.name, enemy.name))
                end = ''
                end = input('')
                print(LOSE_MESSAGE)
                """
                strt = ''
                strt = input('Press any key to continue...')
                """
                print("Try again?")
                answer = input(">> ").lower()
                if answer in ("Yes","yes", "y"):
                    play = True
                    enemy.health = enemy.max_health
                    self.health = self.max_health
                    print()
                elif answer in ("No", "no", "n"):
                    play = False
                    print(CREDITS)
                    exit()
                else:
                    play = False
                    print(CREDITS)
                    exit()

        if check_win_state(self):
            print(WIN_MESSAGE)
            strt = ''
            strt = input('Press any key to continue...')
            print(CREDITS)
            exit()
        #return

    def interact_with(self, person):

        if type(person) != str:
            print('Person has to be a string.')
        elif person not in self.place.enemies:
            print('%s is not here.' % person)
        else:
            name = self.place.enemies[person].name
            print('%s says: %s' % (name, self.place.enemies[person].talk()))
            self.fight(person)

################################################################################
################################################################################
################################################################################


    def take(self, thing):

        if type(thing) != str:                                                  #If it's not the right format
            print('Thing should be a string.')
        elif thing in self.place.enemies or thing in self.place.exits:
            print("That is not an item!")
        else:
            item = self.place.things[thing]
            taken = self.place.take(thing)
            #print("thing:", thing)
            #print("Item:", item.name)
            #print("Taken thing:", taken.name)
            if taken is 0:                                                          #0 = item isn't at the place
                if tookbackpack(self) is False:
                    print('You don\'t have anything to carry it in!')
                if tookbackpack(self) is True:
                    print('That item is not here!')
            elif taken.name in 'backpack':                                          #If the item is the backpack
                #print("PLAYER TOOKBACKPACK TRUE")
                self.tookbackpack = True                                            #Now we have a backpack
                print(self.name, 'takes the', taken.name)
                #self.backpack.append(taken)
            elif tookbackpack(self) is False:                                       #If we don't have a backpack yet
                print('You don\'t have anything to carry it in!')
            elif tookbackpack(self) is True:                                        #If we have a backpack
                print(self.name, 'takes the', taken.name)
                self.backpack.append(taken)
            else:
                print('Error in take(Player): All other conditions were false')

    def check_backpack(self):
        for item in self.backpack:
            if item is backpack:                                                #If backpack item is inside backpack
                del self.backpack[item]                                         #Delete it from backpack

        if tookbackpack(self):                                                  #If we have a backpack
            if len(self.backpack) is 0:                                         #If backpack is empty
                print('Your backpack is empty!')
            else:                                                               #If backpack is not empty
                for item in self.backpack:                                      #Iterate thru backpack and print out items
                    print('   ', item.name, '-', item.description)
        else:                                                                   #If we don't have a backpack
            print('You don\'t have anything to carry it in!')
        return [item.name for item in self.backpack]


################################################################################
# Enemy Object #################################################################
################################################################################
class Enemy(object):
    def __init__(self, name, message, health, weapons):
        self.name = name
        self.message = message
        self.health = health
        self.max_health = health
        self.weapons = {weapon.name: weapon for weapon in weapons}
        self.turn = False

    def talk(self):
        return self.message


################################################################################
# Thing / Item Object ##########################################################
################################################################################
class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


################################################################################
# Place Object #################################################################
################################################################################
class Place(Player):
    def __init__(self, name, description, enemies, things):
        self.name = name
        self.description = description
        self.enemies = {enemy.name: enemy for enemy in enemies}
        self.things = {thing.name: thing for thing in things}
        self.exits = {} # {'name': (exit, 'description')}
        Player.tookbackpack = False

    def tookbackpack(self):
        if tookbackpack(self):
            return True
        else:
            return False

    def look(self):
        if self.name in 'sidewalk' or self.name in 'road':
            print('You are currently on the ' + self.name + '. You take a look around and see:')
        elif self.name in 'aisle1' or self.name in 'aisle2' or self.name in 'aisle3' or self.name in 'aisle4' or 'the dark':
            print('You are currently in ' + self.name + '. You take a look around and see:')
        elif self.name in 'alleyway':
            print('You are currently in an ' + self.name + '. You take a look around and see:')
        elif self.name in 'train exit' or self.name in 'tunnel' or self.name in 'end of the tunnel' or self.name in 'hallway' or self.name in 'unlocked room' or self.name in 'lobby':
            print('You are currently in the ' + self.name + '. You take a look around and see:')
        else:
            print('You are currently in a ' + self.name + '. You take a look around and see:')

        if not self.enemies and not self.things:
            print('nothing.')

        #Enemies
        if self.enemies:
            #print('enemies:')
            for enemy in self.enemies:
                print('   ', enemy)

        #Items
        if self.things:
            #print('Things:')
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)

        self.check_exits()

    def exit_to(self, exit):
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits:
            print(self.exits[exit][1])
            return self.exits[exit][0]
        else:
            print("Can't go to {} from {}.".format(exit, self.name))
            print("Try using the look command to see where to go.")
            return self

    def take(self, thing):
        if thing not in self.things:
            if Player.tookbackpack is False:
                #print('HERE1')
                #print('You don\'t have anything to carry it in!')              #Catch if thing isn't in the place
                return 0
            else:
                #print('HERE2')
                #print(thing, 'is not here.')                                   #Catch if the thing isn't in the place
                return 0
        elif thing in 'backpack':
        #elif self.things[thing] is backpack:                                    #If the item is the backpack
            #print("PLACE TOOKBACKPACK TRUE")
            Player.tookbackpack = True                                            #We now have a backpack
            obj = self.things[thing]
            del self.things[thing]                                              #Delete the backpack from inventory
            return obj
        else:
            if not Player.tookbackpack:                                           #If we haven't picked up the backpack
                #print('HERE3')
                return 0
            else:
                #print("HERE4")
                obj = self.things[thing]                                        #If the item isn't the backpack
                del self.things[thing]                                          #Return the item
                return obj

    def check_exits(self):
        print('You can go to:')
        for exit in self.exits:
            print('   ',exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)


#Things=========================================================================
# thing = Thing('name', 'description')
# Player items
backpack = Thing('backpack', 'This could come in handy.')
keyboard = Thing('keyboard', 'A bluetooth keyboard, I wonder where the rest of the computer is... (Damage: Low/High)')
blowdart = Thing('blowdart', 'We could use this if we had something to shoot it out of.(Damage: None)')
blowgun = Thing('blowgun', 'This could be useful.(Damage: Medium)')
sword = Thing('sword', 'Looks brand new, if only looks could kill.(Damage: High)')

# Bear items/abilities
claws = Thing('claws', 'the bear tries to mawl you with his claws!')
smack = Thing('smack', 'the bear smacked you')
roar = Thing('roar', 'the bear roared at you!')

# Computer items/abilities
whip = Thing('whip', 'the computer whips you with a wire!')

# FinalBoss items/abilities
#whip = Thing('whip', 'the computer whips you with a wire!')
glare = Thing('glare', 'the glare of the computer monitor is powerful')
virus = Thing('virus', 'it infected you with a virus!!')


#Enemies========================================================================
# enemy = Enemy('Name', 'Description', health, [weapons])
computer = Enemy('Computer', 'Mortal combat is my favorite game, let\'s play!', 100, [whip])
bear = Enemy('Giant bear', 'Rawr xD', 200, [claws, smack, roar])
finalBoss = Enemy('Sentient computer', 'I knew I smelled human, I thought we already eradicated all of you?', 2500, [whip, glare, virus])


#Places=========================================================================
# place = Place('Name', 'Description', [enemies], [things])
start = Place('an unfamiliar building', 'You woke up in this building. Mysterious...', [], [])
lobby = Place('lobby', 'The front door is wide open, maybe you should check out what\'s outside', [], [])
hallway1 = Place('hallway', 'There\'s only one room that\'s unlocked, you should go inside.', [], [])
hallway2 = Place('hallway', 'Doesn\'t look like there\'s anything else to explore here.', [], [])
room = Place('unlocked room', 'This room is a mess... looks like something with claws had a tantrum.', [], [backpack] )
road = Place('road', 'You are on a road in the middle of a city.', [], [])

bestbuy = Place('best buy', 'You are in a Best Buy store', [], [])
aisle1 = Place('aisle1', 'This aisle looks empty...', [], [])
aisle2 = Place('aisle2', 'This aisle looks empty...', [], [])
aisle3 = Place('aisle3', 'This aisle is filled with broken computer monitors.', [], [])
aisle4 = Place('aisle4', 'You look into the last aisle and you see a keyboard on the ground...', [computer], [keyboard])

alley = Place('alleyway', 'You are in a dark alleyway... ', [], [])
park = Place('park', 'You are in a park, unkempt and overgrown with plants.', [], [sword])
sidewalk = Place('sidewalk', 'You walk down a sidewalk with an itching feeling that something is watching you.', [], [])

subway = Place('subway system', 'A dark subway station with flickering lights', [], [blowgun])
train_station = Place('train station', 'Nobody seems to be around, but there\'s a patch of fur and blood on the ground', [], [])
train = Place('train', 'This train stopped right in its tracks, it has a gaping hole in it.', [], [])
train_exit = Place('train exit', 'You are in the back of the train.', [], [])
tunnel = Place('tunnel', 'Looks dark and scary... you hear something in the distance', [], [blowdart])
darkness = Place('the dark', 'You bravely travel deeper into the dark tunnel.', [], [])
deeper = Place('deeper in', 'You can barely see a light at the end of the tunnel.\nIt looks like something is barreling towards you!!!', [bear], [])
light = Place('end of the tunnel', 'You\'ve reached the end of the tunnel!', [], [])

start2 = Place('lobby', 'You leave the tunnel and enter the lobby of the building you woke up in. \nYou hear a noise down the hallway!\nIt sounds like it\'s coming from the same room you found that backpack in...', [], [])
hallway3 = Place('hallway', 'You peer into the room and see what looks to be some mesh of wires and flesh.', [finalBoss], [])

#Exits==========================================================================
# exit.add_exits([Place])
me = Player('Name', start, 50)
start.add_exits([hallway1, road])
lobby.add_exits([road, hallway2])
hallway1.add_exits([lobby, room])
room.add_exits([hallway2])
hallway2.add_exits([lobby, room])
road.add_exits([alley, bestbuy, lobby])

bestbuy.add_exits([road, aisle1, aisle2, aisle3, aisle4])
aisle1.add_exits([road, aisle2, aisle3, aisle4])
aisle2.add_exits([road, aisle1, aisle3, aisle4])
aisle3.add_exits([road, aisle1, aisle2, aisle4])
aisle4.add_exits([road, aisle1, aisle2, aisle3])

alley.add_exits([road, park])
park.add_exits([alley, sidewalk])
sidewalk.add_exits([park, subway])

subway.add_exits([sidewalk, train_station])
train_station.add_exits([subway, train])
train.add_exits([train_station, train_exit])
train_exit.add_exits([train, tunnel])
tunnel.add_exits([train_exit, darkness])
darkness.add_exits([tunnel, deeper])
deeper.add_exits([darkness, light])

light.add_exits([tunnel])
if Player.wonBear:
    light.add_exits([start2])
start2.add_exits([tunnel, hallway3])
hallway3.add_exits([start2])

#Player=========================================================================
# The Player should start at start.
#me = Player('Name', hallway, 5000)

################################################################################
# Parsing and Evaluation########################################################
################################################################################
def cmd_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command in ('talk', 'go'):
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_to', ' '.join(tokens[1:]))
    if command in ('interact'):
        if not tokens or tokens[0] != 'with':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_with', ' '.join(tokens[1:]))
    if command in ('use'):
        if not tokens or tokens[0] != 'blowgun' or tokens[0] != 'keyboard' or tokens[0] != 'sword':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command, ' '.join(tokens[1:]))
    elif command == 'check':
        if not tokens or tokens[0] != 'backpack':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS['check backpack']))
        return ('check_backpack', '')
    else:
        return (command, ' '.join(tokens))

def cmd_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    else:
        function(operand)
################################################################################
################################################################################
################################################################################

def tookbackpack(me):
    if me.tookbackpack:
        return True
    else:
        return False

def help():
    if not tookbackpack(me):
        print('There are {} possible commands:'.format(len(COMMAND_BASIC)))
        for usage in COMMAND_BASIC.values():
            print('   ', usage)
    else:
        print('There are {} possible commands:'.format(len(COMMAND_FORMATS)))
        for usage in COMMAND_FORMATS.values():
            print('   ', usage)

def check_win_state(player):
    if not Player.wonFinal or not Player.wonBear or not Player.wonComp:
        print('There\'s still more exploring to do.')
        return False

    if player.health <= 0:
        return False

    if player.place != hallway3:
        return False
    print()
    return True

########
# REPL #
########

def read_eval_print_loop():
    print(WELCOME_MESSAGE)

    ans = 'no'
    m = ''
    while ans != 'yes':
        me.name = input('What is your name? ')
        usrName = me.name
        print(me.name, 'is your name?')
        ans = input('yes/no: ')
        print('Are you sure', me.name, 'is your name?')
        ans = input('yes/no: ')
        print('Your memory is hazy, please be sure that', me.name, 'is your name.')
        m = input('I\'m sure/I\'m not sure: ')

    print('\nGreat, let\'s go over basic controls.')

    if not isinstance(me, Player):
        return

    help()
    print('As you progress, more commands will become available to you!')
    print('Be sure to type "help" if you ever need help.')

    strt = ''
    strt = input('\nPress any key to start>>')

    print(chr(27) + "[2J")
    print("You wake up in an unfamiliar building with a bump on your head...")

    while True:
        if check_win_state(me):
            print(WIN_MESSAGE)
            strt = ''
            strt = input('Press any key to continue...')
            print(CREDITS)
            exit()
            return

        print()

        try:
            line = input('>> ')
            exp = cmd_parse(line)
            cmd_eval(exp)

        except (KeyboardInterrupt, EOFError, SystemExit): #Quitting the game
            print('\nThanks for playing!')
            return

        #Syntax Errors
        except SyntaxError as e:
            print('ERROR:', e)


#Commands and Config============================================================

COMMAND_BASIC = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'interact': 'interact with [character]',
    'help': 'help',
}

COMMAND_FORMATS = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'interact': 'interact with [character]',
    'check backpack': 'check backpack',
    'help': 'help',
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'interact_with': 1,
    'check_backpack': 0,
    'help': 0,
}

SPECIAL_FORMS = {
    'help': help,
}

WELCOME_MESSAGE = """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                    ████████╗ ██████╗
                    ╚══██╔══╝██╔═══██╗
                       ██║   ██║   ██║
                       ██║   ██║   ██║
                       ██║   ╚██████╔╝
                       ╚═╝    ╚═════╝
            █████╗     ████████╗███████╗██╗  ██╗████████╗
           ██╔══██╗    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
           ███████║       ██║   █████╗   ╚███╔╝    ██║
           ██╔══██║       ██║   ██╔══╝   ██╔██╗    ██║
           ██║  ██║       ██║   ███████╗██╔╝ ██╗   ██║
           ╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
by James Garrett
"""

WIN_MESSAGE = """
  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$
 /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$|__  $$__//$$__  $$
| $$  \__/| $$  \ $$| $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$   | $$  | $$  \__/
| $$      | $$  | $$| $$ $$ $$| $$ /$$$$| $$$$$$$/| $$$$$$$$   | $$  |  $$$$$$
| $$      | $$  | $$| $$  $$$$| $$|_  $$| $$__  $$| $$__  $$   | $$   \____  $$
| $$    $$| $$  | $$| $$\  $$$| $$  \ $$| $$  \ $$| $$  | $$   | $$   /$$  \ $$
|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$| $$  | $$   | $$  |  $$$$$$/
 \______/  \______/ |__/  \__/ \______/ |__/  |__/|__/  |__/   |__/   \______/



 /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$  /$$$$$$  /$$   /$$ /$$
|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$ /$$__  $$| $$$ | $$| $$
 \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$| $$  \ $$| $$$$| $$| $$
  \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$| $$  | $$| $$ $$ $$| $$
   \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$| $$  | $$| $$  $$$$|__/
    | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$\  $$$
    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$ \  $$ /$$
    |__/    \______/  \______/       |__/     \__/ \______/ |__/  \__/|__/

You have successfully defeated all 3 enemies and saved the world, or something.
"""

CREDITS = """

 _____ _                 _           __            ______ _             _             _
|_   _| |               | |         / _|           | ___ \\ |           (_)           | |
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __  | |_/ / | __ _ _   _ _ _ __   __ _| |
  | | | '_ \\ / _` | '_ \\| |/ / __| |  _/ _ \\| '__| |  __/| |/ _` | | | | | '_ \ / _` | |
  | | | | | | (_| | | | |   <\\__ \\ | || (_) | |    | |   | | (_| | |_| | | | | | (_| |_|
  \\_/ |_| |_|\\__,_|_| |_|_|\\_\\___/ |_| \\___/|_|    \\_|   |_|\\__,_|\\__, |_|_| |_|\\__, (_)
                                                                   __/ |         __/ |
                                                                  |___/         |___/
 _____              _ _ _
/  __ \\            | (_) |      _
| /  \\/_ __ ___  __| |_| |_ ___(_)
| |   | '__/ _ \\/ _` | | __/ __|
| \\__/\\ | |  __/ (_| | | |_\\__ \\_
 \\____/_|  \\___|\\__,_|_|\\__|___(_)

   ___                             _____                     _   _
  |_  |                           |  __ \\                   | | | |
    | | __ _ _ __ ___   ___  ___  | |  \\/ __ _ _ __ _ __ ___| |_| |_
    | |/ _` | '_ ` _ \\ / _ \\/ __| | | __ / _` | '__| '__/ _ \\ __| __|
/\\__/ / (_| | | | | | |  __/\\__ \\ | |_\\ \\ (_| | |  | | |  __/ |_| |_
\\____/ \\__,_|_| |_| |_|\\___||___/  \\____/\\__,_|_|  |_|  \\___|\\__|\\__|

"""

LOSE_MESSAGE = """
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▄▄▄█████▓
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░
 ░ ░
"""

if __name__ == '__main__':
    read_eval_print_loop()