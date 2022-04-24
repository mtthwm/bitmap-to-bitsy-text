from PIL import Image
import sys

ALT_PIX = (0, 0, 0, 255)
BLANK = \
"00000000\n"+\
"00000000\n"+\
"00000000\n"+\
"00000000\n"+\
"00000000\n"+\
"00000000\n"+\
"00000000\n"+\
"00000000\n"
BLANK_VALUE = "0"

filenames_start_at = int((len(sys.argv) / 2) + 1)
filenames = sys.argv[filenames_start_at:]
suffixes = sys.argv[1:filenames_start_at]
tilemap = {}

with open("output.txt", "w") as output:
    for i in range(len(filenames)):
        suffix = suffixes[i]
        filename = filenames[i]

        img = Image.open(filename)
        height, width = img.size


        output.write(f"ROOM {suffix}\n")

        # Loops which iterate over tiles
        for y in range(0, height, 8):
            for x in range(0, width, 8):

                current_tile = ""
        
                # Read individual tiles
                for j in range(8):
                    for i in range(8):
                        px = img.getpixel((x+i, y+j))

                        if (px != ALT_PIX):
                            current_tile += "1"
                        else:
                            current_tile += "0"

                    current_tile += "\n"

                # If the tile is completely blank, replace it with the constant "0"
                if current_tile != BLANK:
                    # Add tile to the tilemap, if it doesn't already occur
                    
                    if not current_tile in tilemap.keys():
                        tilemap[current_tile] = f"{x+i}_{y+j}_" + suffix

                    output.write(f"{tilemap[current_tile]}")

                else:
                    output.write(BLANK_VALUE)

                # Add comments and line breaks as necessary
                if (x + i + 1) % width == 0:
                    output.write("\n")
                else:
                    output.write(",")

        output.write("\n")

    for key, value in tilemap.items():
        output.write(f"TIL {value}\n{key}\n")