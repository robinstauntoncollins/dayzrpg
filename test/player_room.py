import config
from Room import Location
from Player import Player
from parseCommand import dayzrpgcmd
def play():
    pl = Player()
    cl = Location(config.starting_location)
    #print(cl.intro_text())
    while pl.is_alive():
        cl = Location(pl.location)
        print(cl.intro_text())
        dayzrpgcmd().cmdloop()
        

def move(player,room):
    direction = str(input("Enter a direction to move: "))
    player.move_direction(direction,room)
                

if __name__ == '__main__':
    print('='*5+" DayZ RPG "+'='*5)
    print('='*18)
    print()
    print('(Type "help" for commands.)')
    print()
    pl = Player()
    cl = Location(config.starting_location)
    dayzrpgcmd().cmdloop()
    print("Thanks for playing")
