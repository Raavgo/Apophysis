import os
import time

from embeddings.mp import MP
from utils.getter import get_next_image

from PIL import Image


if __name__ == '__main__':
    with open('test_executables/hello_world.exe', 'rb') as f:
        executable = f.read()
        embedding_metadata = MP()
        img = get_next_image((512, 512))
        img, meta =embedding_metadata(img, executable)
        img.save('test_executables/hello_world.png', format="png", pnginfo=meta)



