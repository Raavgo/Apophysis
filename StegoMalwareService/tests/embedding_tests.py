import os
import sys
import importlib
from pathlib import Path
from PIL import Image
path = str(Path(__file__).resolve().parent.parent)
sys.path.append(path)
embedding_classes = {}

if __name__ == "__main__":
    embeddings_path = os.path.join(path, "embeddings")

    for root, _, files in os.walk(embeddings_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]  # Remove .py extension
                relative_module =""
                try:
                    # Construct the full import path
                    relative_module = f"embeddings.{module_name}"
                    # Dynamically import the module
                    module = importlib.import_module(relative_module)

                    # Search for classes that inherit from EmbeddingBase
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if isinstance(attr, type) and issubclass(attr,module.EmbeddingBase) and attr is not module.EmbeddingBase:
                            embedding_classes[attr_name] = attr
                            print(f"Successfully imported class: {attr_name} from {relative_module}")
                except Exception as e:
                    print(f"Failed to import {relative_module}: {e}")

    for class_name, cls in embedding_classes.items():
        try:
            instance = cls()
            print(f"\nUsing class: {class_name}")

            # Mock image and executable data for testing
            mock_image = Image.new('RGB', (100, 100))
            mock_executable = b"Test executable data"

            # Check and call the function method
            if hasattr(instance, "function"):
                encoded_image, metadata = instance(mock_image, mock_executable)
                print(f"Function output for {class_name}: {metadata}")

            # Check and call the reverse_function method
            if hasattr(instance, "reverse_function"):
                recovered_data = instance.reverse_function(mock_image)
                print(f"Reverse function output for {class_name}: {recovered_data}")

        except Exception as e:
            print(f"Error using class {class_name}: {e}")