import sys
import os
from PIL import Image

# 1) grab first and second argument.
first = sys.argv[1]
second = sys.argv[2]

# 2)  check if new/ exists, if not create it.
if not os.path.exists(second):
    os.mkdir(second)
else:
    print("This folder already exists.")

# 3) loop through entire given folder.
for file in os.listdir(first):
    full_path = os.path.join(first, file)

    # 4) convert images to png.
    image = Image.open(full_path)

    # 5) save to the new folder.
    removed_extension = os.path.splitext(file)[0]
    image.save(f"{second}{removed_extension}.png", "png")
    print("All done")
