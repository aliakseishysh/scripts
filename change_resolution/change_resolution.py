from PIL import Image
import sys

image = Image.open(sys.argv[1])
image.save(sys.argv[2], dpi=(sys.argv[3], sys.argv[4]))