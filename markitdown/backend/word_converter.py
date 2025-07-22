# word_converter.py

import io
import os
import aspose.words as aw
from interfaces import IDocumentConverter

class WordConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        # Load the Word document
        doc = aw.Document(file_path)

        # Define a temporary output markdown file
        md_output = "output.md"
        doc.save(md_output, aw.SaveFormat.MARKDOWN)

        # Read the markdown content
        with open(md_output, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        # Optionally delete the file afterward
        os.remove(md_output)

        return markdown_content

    def convert_to_json(self, file_path: str) -> str:
        raise NotImplementedError("Word to JSON conversion is not supported yet. Coming soon!")

    def convert_to_html(self, file_path: str) -> str:
        doc = aw.Document(file_path)
        stream = aw.io.MemoryStream()
        doc.save(stream, aw.SaveFormat.HTML)
        stream.seek(0)
        return stream.read().decode("utf-8")
