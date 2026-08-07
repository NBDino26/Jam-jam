# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Characters
define d = Character("Doyle")
define im = Character("")
define h = Character("Hester")
define g = Character("Grant")
define j = Character("Captain Jay")
define a = Character("Alek")
define l = Character("Lenore")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg whalewindow

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show doyle_neutral

    # These display lines of dialogue.

    d "I'm the dectective"

    h "I'm a biologist and also dead"

    g "I'm the geologist and eat rocks"

    j "I'm the Captain"



    # This ends the game.

    return
