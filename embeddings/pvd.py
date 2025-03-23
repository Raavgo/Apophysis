from PIL import Image

from embeddings.embeddingbase import EmbeddingBase

class PVD(EmbeddingBase):
    def function(self, image:Image, executable:bytes) -> Image:
        pass