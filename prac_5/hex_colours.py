COLOUR_AND_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "aquamarine2": "	#76eec6", "aquamarine4": "#458b74",
                    "azure1": "#f0ffff"}

colour = input("Please enter a colour: ").lower()
while colour != "":
    if colour in COLOUR_AND_CODES:
        print(colour, "is", COLOUR_AND_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Please enter a colour: ").lower()

