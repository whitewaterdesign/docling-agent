from io import BytesIO
from unittest.mock import MagicMock

import pytest
from docling.document_converter import DocumentConverter

from app.service.documents import DocumentService

@pytest.fixture
def get_document_service():
    document_converter = MagicMock(spec=DocumentConverter)
    document_service = DocumentService(document_converter)

    return document_service, document_converter

def test_document_service(get_document_service):
    document_service, _ = get_document_service
    stream = BytesIO(b"hello world")
    result = document_service._create_stream("test.txt", stream)

    assert isinstance(document_service.converter, DocumentConverter)
    assert result.name == "test.txt"
    assert result.stream == stream

def test_document_service_convert_to_md(get_document_service):
    document_service, document_converter = get_document_service
    result = document_service.convert_to_md("test.txt", BytesIO(b"hello world"))
    called_arg = document_converter.convert.call_args.args[0]

    assert called_arg.name == "test.txt"
    assert called_arg.stream.getvalue() == b"hello world"

    markdown = document_converter.convert.return_value.document.export_to_markdown()
    assert result.name == markdown.name
    assert result.stream == markdown.stream

def test_document_service_convert_to_json(get_document_service):
    document_service, document_converter = get_document_service
    document_converter.convert.return_value.document.export_to_dict.return_value = {
        "name": "test.txt",
        "content": "hello world",
    }

    result = document_service.convert_to_json("test.txt", BytesIO(b"hello world"))
    called_arg = document_converter.convert.call_args.args[0]

    assert called_arg.name == "test.txt"
    assert called_arg.stream.getvalue() == b"hello world"

    expected_json = document_converter.convert.return_value.document.export_to_dict.return_value
    assert result == expected_json


def test_document_service_convert_to_html(get_document_service):
    document_service, document_converter = get_document_service
    document_converter.convert.return_value.document.export_to_html.return_value = "<p>hello world</p>"

    result = document_service.convert_to_html("test.txt", BytesIO(b"hello world"))
    called_arg = document_converter.convert.call_args.args[0]

    assert called_arg.name == "test.txt"
    assert called_arg.stream.getvalue() == b"hello world"

    expected_html = document_converter.convert.return_value.document.export_to_html.return_value
    assert result == expected_html

def test_document_service_convert_to_text(get_document_service):
    document_service, document_converter = get_document_service
    document_converter.convert.return_value.document.export_to_text.return_value = "hello world"

    result = document_service.convert_to_text("test.txt", BytesIO(b"hello world"))
    called_arg = document_converter.convert.call_args.args[0]

    assert called_arg.name == "test.txt"
    assert called_arg.stream.getvalue() == b"hello world"

    expected_text = document_converter.convert.return_value.document.export_to_text.return_value
    assert result == expected_text


def test_document_service_convert_to_doctags(get_document_service):
    document_service, document_converter = get_document_service
    document_converter.convert.return_value.document.export_to_doctags.return_value = "<doctags>hello world</doctags>"

    result = document_service.convert_to_doctags("test.txt", BytesIO(b"hello world"))
    called_arg = document_converter.convert.call_args.args[0]

    assert called_arg.name == "test.txt"
    assert called_arg.stream.getvalue() == b"hello world"

    expected_doctags = document_converter.convert.return_value.document.export_to_doctags.return_value
    assert result == expected_doctags