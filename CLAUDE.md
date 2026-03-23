# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Document conversion tool built on [Docling](https://github.com/DS4SD/docling) with an agent-based architecture using [Agno](https://github.com/agno-agi/agno). Converts documents (PDFs, etc.) to various formats: Markdown, JSON (DoclingDocument schema), HTML, plain text, and Doctags.

## Development Setup

- **Python 3.13** (see `.python-version`)
- **uv** for dependency management
- Install dependencies: `uv sync`
- Run scripts: `uv run python <script>`

## Architecture

- `app/agents/tools/` — Agno `Toolkit` subclasses that wrap Docling functionality (e.g., `DocumentsTool`)
- `app/core/` — Configuration (Pydantic settings, API keys)
- `data/pdfs/` — Sample documents for testing

## Instructions

Never read or output contents of .env files or any file containing API keys. 