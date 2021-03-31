import glob


async def is_valid(ctx, arg, name):
    tempspells = [f for f in glob.glob("Spells/" + "**/*.txt", recursive=True)]
    spells = ""
    for f in tempspells:
        f = f.lower()
        spells = spells + "," + f[7:-4]
    spells = spells[1:]

    tempclasses = [f for f in glob.glob("Character Classes/" + "**/*.txt", recursive=True)]
    classes = ""
    for f in tempclasses:
        f = f.lower()
        classes = classes + "," + f[18:-4]
    classes = classes[1:]

    if name == "hp" and arg <= 0:
        await ctx.send("``You donkey! You are not dead yet!``")
        raise ValueError("bad hp")
    if (name == "attribute" or name == "level") and (arg <= 0 or arg > 20):
        await ctx.send("``You master donkey! Put an attribute value between 0 and 20!``")
        raise ValueError("bad attr or level")
    if name == "coins" and arg < 0:
        await ctx.send("``Good news for you, you are not indebted, so get that negative money away from my eyes!``")
        raise ValueError("bad coins")
    if name == "initiative" and (arg < -10 or arg > 10):
        await ctx.send("``What is even this initiative value you donkey?!``")
        raise ValueError("bad init")
    if name == "skill" and (arg != "dnd" and
                            arg != "acrobatics" and arg != "athletics" and arg != "sleight of hand" and arg != "stealth" and
                            arg != "arcana" and arg != "history" and arg != "investigation" and arg != "nature" and
                            arg != "religion" and arg != "animal handling" and arg != "insight" and arg != "medicine" and
                            arg != "perception" and arg != "survival" and arg != "deception" and arg != "intimidation" and
                            arg != "performance" and arg != "persuasion"):
        await ctx.send("``Enter a correct skill name!``")
        raise ValueError("bad skillname")
    if name == "spell" and (arg not in spells) and arg != "dnd":
        await ctx.send("``This spell does not exist! If your spell has 2 or more words, separate them with -``")
        raise ValueError("bad spell")
    if name == "class" and (arg not in classes):
        await ctx.send("``This class does not exist!``")
        raise ValueError("bad class")