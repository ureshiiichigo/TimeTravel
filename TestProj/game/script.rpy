# The script of the game goes in this file.

init:
    $ charcenter = Position(xpos=.5, xanchor=0.5, ypos=.3, yanchor=0.5)
    $ charright = Position(xpos=0.9, xanchor=1.0, ypos=.3, yanchor=0.5)

image momdad happy = "images/elliot.png"
image fluffy = im.Scale("images/SneakyBallerina.jpg", 300, 400)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Mother = Character("Mom")
define Father = Character("Dad")

define player_name = "Elliot"

define Player = Character(_(player_name),
    show_side_image=Image("images/eileen_side.png", xalign=0.1, yalign=1.0))

define pro_subj = "they"
define pro_obj = "them"
define pro_poss = "their"
define pro_poss2 = "theirs"
define pro_ref = "themselves"
define verbplural = True

define pro_Subj = pro_subj.capitalize()
define pro_Poss = pro_poss.capitalize()
define pro_Poss2 = pro_poss2.capitalize()

# The game starts here.

label start:

    scene black
        
    $ player_name = renpy.input("What's your name?", "Elliot")
    $ player_name = player_name.strip()
    $ Player = Character(_(player_name), show_side_image=Image("images/eileen_side.png", xalign=0.1, yalign=1.0))

label ask_pronouns:

    menu:
        "I use they/them/theirs.":
            jump story
        "I use he/him/his.":
            $ pro_subj = "he"
            $ pro_obj = "him"
            $ pro_poss = "his"
            $ pro_poss2 = "his"
            $ pro_ref = "himself"
            $ verbplural = False
            jump set_pronouns
        "I use she/her/hers.":
            $ pro_subj = "she"
            $ pro_obj = "her"
            $ pro_poss = "her"
            $ pro_poss2 = "hers"
            $ pro_ref = "herself"
            $ verbplural = False
            jump set_pronouns
#        "I want to set my own!":
#            "Sorry, we don't actually have that functionality yet."
#            jump ask_pronouns
                
            
label set_pronouns:
    $ pro_Subj = pro_subj.capitalize()
    $ pro_Poss = pro_poss.capitalize()
    $ pro_Poss2 = pro_poss2.capitalize()

label story:

    show text "Week Zero" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    
    show text "Monday" at truecenter
    with dissolve
    pause 2
    hide text

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "mother_happy.png" to the images
    # directory.

    show momdad happy at charcenter with move

    # Drive up to college. Brother is sitting in seat next to you. Parents are in the front. Mom looks back at you.
    
    Father "Are we there yet?"
    Mother "Google says fifteen minutes."
    Father "Are we there yet?"
    Mother "No."
    Father "Are we th--"
    Mother "I will hit you."
    Father "Can't hit the driver."
    Mother "I will hit you anyway, and the car will crash, and all of us will die, but you will no longer be asking stupid questions."
    Father "Think of the children."

    "In the seat next to you, your brother is engrossed in playing on his handheld."

    Mother "How you doing, honey? Nervous?"
    
    "Yes."
    
    Player "No."
    Father "I know you'll do fine, sweetheart."
    Mother "And home is just a phone call away."
    Father "We might even do your laundry for you."
    Mother "Speak for yourself."
    
    menu:
        "I'll miss you too.":
            jump choice1a
        "You're embarrassing me.":
            jump choice1b
        "Don't worry about me.":
            jump choice1c

label choice1a:
    Player "How soon can I come home? Is tomorrow good?"
    Father "Well, let me check my busy calendar—"
    Mother "Shush, the locksmith is coming tomorrow, we can't let [pro_obj] come back before then."
    Player "Very funny."
    if verbplural:
        Mother "[pro_Subj] think I'm kidding."
    else:
        Mother "[pro_Subj] thinks I'm kidding."
        
    jump choice1end

label choice1b:
    Player "Stop it, someone might overhear your smothering."
    Father "But [player_name]! How will we live without your sunny presence in our daily lives!"
    Mother "Be thankful he hasn't started weeping."
    Father "Remember Uncle Joe's wedding? God, that was a good one."

    jump choice1end

label choice1c:
    Player "I'm an adult now. I can take care of myself."
    Mother "Hmmm, remember that time you tried to microwave a pie plate?"
    Father "Oh, or the time [pro_subj] ate an entire tray of brownies and couldn’t look at chocolate for over a month without gagging?"
    Mother "Or the time—"

    jump choice1end
    
label choice1end:
    Player "That's it, I'm officially disinheriting you. Can I disinherit my parents?"
    Mother "Remember who helped you steal those cookies last week."
    Father "Hey! Those were earmarked!"
    Mother "Remember the last time that [player_name] tried to earmark cookies, and you ate [pro_poss] cookies anyway?"
    Father "[pro_Subj] brought it upon [pro_ref]."
    
    "Maybe you won't miss them as much as you thought you would."
    
    #Player "Alright, losers, get out of my room."
    
    
    
    
    
    
    "Your brother shoots you a look, but you're too busy being smothered by your mother's hug to figure out what it means."

    Mother "I mean it, [player_name]. You call if you ever feel overwhelmed."

    "\[MOM has been added to your contacts list.\]"

    hide momdad with dissolve
    
    "Once your parents are gone, you take a deep breath and collapse on the bed. Finally."

    Player "Ugh. Orientation is tomorrow. I should look at my schedule..."

    #Schedule button is highlighted. When the user clicks, they see an agenda pop up.

    show text "Tuesday, August 29" + '\n' + "11a Freshman orientation" at truecenter
    
    "\[Schedule\]"

    Player "I am so not prepared for this."

    hide text with dissolve

    "You set your alarm for ten thirty, just in case, and dig your toothbrush out of a cardboard box, cheerfully labeled as \"bathroom :)\" by your mother."
    "You’re too tired to deal with braving the shared bathroom, so you brush your teeth without using toothpaste and strip down to your shirt and underwear."
    "You’re pretty much ready to collapse on the bed and pass out, but first you need to unpack something. You root around in your backpack until you find what you’re looking for."

    show fluffy at charcenter with dissolve

    "Sir Fluffy, your faithful companion for the last eighteen years, will help you get to sleep. Who needs a college roommate when you have your best friend at your side?"

    "You flick off the light and crawl under the covers, and try not to think about tomorrow. It’ll come soon enough."

    scene black with dissolve

    show text "Tuesday" at truecenter
    with dissolve
    pause 2
    hide text

    #Alarm music plays

    scene bg room

    "You bat at your cellphone until it stops bleating and sit up. It takes you a moment to remember where you are."

    Player "...Ugh."
    Player "Five more minutes."
    
    scene black with dissolve
    pause 2
    scene bg room with move
    
    #Alarm music plays

    Player "Argh!"
    
    "With some reluctance, you get out of bed and start getting dressed."
    "Brushing your hair sounds like too much effort, so you slip on your shoes and grab your keys and phone before heading down to..."
    "Crap, where are you going again?"

    scene bg exit
    with dissolve
    
    "This concludes the demo! We hope you enjoyed playing."

    # This ends the game.

    return
