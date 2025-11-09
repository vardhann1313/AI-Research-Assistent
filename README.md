# AI Research Assistant

An intelligent AI-powered research assistant built with FastAPI and CrewAI that helps users analyze and interact with research documents through natural language conversations.

## Description

AI Research Assistant is a FastAPI-based web service that enables users to upload research documents and interact with them through a conversational interface. The system leverages CrewAI for orchestrating AI agents and LangChain for document processing, enabling intelligent question-answering and information extraction from various document formats.

## Key Features

- **Document Processing**: Upload and process various document formats including PDF and Word documents
- **Conversational Interface**: Interact with your documents through natural language queries
- **Multi-document Support**: Create separate chat sessions for different research documents
- **Secure Authentication**: JWT-based authentication system for secure access
- **RESTful API**: Well-documented endpoints for easy integration with frontend applications

## Dependencies

### Core Dependencies
- **FastAPI** (>=0.120.2) - Modern, fast web framework for building APIs
- **Uvicorn** (>=0.38.0) - ASGI server for running the FastAPI application
- **Python-multipart** (>=0.0.20) - Support for multipart/form-data file uploads

### Database
- **Motor** (>=3.7.1) - Asynchronous MongoDB driver

### Authentication & Security
- **Python-JOSE** (>=3.3.0) - JWT implementation for Python
- **Passlib** (>=1.7.4) - Password hashing with Argon2 support
- **HTTPX** (>=0.27.0) - Async HTTP client
- **Authlib** (>=1.6.5) - Authentication library
- **itsdangerous** (>=2.2.0) - Security utilities

### AI/ML & Document Processing
- **CrewAI** (>=1.2.1) - Framework for orchestrating AI agents
- **LangChain** (>=0.1.0) - Framework for LLM applications
- **PyPDF** (>=3.17.0) - PDF processing
- **Python-docx** (>=1.1.0) - Word document processing

### Utilities
- **Pydantic** (>=2.11.9) - Data validation
- **Python-dotenv** (>=1.2.1) - Environment management

## Requirements

- Python 3.11 or higher
- uv (recommended) or pip for package management

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - User logout

### Chat & Documents
- `POST /api/v1/chat/new_chat` - Start a new chat session with a document
- `GET /api/v1/chat/ask/{chat_id}` - Ask a question about the document

## Project Setup

### Prerequisites
- Python 3.11 or higher
- MongoDB database
- OpenAI API key (or other LLM provider)
- uv package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Research-Assistant.git
   cd AI-Research-Assistant
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```
   or with pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root with the following variables:
   ```
   MONGODB_URI=mongodb://localhost:27017/ai_research
   JWT_SECRET_KEY=your-secret-key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_DAYS=7
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - API Documentation: `http://localhost:8000/docs`
   - Interactive Docs: `http://localhost:8000/redoc`

## Project Structure

```
AI-Research-Assistant/
├── app/
│   ├── Agents/           # AI agent implementations
│   ├── Config/           # Configuration files
│   ├── Models/           # Database models and DTOs
│   ├── Router/           # API route definitions
│   ├── Service/          # Business logic
│   └── Utils/            # Utility functions
├── tests/                # Test files
├── .env                  # Environment variables
├── main.py               # Application entry point
└── pyproject.toml        # Project metadata and dependencies
```

## Development

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints for better code clarity

2. **Testing**
   - Write unit tests for new features
   - Run tests with `pytest`

3. **Documentation**
   - Keep API documentation updated
   - Add docstrings to new functions and classes

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
