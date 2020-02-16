"""Final.py: A Text Adventure"""
__author__ = "James Garrett"
__credits__ = [""]
__email__ = "garretjb@mail.uc.edu"
from random import randint

class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0:
        print("%s The attack missed!" % (enemy.name, self.name))
    else:
        print("%s damages %s!" % (self.name, enemy.name))
    return enemy.health <= 0

class AI(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'a Computer'
        self.health = 1

class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10

  def quit(self):
    print("Suddenly a black hole forms, %s is sucked into oblivion." % self.name)
    print("""
    ___________   __
   / ____/  _/ | / /
  / /_   / //  |/ /
 / __/ _/ // /|  /
/_/   /___/_/ |_/
""")
    self.health = 0

  def help(self):
      print(Commands.keys())

  def stats(self):
      print("%s's health: %d/%d" % (self.name, self.health, self.health_max))

  def tired(self):
    print("%s feels tired." % self.name)
    self.health = max(1, self.health - 1)

  def heal(self):
    if self.state != 'normal':
        print("%s, maybe we should do something more productive." % self.name)
        self.enemy_attacks()
    else:
      print("%s is healed." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print("%s is interupted by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
            self.health = self.health_max
        else:
            print("%s slept too much." % self.name)
            self.health = self.health - 1

  def explore(self):
    if self.state != 'normal':
        print("%s is too busy right now!" % self.name)
        self.enemy_attacks()
    else:
        print ("%s explores a twisty passage." % self.name)
        if randint(0, 1):
            self.enemy = Enemy(self)
            print("%s encounters %s!" % (self.name, self.enemy.name))
            self.state = 'fight'
        else:
            if randint(0, 1): self.tired()

  def run(self):
    if self.state != 'fight':
        print ("%s fled the scene." % self.name)
        self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
          print ("%s runs from %s." % (self.name, self.enemy.name))
          self.enemy = None
          self.state = 'normal'
      else:
          print ("%s couldn't escape from %s!" % (self.name, self.enemy.name))
          self.enemy_attacks()

  def fight(self):
    if self.state != 'fight':
        print ("%s swats the air, without notable results." % self.name)
        self.tired()
    else:
        if self.do_damage(self.enemy):
            print ("%s executes %s!" % (self.name, self.enemy.name))
            self.enemy = None
            self.state = 'normal'
            if randint(0, self.health) < 10:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                print ("%s feels stronger!" % self.name)
        else:
            self.enemy_attacks()

  def enemy_attacks(self):
      if self.enemy.do_damage(self):
          print ("%s was killed by %s.\n" %(self.name, self.enemy.name))
          print("""
    ____    ____  ____
   / __ \  /  _/ / __ \
  / /_/ /  / /  / /_/ /
 / _, _/ _/ /_ / ____/
/_/ |_(_)___(_)_/   (_)
      """)

Commands = {
  'help': Player.help,
  'quit': Player.quit,
  'explore': Player.explore,
  'stats': Player.stats,
  'heal': Player.heal,
  'run': Player.run,
  'fight': Player.fight,
  }

p = Player()
print("""
    ___       ______          __     ___       __                 __
   /   |     /_  __/__  _  __/ /_   /   | ____/ /   _____  ____  / /___  __________
  / /| |      / / / _ \\| |/_/ __/  / /| |/ __  / | / / _ \\/ __ \\/ __/ / / / ___/ _ \\
 / ___ |     / / /  __/>  </ /_   / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
/_/  |_|    /_/  \\___/_/|_|\\__/  /_/  |_\\__,_/ |___/\\___/_/ /_/\\__/\\__,_/_/   \\___/
                                                                    by James Garrett
""")
print("You wake up in a building you aren't familiar with, it's thunderstorming outside.")
p.name = input("What is your name? ")
print("%s, type help to look at your options!\n" % p.name)


while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s doesn't understand the suggestion." % p.name)

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
