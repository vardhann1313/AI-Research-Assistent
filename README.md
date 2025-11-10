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

### Authentication (`/api/v1/auth`)
- `GET /check` - Router health check
- `POST /signup` - Create a new user
- `POST /login` - Login and receive a JWT
- `GET /google` - Initiate Google OAuth
- `GET /google/callback` - Google OAuth callback

### Chat & Documents (`/api/v1/chat`)
- `POST /new_chat` - Start a new chat session by uploading a document
  - Auth: Bearer token required (Authorization: Bearer <token>)
  - Body: multipart/form-data with `file` (.pdf, .txt, .docx)
  - Response: chat_id and a welcome message
- `GET /ask/{chat_id}` - Ask a question about the uploaded document
  - Auth: Bearer token required
  - Query: `question` (string)

### Agent Management (`/api/v1/agent`)
- `GET /health_check` - Current and max agent pool info

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
   MONGO_URL=mongodb://localhost:27017

   # FastAPI sessions
   SESSION_SECRET_KEY=replace-with-a-random-secret

   # JWT
   JWT_SECRET_KEY=replace-with-a-random-secret
   JWT_ALGORITHM=HS256

   # LLM (Gemini via CrewAI)
   GEMINI_API_KEY=your-gemini-api-key

   # Google OAuth (optional)
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
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
AI-Research Assistant/
├── app/
│   ├── Agents/
│   │   ├── agent.py
│   │   ├── agentManager.py
│   │   ├── agentTools.py
│   │   ├── agent_utils.py
│   │   ├── ragChain.py
│   │   └── utilityFunctions.py
│   ├── Config/
│   │   └── directoryConfig.py
│   ├── Models/
│   │   ├── DTO.py
│   │   ├── chatModel.py
│   │   └── userModel.py
│   ├── Router/
│   │   ├── agentRouter.py
│   │   ├── authRouter.py
│   │   └── chatRouter.py
│   ├── Service/
│   │   ├── authService.py
│   │   └── chatService.py
│   └── Utils/
│       ├── dbUtlis.py
│       ├── fileUtils.py
│       ├── jwtUtils.py
│       ├── passwordUtils.py
│       └── textUtils.py
├── main.py
└── pyproject.toml
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

