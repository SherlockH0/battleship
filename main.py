numbers = "  󰎤 󰎧 󰎪 󰎭 󰎱 󰎳 󰎶 󰎹 󰎼 󰽽 "
letters = "󰬈󰬉󰬊󰬋󰬌󰬍󰬎󰬏󰬐󰬑"
blocks = "󱓼 󰯆󰿦󰅗󰵆󰌲󰇽󰐖󱗜"
ships = "󰵆󰌲󰇽󰐖󱗜"

ships = [
    {
        "size": 5,
        "x": 1,
        "y": 1,
        "rotate": False,
        "type": 0
    },
    {
        "size": 4,
        "x": 3,
        "y": 4,
        "rotate": True,
        "type": 1
    },
    {
        "size": 3,
        "x": 5,
        "y": 5,
        "rotate": False,
        "type": 2
    },
    {
        "size": 3,
        "x": 6,
        "y": 2,
        "rotate": False,
        "type": 3
    },
    {
        "size": 2,
        "x": 7,
        "y": 8,
        "rotate": False,
        "type": 4
    },
]


class bcolors:
    BLUE = '\033[34m'
    BLACK = '\033[2m'
    GRAY = '\033[40m'
    BLINK = '\033[5m'
    GREEN = '\033[46m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

for i in range(255):
    print(f"\033[{i}m" + f"{i} ", end="")
    print(bcolors.ENDC, end="")

def ships_to_dots(ships):

    dots = []
    for i in range(len(ships)):

        x = ships[i]['x']
        y = ships[i]['y']
        size = ships[i]['size']
        rotate = ships[i]['rotate']

        ship = {}

        if x <= 0 or y <= 0:
            print("Ship is out of the field!!")
            return

        if rotate:
            if x > 10 or y + size > 11:
                print("Ship is out of the field!!")
                return
            for j in range(size):
                ship[str(x - 1) + str(y - 1 + j)] = ships[i]["type"]
        else:
            if x + size > 11 or y > 10:
                print("Ship is out of the field!!")
                return
            for j in range(size):
                ship[str(x - 1 + j) + str(y - 1)] = ships[i]["type"]

        dots.append(ship)

    return dots


class Field():
    """Battle field"""

    def __init__(self, ships):
        self.field = [[0 for x in range(10)] for y in range(10)]

        for ship in ships:
            for pos, type in ship.items():

                self.field[int(pos[0])][int(pos[1])] = type + 5

    def draw(self, shaddow=False):
        print(bcolors.BLUE)
        print(" ╭" + "─" * 22 + "╮",)
        print(" │" + numbers + "│")

        for row in range(10):
            print(" │" + letters[row], end=" ")

            for block in self.field[row]:
                index = block


                if shaddow and block >= 5:
                    index = 0
                elif block == 1:
                    for ship in dots:

                        ...

                print(blocks[index], end=" ")

            print("│")
        print(" ╰" + "─" * 22 + "╯")


    def hit(self, x, y):
        x = x - 1
        y = y - 1

        if self.field[y][x] >= 5:
            self.field[y][x] = 4
            return 2

        elif self.field[y][x] == 0:
            self.field[y][x] = 3
            return 1

        else:
            return 0


dots = ships_to_dots(ships)
my_field = Field(dots)

messege = "Sea Battle"

while True:

    print()
    my_field.draw(True)
    print(bcolors.ENDC)
    print(bcolors.BLINK, bcolors.GREEN, end="")
    print("       " + messege + "       " + bcolors.ENDC)
    my_field.draw()

    pos = input("Enter hit position: ")
    if not(pos.isalnum() and len(pos) == 2):
        continue

    h = my_field.hit(int(pos[0]), int(pos[1]))

    if h == 0:
        messege = "You already shot this cell!"
    elif h == 1:
        messege = "MISS!"
    elif h == 2:
        messege = "HIT!"
