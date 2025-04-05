import numpy as np
import brotli
import zlib
import bz2
import lzma
from PIL import Image
from brotli import decompress
#from multipledispatch import dispatch

class EmbeddingBase:
    def __init__(self):
        self.ctr = 0
        self.limit = -1
        self.mode = ['brotli', 'lzma', 'bz2', 'zlib']

    def __call__(self, img:Image, executable:bytes) -> Image:
        compress = self.__compress(executable)
        self.__set_limit_function(img.size)
        if not self.__can_embed(compress):
            raise Exception('File cannot be embedded')
        return self.function(img, compress)

    def function(self, image:Image, executable:bytes) -> Image:
        pass

    def reverse_function(self,image:Image) -> bytes:
        pass

    def __set_limit_function(self, dims) -> None:
        pass

    def reverse(self, image:Image) -> Image:
        data = self.reverse_function(image)
        return self.__decompress(data)

    def __can_embed(self, compressed:bytes) -> bool:
        if self.limit == -1:
            return True

        return len(compressed) <= self.limit

    def __compress(self, executable) -> bytes:
        mode = self.mode[self.ctr % len(self.mode)]
        print(mode)
        self.ctr += 1

        if mode == 'brotli':
            return b'R' + brotli.compress(executable)
        elif mode == 'lzma':
            return b'L' + lzma.compress(executable)
        elif mode == 'bz2':
            return b'B' + bz2.compress(executable)
        elif mode == 'zlib':
            return b'Z' + zlib.compress(executable)
        else:
            raise ValueError(f"Unsupported compression mode: {mode}")

    def __decompress(self, data: bytes) -> bytes:
        if not data:
            raise ValueError("Empty input data")

        method = data[0:1]
        compressed = data[1:]

        if method == b'Z':
            return zlib.decompress(compressed)
        elif method == b'B':
            return bz2.decompress(compressed)
        elif method == b'L':
            return lzma.decompress(compressed)
        elif method == b'R':
            return brotli.decompress(compressed)
        else:
            raise ValueError(f"Unknown compression method byte: {method}")