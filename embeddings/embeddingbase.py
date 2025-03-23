import numpy as np
import brotli
import zlib
import bz2
import lzma
from PIL import Image

class EmbeddingBase:
    def __init__(self, limit=-1):
        self.ctr = 0
        self.limit = limit
        self.mode = ['brotli', 'lzma', 'bz2', 'zlib']

    def __call__(self, img, executable) -> Image:
        compress = self.__compress(executable)

        if not self.__can_embed(compress):
            raise Exception('File cannot be embedded')
        return self.function(img, compress)

    def function(self, image:Image, executable:bytes) -> Image:
        pass

    def __can_embed(self, compressed:bytes) -> bool:
        if self.limit == -1:
            return True

        return len(compressed) <= self.limit

    def __compress(self, executable) -> bytes:
        mode = self.mode[self.ctr % len(self.mode)]
        self.ctr += 1

        if mode == 'brotli':
            return brotli.compress(executable)
        elif mode == 'lzma':
            return lzma.compress(executable)
        elif mode == 'bz2':
            return bz2.compress(executable)
        elif mode == 'zlib':
            return zlib.compress(executable)
        else:
            raise ValueError(f"Unsupported compression mode: {mode}")