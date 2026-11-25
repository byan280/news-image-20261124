# Copy the daily news image into the output folder.
# The picture sits beside this script in the repo.
# Every run writes a byte-identical copy to /output/image.png.
# The script then prints the output file name, nothing else.
# The source path is resolved from this file's own location.
import os

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.png")
os.makedirs("/output", exist_ok=True)
with open(src, "rb") as f:
    data = f.read()
with open("/output/image.png", "wb") as f:
    f.write(data)
print("image.png")
