import random
from PIL import Image
from embeddings.embeddingbase import EmbeddingBase
from typing import override

class RLSB(EmbeddingBase):
    def __init__(self, seed: int = 42):
        super().__init__()
        self.seed = seed

    @override
    def function(self, image: Image, executable: bytes) -> Image:
        payload = executable.hex() + chr(0)
        payload_bits = ''.join(f"{ord(c):08b}" for c in payload)
        width, height = image.size
        total_pixels = width * height

        positions = [(x, y) for y in range(height) for x in range(width)]
        random.Random(self.seed).shuffle(positions)

        data_index = 0
        for x, y in positions:
            if data_index >= len(payload_bits):
                break
            pixel = list(image.getpixel((x, y)))
            for i in range(3):  # R, G, B
                if data_index < len(payload_bits):
                    pixel[i] = (pixel[i] & ~1) | int(payload_bits[data_index])
                    data_index += 1
            image.putpixel((x, y), tuple(pixel))

        return image

    @override
    def reverse_function(self, image: Image) -> bytes:
        width, height = image.size
        total_pixels = width * height

        positions = [(x, y) for y in range(height) for x in range(width)]
        random.Random(self.seed).shuffle(positions)

        message_bits = []
        for x, y in positions:
            pixel = image.getpixel((x, y))
            for i in range(3):
                message_bits.append(str(pixel[i] & 1))

        bits = ''.join(message_bits)
        chars = [bits[i:i + 8] for i in range(0, len(bits), 8)]
        decoded = ''.join(chr(int(c, 2)) for c in chars).split(chr(0), 1)[0]

        return bytes.fromhex(decoded)

    @override
    def __set_limit_function(self, dims) -> None:
        self.limit = (dims[0] * dims[1] * 3) // 8
