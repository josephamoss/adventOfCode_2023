# 12 red cubes
# 13 green cubes
# 14 blue cubes

def parse(lines):
    for game in lines:
        print(game)




if __name__ == "__main__":
    filename = "test.txt"

    f = open(filename, "r")

    parse(f.readlines())
    # for line in f.readlines():
    #     print("test")

# Game 1: 1 blue, 1 red; 10 red; 8 red, 1 blue, 1 green; 1 green, 5 blue
# [ 
#  [{red:,},{}]
# ]
