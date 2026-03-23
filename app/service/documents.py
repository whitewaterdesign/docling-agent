from io import BytesIO

from docling.datamodel.base_models import DocumentStream
from docling.document_converter import DocumentConverter


class DocumentService:
    def __init__(self, converter: DocumentConverter):
        self.converter = converter

    @staticmethod
    def _create_stream(name: str, stream: BytesIO) -> DocumentStream:
        return DocumentStream(name=name, stream=stream)

    def convert_to_md(self, name: str, stream: BytesIO) -> str:
        """Convert a document to markdown format.

        Args:
            name: The document filename.
            stream: The document bytes.

        Returns:
            The document content as markdown.
        """
        result = self.converter.convert(self._create_stream(name, stream))
        return result.document.export_to_markdown()

    def convert_to_json(self, name: str, stream: BytesIO) -> str:
        """Convert a document to Docling's DoclingDocument JSON schema.

        Args:
            name: The document filename.
            stream: The document bytes.

        Returns:
            The document content as JSON.
        """
        result = self.converter.convert(self._create_stream(name, stream))
        return result.document.export_to_dict()

    def convert_to_html(self, name: str, stream: BytesIO) -> str:
        """Convert a document to HTML format.

        Args:
            name: The document filename.
            stream: The document bytes.

        Returns:
            The document content as HTML.
        """
        result = self.converter.convert(self._create_stream(name, stream))
        return result.document.export_to_html()

    def convert_to_text(self, name: str, stream: BytesIO) -> str:
        """Convert a document to plain text.

        Args:
            name: The document filename.
            stream: The document bytes.

        Returns:
            The document content as plain text.
        """
        result = self.converter.convert(self._create_stream(name, stream))
        return result.document.export_to_text()

    def convert_to_doctags(self, name: str, stream: BytesIO) -> str:
        """Convert a document to Doctags format (tagged format for downstream ML tasks).

        Args:
            name: The document filename.
            stream: The document bytes.

        Returns:
            The document content as doctags.
        """
        result = self.converter.convert(self._create_stream(name, stream))
        return result.document.export_to_doctags()