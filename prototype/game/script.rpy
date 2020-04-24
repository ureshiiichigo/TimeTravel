# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

default has_looped = False

label start:
    jump first_day

label first_day:
    scene bg room

    "Oh boy, time for your first big day at the Lorem Ipsum Academy for Dolor Sit Amet!"

    menu:
        "Now, which class did you have first...?"

        "Physics":
            jump physics
        "Art":
            jump art


label physics:
    "Ah, physics, the only science that isn't stamp collecting...                                     "
    "Ah, physics, the only science that isn't stamp collecting...(at least according to some asshole)."

    if has_looped:
        "You notice something strange in the corner...             "

        menu:
            "You notice something strange in the corner... Investigate?"

            "Yes":
                jump investigation
            "No":
                "You decide not to investigate the oddity."

    "But what's this!? Something strange is happening! You're going back in time!"

    $ has_looped = True
    jump first_day


label art:
    "You have a lovely time in art class making an ash tray for your parents."
    "Neither of them smoke; it's really just a way to show that you're thinking of them."

    jump subsequent_days


label subsequent_days:
    "The sun sets and then rises on a new morn..."
    window auto hide

    "Oh boy, time for your next big day at the Lorem Ipsum Academy for Dolor Sit Amet!"

    menu:
        "Now which class do you have today...?"

        "Physics":
            jump physics
        "Art":
            jump art


label investigation:
    "You look and discover a malfunctioning time machine in the corner of the room!"
    "Using your combined knowledge of mechatronics and advanced theoretical physics, you repair the time machine and restore order to the Academy."

    jump end


label end:
    "You've escaped the time loop! Thanks for playing :)"
    return
