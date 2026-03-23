
from io import BytesIO
from unittest.mock import MagicMock

import pytest
from agno.media import File

from app.agents.tools.documents import DocumentsTool


@pytest.fixture
def mock_service():
    return MagicMock()


@pytest.fixture
def tool(mock_service):
    return DocumentsTool(service=mock_service)


@pytest.fixture
def file_with_content():
    return File(content=b"pdf-bytes", filename="report.pdf")


def test_init(tool):
    registered = set(tool.functions.keys())
    assert registered == {
        "convert_to_md",
        "convert_to_json",
        "convert_to_html",
        "convert_to_text",
        "convert_to_doctags",
    }
    assert tool.name == "documents"

def test_init_uses_provided_service(mock_service):
    t = DocumentsTool(service=mock_service)
    assert t.service is mock_service


def test_to_stream_returns_name_and_bytesio(tool):
    file = File(content=b"hello", filename="test.pdf")
    name, stream = tool._to_stream(file)
    assert name == "test.pdf"
    assert isinstance(stream, BytesIO)
    assert stream.read() == b"hello"


def test_to_stream_falls_back_to_name_field(tool):
    file = File(content=b"hello", name="fallback.pdf")
    name, _ = tool._to_stream(file)
    assert name == "fallback.pdf"


def test_to_stream_falls_back_to_document_when_no_names(tool):
    file = File(content=b"hello")
    name, _ = tool._to_stream(file)
    assert name == "document"


def test_to_stream_prefers_filename_over_name(tool):
    file = File(content=b"hello", filename="first.pdf", name="second.pdf")
    name, _ = tool._to_stream(file)
    assert name == "first.pdf"


def test_to_stream_raises_when_no_content(tool):
    file = MagicMock()
    file.get_content_bytes.return_value = None
    with pytest.raises(ValueError, match="File has no readable content"):
        tool._to_stream(file)


def test_convert_to_md(tool, mock_service, file_with_content):
    mock_service.convert_to_md.return_value = "# Heading"
    result = tool.convert_to_md(file_with_content)
    assert result == "# Heading"
    args = mock_service.convert_to_md.call_args[0]
    assert args[0] == "report.pdf"
    assert isinstance(args[1], BytesIO)
    assert args[1].read() == b"pdf-bytes"


def test_convert_to_json(tool, mock_service, file_with_content):
    mock_service.convert_to_json.return_value = '{"key": "val"}'
    result = tool.convert_to_json(file_with_content)
    assert result == '{"key": "val"}'
    args = mock_service.convert_to_json.call_args[0]
    assert args[0] == "report.pdf"
    assert isinstance(args[1], BytesIO)


def test_convert_to_html(tool, mock_service, file_with_content):
    mock_service.convert_to_html.return_value = "<p>hi</p>"
    result = tool.convert_to_html(file_with_content)
    assert result == "<p>hi</p>"
    args = mock_service.convert_to_html.call_args[0]
    assert args[0] == "report.pdf"
    assert isinstance(args[1], BytesIO)


def test_convert_to_text(tool, mock_service, file_with_content):
    mock_service.convert_to_text.return_value = "plain text"
    result = tool.convert_to_text(file_with_content)
    assert result == "plain text"
    args = mock_service.convert_to_text.call_args[0]
    assert args[0] == "report.pdf"
    assert isinstance(args[1], BytesIO)


def test_convert_to_doctags(tool, mock_service, file_with_content):
    mock_service.convert_to_doctags.return_value = "<doctag>stuff</doctag>"
    result = tool.convert_to_doctags(file_with_content)
    assert result == "<doctag>stuff</doctag>"
    args = mock_service.convert_to_doctags.call_args[0]
    assert args[0] == "report.pdf"
    assert isinstance(args[1], BytesIO)