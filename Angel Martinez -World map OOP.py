class Room(object):
    def __init__(self, name, north, east, west, south, up, down, description):
        self.name = name
        self.north = north
        self.east = east
        self.west = west
        self.south = south
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Intialize Room
west_house = Room("West of house", 'north_house', 'east_house', None, 'south_house', None, None,
                  "Insert description here")
south_house = Room("South of house")

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']


while True:
    print(current_node)
    print(current_node)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')
    print()