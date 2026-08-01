# AI Engineer Interview Preparation Plan

This repository contains a 4-week study and practice plan designed to prepare for AI engineering interviews in one month.

## Goal

Build a strong practical foundation in Python, APIs, MCP, and agent frameworks while developing small projects and real tools each week.

## Week 1 - Python Refresher + AI Prerequisites

Objective: Refresh core Python skills and modern tooling to prepare for AI project development.

Focus areas:
- Python comprehensions, slicing, unpacking, f-strings
- Functions with defaults, `*args`, `**kwargs`
- Error handling, custom exceptions, file I/O, JSON read/write
- OOP, `dataclass`, abstract base classes
- `uv` project scaffolding, Pydantic v2 models and validation
- `asyncio`, `httpx`, concurrent HTTP calls, retry/backoff

Weekend project:
- Async multi-source data aggregator
- Separate Pydantic models for each API response
- Store results in a data class
- Handle partial failures gracefully
- Package as a `uv` project with environment support and README

Tech stack: `uv`, `httpx`, `pydantic`, `python-dotenv`, `rich`

## Week 2 - APIs & LLM Integration

Objective: Build a secure REST microservice that integrates LLMs and supports tool calling.

Focus areas:
- FastAPI `POST` endpoint with request/response models
- Uvicorn live reload and Swagger docs
- Dependency injection and API-key auth
- Background tasks and HTTP exception handling
- Anthropic / Claude SDK structured outputs
- OpenAI chat completions with JSON-mode responses
- Native tool calling loop and tool execution

Weekend project:
- AI-powered REST microservice with `/ask`
- API-key protection and error handling
- Tool-use loop with at least two tools
- Structured output validation with Pydantic
- Health endpoint and `curl` examples

Tech stack: `fastapi`, `uvicorn[standard]`, `anthropic`, `openai`, `pydantic`

## Week 3 - Model Context Protocol (MCP)

Objective: Learn MCP architecture and ship a custom MCP server that works with Claude Desktop.

Focus areas:
- MCP host/client architecture and transport modes
- Build a FastMCP server with tool definitions
- Add resources and prompt templates
- Run over stdio and streamable HTTP
- Connect the server to Claude Desktop and verify tool calls
- Call the server from Python using an MCP client

Weekend project:
- Custom MCP assistant theme
- At least three real tools, one resource, one prompt
- Support stdio and HTTP transport
- Verify with MCP Inspector and Claude Desktop
- Document tools, resources, and prompts in README

Tech stack: `fastmcp`, MCP Inspector, Claude Desktop

## Week 4 - RAG Infrastructure & Agent Frameworks

Objective: Add grounding, observability, and agent orchestration to a production-style system.

Focus areas:
- Vector database basics and similarity search
- RAG pipeline with text chunking, embedding, and retrieval
- Observability with Langfuse traces
- Guardrails for input/output and safety checks
- Stateful agent graphs with LangGraph
- Agent orchestration using PydanticAI and MCP integration
- Optional exploration of CrewAI for multi-agent workflows

Weekend capstone:
- Full-stack agent with RAG grounding and tool access
- Tools sourced from the MCP server
- End-to-end tracing and at least one guardrail
- Served through FastAPI endpoint `/agent/ask`
- Architecture documentation with a simple diagram

Tech stack: `chromadb`, `langfuse`, `langgraph`, `pydantic-ai`, optional `crewai`, optional `qdrant-client`

## After Week 4

Recommended next steps:
- Deepen work in one Week 4 framework
- Add OAuth or remote deployment to MCP server
- Build an evaluation suite for guardrails
- Track monthly changelogs for fast-moving tooling

## Installation

1. Install Python 3.11 or newer.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies for the projects you want to build. Example:
   ```bash
   pip install uv httpx pydantic python-dotenv rich fastapi uvicorn[standard] anthropic openai chromadb langfuse langgraph pydantic-ai
   ```
4. If you use `uv`, initialize a new Python project in the target folder:
   ```bash
   uv project init
   ```
5. Create a `.env` file for API keys and runtime settings.
6. Run project code from the activated environment.

## Notes

This plan is intended as a focused one-month pathway into AI engineering interviews, with practical projects and real tooling exposure.
