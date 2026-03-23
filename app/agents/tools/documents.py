from io import BytesIO

from agno.media import File
from agno.tools import Toolkit

from app.service.documents import DocumentService


class DocumentsTool(Toolkit):
    def __init__(self, service: DocumentService | None = None):
        self.service = service or DocumentService()

        tools = [
            self.convert_to_md,
            self.convert_to_json,
            self.convert_to_html,
            self.convert_to_text,
            self.convert_to_doctags,
        ]
        super().__init__(name="documents", tools=tools)

    def _to_stream(self, file: File) -> tuple[str, BytesIO]:
        content = file.get_content_bytes()
        if content is None:
            raise ValueError("File has no readable content (provide content, filepath, or url)")
        name = file.filename or file.name or "document"
        return name, BytesIO(content)

    def convert_to_md(self, file: File) -> str:
        """Convert a document to markdown format.

        Args:
            file: An Agno File containing the document.

        Returns:
            The document content as markdown.
        """
        name, stream = self._to_stream(file)
        return self.service.convert_to_md(name, stream)

    def convert_to_json(self, file: File) -> str:
        """Convert a document to Docling's DoclingDocument JSON schema.

        Args:
            file: An Agno File containing the document.

        Returns:
            The document content as JSON.
        """
        name, stream = self._to_stream(file)
        return self.service.convert_to_json(name, stream)

    def convert_to_html(self, file: File) -> str:
        """Convert a document to HTML format.

        Args:
            file: An Agno File containing the document.

        Returns:
            The document content as HTML.
        """
        name, stream = self._to_stream(file)
        return self.service.convert_to_html(name, stream)

    def convert_to_text(self, file: File) -> str:
        """Convert a document to plain text.

        Args:
            file: An Agno File containing the document.

        Returns:
            The document content as plain text.
        """
        name, stream = self._to_stream(file)
        return self.service.convert_to_text(name, stream)

    def convert_to_doctags(self, file: File) -> str:
        """Convert a document to Doctags format (tagged format for downstream ML tasks).

        Args:
            file: An Agno File containing the document.

        Returns:
            The document content as doctags.
        """
        name, stream = self._to_stream(file)
        return self.service.convert_to_doctags(name, stream)