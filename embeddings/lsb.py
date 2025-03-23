from PIL import Image

from embeddings.embeddingbase import EmbeddingBase

class LSB(EmbeddingBase):
    def function(self, image:Image, executable:bytes) -> Image:
        pass