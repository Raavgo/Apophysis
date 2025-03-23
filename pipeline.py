import os
import subprocess
import time
import base64
import tempfile

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
        img = Image.open('test_executables/hello_world.png')
        b64_string = embedding_metadata.reverse_function(img)

        exe_data = base64.b64decode(b64_string)

        # Step 2: Write to temporary file
        with open("tmp.exe", "wb") as temp_exe:
            temp_exe.write(exe_data)


        subprocess.run(["tmp.exe"], check=True)



