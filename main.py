# Copy the news image to /output, byte-for-byte, every run.
import os

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.png")
os.makedirs("/output", exist_ok=True)
with open(src, "rb") as f:
    data = f.read()
with open("/output/image.png", "wb") as f:
    f.write(data)
print("image.png")
