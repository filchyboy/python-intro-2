from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
outside_text = '''
you are outside, there is a dark hole in the rock wall in front of you. 
There is a sign roughly nailed into the rock wall, it says 
'''

#dedented_text = textwrap.dedent(sample_text).strip()"

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def try_again():
    play_again = input(f"\n\nWould you like to play again? ")
    play_again = play_again.lower()
    if play_again == "y":
        adventure_begins()
    else:
        print(f"\n\nBye!")
        exit()

def space_happens(player, choice):   
    pass

def adventure_begins():
    player_name = input("\nWelcome to my random dungeon! What shall I call you? ")
    current_player = Player(player_name, "outside")
    state_of_play = True
    while state_of_play == True:
        print(f"\n\nYou, {current_player.name.title()} are at the {room[current_player.room].name}. {room[current_player.room].description}")

        next_step = input(f"\n\n{current_player.name.title()}, where will you go? ")
        next_step.lower()
        query = ["q", "quit", "h", "help", "n", "north", "e", "east", "s", "south", "w", "west"]
        for _ in range(len(query)):
            if next_step == query[_]:
                if query[_] == "q" or query[_] == "quit":
                    try_again()
                if query[_] == "h" or query[_] == "help":
                    pass
                if query[_] == "n" or query[_] == "north":
                    if current_player.room == "outside":
                        current_player = Player(player_name, "foyer")
                    elif current_player.room == "foyer":
                        current_player = Player(player_name, "overlook")
                    elif current_player.room == "narrow":
                        current_player = Player(player_name, "treasure")
                    else:
                        print("There's a wall there silly!")
                if query[_] == "e" or query[_] == "east":
                    if current_player.room == "foyer":
                        current_player = Player(player_name, "narrow")
                    else:
                        print("There's a wall there silly!")
                if query[_] == "s" or query[_] == "south":
                    if current_player.room == "foyer":
                        current_player = Player(player_name, "outside")
                    elif current_player.room == "overlook":
                        current_player = Player(player_name, "foyer")
                    elif current_player.room == "treasure":
                        current_player = Player(player_name, "narrow")
                    else:
                        print("There's a wall there silly!")
                if query[_] == "w" or query[_] == "west":
                    if current_player.room == "narrow":
                        current_player = Player(player_name, "foyer")
                    else:
                        print("There's a wall there silly!")


    



adventure_begins()



# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
