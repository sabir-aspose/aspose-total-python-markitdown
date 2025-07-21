# markdown_postprocessor.py

import base64
import os
import re
from interfaces import IMarkdownPostProcessor
from PIL import Image
import pytesseract

class MarkdownPostProcessor(IMarkdownPostProcessor):
    def remove_images(self, markdown: str) -> str:
        return re.sub(r'!\[.*?\]\(.*?\)', '', markdown)

    def encode_images_base64(self, markdown: str, base_path: str) -> str:
        def embed(match):
            alt_text, img_path = match.groups()
            full_path = os.path.join(base_path, img_path)

            if not os.path.isfile(full_path):
                return match.group(0)

            with open(full_path, 'rb') as f:
                encoded = base64.b64encode(f.read()).decode('utf-8')
                ext = os.path.splitext(full_path)[1][1:]  # "png", "jpg"
                return f'![{alt_text}](data:image/{ext};base64,{encoded})'

        return re.sub(r'!\[(.*?)\]\((.*?)\)', embed, markdown)

    def ocr_images(self, markdown: str, base_path: str) -> str:
        def extract_text(match):
            alt_text, img_path = match.groups()
            full_path = os.path.join(base_path, img_path)

            if not os.path.isfile(full_path):
                return match.group(0)

            try:
                text = pytesseract.image_to_string(Image.open(full_path)).strip()
                return f'**Extracted Text:** {text}'
            except Exception:
                return match.group(0)

        return re.sub(r'!\[(.*?)\]\((.*?)\)', extract_text, markdown)
