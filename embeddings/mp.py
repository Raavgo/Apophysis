import base64

from embeddings.embeddingbase import EmbeddingBase
from PIL import Image, PngImagePlugin
from typing import override


class MP(EmbeddingBase):
    @override
    def function(self, image:Image, executable:bytes) -> (Image, bytes):
        encoded_executable = base64.b64encode(executable).decode('utf-8')
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("Title", "Embedded File")
        metadata.add_text("Description", encoded_executable)
        
        return image, metadata