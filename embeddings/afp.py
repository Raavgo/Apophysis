from PIL import Image

from embeddings.embeddingbase import EmbeddingBase

from PIL import Image
from embeddings.embeddingbase import EmbeddingBase
from typing import override

class AFP(EmbeddingBase):
    @override
    def function(self, image: Image, executable: bytes) -> Image:
        image = image.convert("RGBA")  # Ensure image has alpha channel
        payload = executable.hex() + chr(0)
        payload_bits = ''.join([f"{ord(c):08b}" for c in payload])
        data_index = 0
        width, height = image.size

        for y in range(height):
            for x in range(width):
                r, g, b, a = image.getpixel((x, y))
                if data_index < len(payload_bits):
                    a = (a & ~1) | int(payload_bits[data_index])
                    data_index += 1
                image.putpixel((x, y), (r, g, b, a))
                if data_index >= len(payload_bits):
                    break
            if data_index >= len(payload_bits):
                break
        return image

    @override
    def reverse_function(self, image: Image) -> bytes:
        image = image.convert("RGBA")
        width, height = image.size
        message_bits = []

        for y in range(height):
            for x in range(width):
                _, _, _, a = image.getpixel((x, y))
                message_bits.append(str(a & 1))

        message = ''.join(message_bits)
        chars = [message[i:i + 8] for i in range(0, len(message), 8)]
        decoded_message = ''.join([chr(int(char, 2)) for char in chars]).split(chr(0), 1)[0]
        return bytes.fromhex(decoded_message)

    @override
    def __set_limit_function(self, dims) -> None:
        self.limit = (dims[0] * dims[1]) // 8  # 1 bit per alpha channel
