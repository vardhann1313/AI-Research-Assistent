# AI Research Assistant

An intelligent AI-powered research assistant built with FastAPI and CrewAI that enables natural language interaction with research documents through a sophisticated agent-based architecture.

## Description

AI Research Assistant is a high-performance web service that allows users to upload research documents and engage in meaningful conversations about their content. The system features:

- **Agent Management System**: Implements a singleton pattern for efficient agent lifecycle management
- **Document Processing**: Supports multiple document formats with intelligent chunking and embedding
- **Conversational Memory**: Maintains context-aware conversations using RAG (Retrieval-Augmented Generation)
- **Modular Architecture**: Clean separation of concerns with dedicated modules for agents, tools, and services
- **Asynchronous Processing**: Built with async/await for optimal performance

## Key Features

- **Intelligent Agent System**: Manages multiple AI agents with configurable tools and memory
- **Document Processing**: Handles PDF and Word documents with smart chunking
- **Conversational Interface**: Natural language interaction with document content
- **Context-Aware Responses**: Uses RAG to provide relevant answers based on document content
- **Session Management**: Maintains separate chat sessions with independent contexts
- **Tool Integration**: Equipped with specialized tools for document retrieval and chat history
- **Performance Optimized**: Implements connection pooling and async operations

## Dependencies

### Core Dependencies
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running the FastAPI application
- **Python-multipart** - Support for file uploads
- **Pydantic** - Data validation and settings management
- **Python-dotenv** - Environment variable management

### Database
- **Motor** - Async MongoDB driver

### AI/ML & Processing
- **CrewAI** - Framework for orchestrating AI agents
- **LangChain-Google-GenAI** - Google's Gemini integration
- **PyPDF** - PDF text extraction
- **Python-docx** - Word document processing
- **SentenceTransformers** - Embedding generation
- **Langchain-Chroma** - Vector similarity search
- **Langchain-Huggingface** - For embedding model
- **Langchain-Text-Splitters** - For chunking of docs

### Authentication & Security
- **Python-JOSE** - JWT implementation
- **Passlib** - Password hashing with Argon2
- **HTTPX** - Async HTTP client
- **itsdangerous** - Security utilities

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

### Agent Management
- `GET /api/v1/agent/health_check` - Check agent health and stats

## Project Setup

### Prerequisites
- Python 3.11 or higher
- MongoDB database
- GEMINI API key (or other LLM provider)
- uv package manager (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Research-Assistant.git
   cd AI-Research-Assistant
   ```

2. **Install uv package manager** (recommended)
   ```bash
   pip install uv
   ```

3. **Install dependencies using uv**
   ```bash
   uv sync .
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root with the following variables:
   ```env
   # Database
   MONGODB_URI=mongodb://localhost:27017/ai_research
   
   # JWT Authentication
   JWT_SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_DAYS=7
   
   # AI/ML Services
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Run the application**
   ```bash
   uv run main.py
   ```

6. **Access the API**
   - API Documentation: `http://localhost:8000/docs`
   - Interactive Docs: `http://localhost:8000/redoc`

## Project Structure

```
AI-Research-Assistant/
├── app/
│   ├── Agents/           # AI agent implementations
│   │   ├── agent.py            # Main agent interface
│   │   ├── agent_utils.py      # Agent creation utilities
│   │   ├── agentManager.py     # Agent lifecycle management
│   │   ├── agentTools.py       # Custom tools for agents
│   │   ├── ragChain.py         # RAG implementation
│   │   └── utilityFunctions.py # Helper functions
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
   - Use type hints consistently
   - Keep functions focused and modular

2. **Documentation**
   - Update API documentation when adding new endpoints
   - Add comprehensive docstrings to all public methods

3. **Best Practices**
   - Use async/await for I/O operations
   - Implement proper error handling
   - Follow the single responsibility principle

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

