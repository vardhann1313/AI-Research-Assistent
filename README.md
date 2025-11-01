# AI Document Summarizer

An intelligent document summarization API built with FastAPI and CrewAI that leverages AI agents to analyze and summarize documents efficiently.

## Description

AI Document Summarizer is a FastAPI-based web service designed to provide automated document summarization capabilities. The project utilizes CrewAI for orchestrating AI agents and LangChain for natural language processing tasks, enabling intelligent extraction and condensation of key information from various document formats.

## Dependencies

This project uses the following key dependencies:

### Web Framework
- **FastAPI** (>=0.120.2) - Modern, fast web framework for building APIs
- **Uvicorn** (>=0.38.0) - ASGI server for running the FastAPI application
- **Python-multipart** (>=0.0.20) - Support for multipart/form-data file uploads

### Database
- **Motor** (>=3.7.1) - Asynchronous MongoDB driver

### Authentication & Security
- **Python-JOSE** (>=3.3.0) - JWT implementation for Python
- **Passlib** (>=1.7.4) - Password hashing library with Argon2 support
- **HTTPX** (>=0.27.0) - Async HTTP client for OAuth and API requests
- **Authlib** (>=1.6.5) - Authentication library for OAuth and OpenID
- **itsdangerous** (>=2.2.0) - Security-related functionality

### AI/ML
- **CrewAI** (>=1.2.1) - Framework for orchestrating AI agents
- **LangChain** (>=0.1.0) - Framework for developing applications powered by language models

### Document Processing
- **PyPDF** (>=3.17.0) - PDF processing library
- **Python-docx** (>=1.1.0) - Library for working with Word documents

### Utilities
- **Pydantic** (>=2.11.9) - Data validation and settings management
- **Python-dotenv** (>=1.2.1) - Environment variable management from .env files

## Requirements

- Python 3.11 or higher
- uv (recommended) or pip for package management

## Project Setup

### Step 1: Clone the Repository

Clone this repository to your local machine.

### Step 2: Create a Virtual Environment

Create and activate a Python virtual environment to isolate project dependencies.

### Step 3: Install Dependencies

#### Using uv

Install all project dependencies using uv package manager:

```
uv sync
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory and add any required API keys or configuration variables (e.g., OpenAI API keys, model configurations).

### Step 5: Run the Application

Start the FastAPI development server:

```
uv run main.py
```

The server will start on `http://127.0.0.1:8000` with hot-reload enabled for development.

### Step 6: Access the API

- **API Root**: `http://127.0.0.1:8000/`
- **Interactive API Documentation**: `http://127.0.0.1:8000/docs`
- **Alternative API Documentation**: `http://127.0.0.1:8000/redoc`

## Development

The application runs in development mode with auto-reload enabled, allowing you to make changes and see them reflected immediately without restarting the server.

## Project Structure

- `main.py` - Main application entry point and FastAPI server configuration
- `pyproject.toml` - Project metadata and dependency specifications
- `.env` - Environment variables (create this file locally)
- `.venv/` - Virtual environment directory

## License

This project is open source and available for use and modification.
