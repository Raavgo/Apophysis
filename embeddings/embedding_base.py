import numpy as np
import brotli
from PIL import Image
class Embedding_base:
    def __init__(self, limit=-1):
        self.ctr = 0
        self.limit = limit

    def __call__(self, img, executable) -> Image:
        compress = self._compress(executable)
        return self.function(img, compress)

    def function(self, image, executable) -> Image:
        pass

    def _compress(self, executable) -> bytes:
        pass