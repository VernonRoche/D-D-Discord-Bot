from Source.Player_Information.Character import Character


# transforms character file to array with usable values
def open_character(character, *args):
    for ar in args:
        if ar != "":
            print(ar)
            character = character + " " + ar

    path = "../Characters/" + character + ".txt"
    ftemp = open(path, "r")
    file = ftemp.read()
    ftemp.close()

    file = file.split('$')
    file[6] = file[6].split(',')
    file[6] = file[6][:-1]
    file[6] = [int(i) for i in file[6]]
    file[3] = int(file[3])
    file[4] = int(file[4])
    file[5] = int(file[5])
    file[9] = int(file[9])
    file[10] = file[10].split(',')
    file[10] = file[10][:-1]
    file[11] = file[11][1:]
    file[13] = file[13].split(',')
    file[13] = file[13][:-1]
    file[13] = [int(i) for i in file[13]]

    return file


# transforms an array representing a character into a Character Class instance
def file_to_character(character_file):
    return Character(character_file[0], character_file[1], character_file[2], character_file[3], character_file[4],
                     character_file[5], character_file[6], character_file[7], character_file[8], character_file[9],
                     character_file[10], character_file[11], character_file[12], character_file[13])


# checks if a text is too long for a single discord message
def is_long_text(text):
    if len(text) >= 1900:
        return True
    return False


# looks for the nearest text breaking character and returns it's location.
# look_for_format indicates if it must search the end of ``` for text formatting
def detect_endof_word(text, position, look_for_format):
    if look_for_format == False:
        counter = position
        for char in text[position:]:
            counter += 1
            if char == ' ' or char == ',' or char == '\n':
                return counter

    else:
        counter = position
        format_counter = 0
        for char in text[position:]:
            if char == '`':
                format_counter += 1
            counter += 1
            if format_counter == 3:
                return counter


# recursively separates a long text into an array of texts with 1900 or less words
def separate_long_text(text, look_for_format=False):
    if is_long_text(text):
        separator = detect_endof_word(text, 1900, look_for_format)
        left, right = text[:(separator + 1)], text[separator:]
        return [left] + separate_long_text(right)
    else:
        return [text]


# takes an array representing a character and saves it in a text file form
def save_char_file(file):
    filename = "../Characters/" + file[0] + ".txt"
    saves = open(filename, "w+")
    saves.write(file[0] + "$")
    saves.write(file[1] + "$")
    saves.write(file[2] + "$")
    saves.write(str(file[3]) + "$")
    saves.write(str(file[4]) + "$")
    saves.write(str(file[5]) + "$")
    for i in file[6]:
        saves.write(str(i) + ",")
    saves.write("$")
    saves.write(file[7] + "$")
    saves.write(file[8] + "$")
    saves.write(str(file[9]) + "$")
    for i in file[10]:
        saves.write(i + ",")
    saves.write("$")

    saves.write("@")
    for i in file[11]:
        saves.write(i + ",")
    saves.write("$")

    saves.write(file[12] + "$")
    for i in file[13]:
        saves.write(str(i) + ",")

    saves.close()


async def this_is_some_alien_bababouy(ctx):
    i = 0
    fuckfest = ""
    while (i < 25):
        fuckfest = fuckfest + ("<a:emoji_1:746866499729489950>")
        i = i + 1
    tab = separate_long_text(fuckfest)
    for x in tab:
        await ctx.send(x)
