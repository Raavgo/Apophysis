import base64

from embeddings.embeddingbase import EmbeddingBase
from PIL import Image
from typing import override
import piexif

class MP(EmbeddingBase):
    @override
    def function(self, image:Image, executable:bytes) -> Image:
        
        encoded_executable = base64.b64encode(executable).decode('utf-8')
    
        #metadata dictionary
        metadata = {
            'Title': 'Embedded File',
            'Author': 'Valentina',
            'Description': encoded_executable
        }
        
        stegoimage = image.copy()
        stegoimage.info.update(metadata)
        
        return stegoimage