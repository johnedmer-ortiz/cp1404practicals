COLOUR_TO_HEX = {"Army Green": "#4b5320", "Arylide Yellow": "#e9d66b", "Ash Grey": "#b2beb5",
                 "Asparagus": "#87a96b", "Aureolin": "#fdee00", "Baby Blue": "#89cff0",
                 "Baker-Miller Pink": "#ff91af", "Banana Mania": "#fae7b5", "Barn Red": "#7c0a02",
                 "Battleship Gray": "#848482"}

colour = input("Enter colour: ").lower().title()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(f"{colour} hex code is {COLOUR_TO_HEX[colour]}")
    else:
        print("Invalid color")
    colour = input("Enter colour: ").lower().title()
