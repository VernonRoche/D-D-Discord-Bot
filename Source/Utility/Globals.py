import youtube_dl

from Source.Story.StoryGenerator import *
# Global variable to check if a command needs to be cancelled
is_cancel_requested = False

# A bot manual called by the help command
bot_manual = ("```This is a list of possible commands:\n"
              "!help  |||  Bring up this panel\n"
              "\n"
              "Dice Player_Interaction: \n"
              "!dice <amount>d<sides> <modifier>  |||  Throws the given amount of dices, with specific sides. Modifier parameter is optional. Example: 3d6\n"
              "!dice  |||  Throws 1d20\n"
              "!init <character> or !initiative <character>  |||  Rolls an initiative roll for the given character\n"
              "!roll <skill> <character>  |||  Rolls 1d20 for a specific skill with the given character\n"
              "\n"
              "Listing Player_Interaction: \n"
              "!list  |||  List all created characters\n"
              "!show <character>  |||  Shows the character's sheet\n"
              "!delete <character>  |||  Deletes a character\n"
              "!weapons ||| Shows the available weapons and their stats"
              "!spells  |||  Lists all available spells\n"
              "!spellbook <character>  |||  Shows all the spells the character knows\n"
              "!spell <name of spell>  |||  Shows information on the asked spell\n"
              "!cast <spell> <character>  |||  Casts a given spell for the specific character. He must know it and have enough spell slots\n"
              "\n"
              "Private Chat Player_Interaction: \n" \
              "!create  |||  Create a character\n"
              "!bag <character>  |||  Opens up the bag management tab for the character\n"
              "!bank <character> or !money <character> |||  Opens up the bank\n"
              "\n"
              "Miscellaneous Player_Interaction: \n"
              "!bababouy  |||  Vibe check\n"
              "\n"
              "|||Brought to you by Alex Stergiou|||"
              "```")
####
#### Dictionary used to call functions related to story generation
####
stories_enum = {
    "CLUBPENGUIN": club_penguin,
    "HOLYWATER": holy_water,
    "MINORILLUSION": minor_illusion,
    "FIENDZONE": fiend_zone,
    "ABORTIONPREORDER": abortion_preorder,
    "CHICKENROAD": chicken_road,
    "WATERWIZARD": water_wizard,
    "IDENTITYTHEFT": identity_theft,
    "FRANCEBATHROOM": france_bathroom,
}

####
#### Global variables for music functions
####



ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}
