# CODE: Embedding image into PNG metadata
from typing import override

from .embedding_base import Embedding_base

class metadata(Embedding_base):
    @override
    def function(self, x):
        pass

from PIL import Image
import base64
import os
# import png

# 1. Load PNG image
# 512 x 512 pixels
def load_png(image_file):
    with open(image_file, "rb") as f:
        return Image.open(f)

# Errorhandling for image
def load_png_errorhandling(image_file):
    # check if image exists
    if not os.path.exists(image_file):
        print(f"Error: Image {image_file} does not exist!")
        return None
    try:
        with open(image_file, "rb") as f:
            return Image.open(f)
    except Exception as e:
        print(f"Error while loading image: {e}")
        return None

# 2. Load textfile (later malware)
def load_input_file(input_file):
    with open(input_file, "r") as f:
        return f.read()

def load_input_file_errorhandling(input_file):
    # check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist!")
        return None
    try:
        with open(input_file, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Error while loading file: {e}")
        return None

# TODO: check size fo malware before embedding

# convert textfile to base64
def input_file_to_base64(input_file):
    with open(input_file, "rb") as f:
        file_data = f.read()
        return base64.b64encode(file_data).decode("utf-8")

    # check if conversion to base64 was successful
    try:
        with open(input_file, "rb") as f:
            file_data = f.read()
            return base64.b64encode(file_data).decode("utf-8")
    except Exception as e:
        print(f"Error occured while converting file in Base64: {e}")
        return None

# safe base64 encoded file in PNG metadata
def save_file_to_image(image, input_file, output_file):
  # load image
  # image = Image.open(image_file)
  # create base64 encoded file
  #base64_file = input_file_to_base64(input_file)
  # create metadata for the file
  metadata = {
    'Title': 'Embedded File',
    'Author': 'Valentina',
    'Description': input_file
  }
  # safe image in metadata
  # image.save(output_file, "PNG", pnginfo=metadata)

  # check if file was saved in image
  try:
        image.save(output_file, "PNG", pnginfo=metadata)
        print(f"File was saved in image successfully: {output_file}")
  except Exception as e:
        print(f"Error while saving image: {e}")

# 3. Extract file from PNG metadata
def extract_file_from_image(image_file, output_file):
  # load image and metadata
  image = Image.open(image_file)
  # extract metadata
  metadata = image.text
  # get base64 encoded file from metadata
  base64_file = metadata.get('Description', None)

  # check if metadata saved in image
  if base64_file is None:
    print("No data was found in metadata!")
    return

  # decode base64 encoded file data
  file_data = base64.b64decode(base64_file)
  # safe decoded file
  with open(output_file, "wb") as f:
    f.write(file_data)

  # check if decoding is successful
  try:
        file_data = base64.b64decode(base64_file)
  except Exception as e:
        print(f"Error while decoding Base64 data: {e}")
        return