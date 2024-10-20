"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""
COLOUR_TO_HEX = {
    "Amaranth": "#e52b50",
    "Celadon": "#ace1af",
    "Fuchsia": "#ff00ff",
    "Indigo": "#4b0082",
    "Malachite": "#0bda51",
    "Periwinkle": "#ccccff",
    "Saffron": "#f4c430",
    "Sepia": "#704214",
    "Vermilion": "#e34234",
    "Viridian": "#40826d",
    "CustomColor": "#79cdcd"
}

color_name = input("Enter a color name: ").strip().upper()
while color_name != "":
    if color_name in COLOUR_TO_HEX:
        print(f"The hexadecimal code for {color_name} is {COLOUR_TO_HEX[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ").strip().upper()

print("Finished.")
