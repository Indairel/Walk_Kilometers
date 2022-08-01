def add_new():
    new_word = input('Hello, how much did you walk today ?')

    f = open("../Walk_Kilometers/distance.txt", "a")
    f.write(str(new_word) + '\n')
    f.close()


def how_much_already():
    variable = {}
    with open('distance.txt', 'r') as file:
        for line in file:
            name, _, value = line.partition('=')
            variable[name.strip()] = value.strip()

    print('You have already walked' + variable['base'])