# One picture, one job: carry the daily news image to the output folder.
#
# The image lives next to this script. Each run drops an exact copy
# at /output/image.png, then reports the file name and nothing else.
# No arguments, no configuration, no surprises.
# The copy is byte-for-byte: no resizing, no re-encoding, no edits.
# The destination folder is created automatically when it is missing.
#
# Steps: find the picture, prepare the folder, copy, report.

from pathlib import Path
import shutil

here = Path(__file__).resolve().parent
picture = here / "image.png"

destination = Path("/output")
destination.mkdir(parents=True, exist_ok=True)

target = destination / picture.name
shutil.copyfile(picture, target)

print(target.name)
