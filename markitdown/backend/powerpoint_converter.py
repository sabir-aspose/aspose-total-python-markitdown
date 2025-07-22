import os
import aspose.slides as slides
from interfaces import IDocumentConverter

class PowerPointConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        # Load the PowerPoint presentation
        with slides.Presentation(file_path) as pres:
            # Define a temporary output markdown file
            md_output = "output.md"
            pres.save(md_output, slides.export.SaveFormat.MD)

        # Read the markdown content
        with open(md_output, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        # Optionally delete the file afterward
        os.remove(md_output)

        return markdown_content

    def convert_to_json(self, file_path: str) -> str:
        raise NotImplementedError("PowerPoint to JSON conversion is not supported yet. Coming soon!")

    def convert_to_html(self, file_path: str) -> str:
        with slides.Presentation(file_path) as pres:
            # Define a temporary output HTML file
            html_output = "output.html"
            pres.save(html_output, slides.export.SaveFormat.HTML)

        with open(html_output, "r", encoding="utf-8") as f:
            html_content = f.read()

        os.remove(html_output)

        return html_content
