# LangGraph Cloud Example

![](static/agent_ui.png)

This is an example agent to deploy with LangGraph Cloud.

> [!TIP]
> If you would rather use `pyproject.toml` for managing dependencies in your LangGraph Cloud project, please check out [this repository](https://github.com/langchain-ai/langgraph-example-pyproject).

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications with LLMs. The main use cases for LangGraph are conversational agents, and long-running, multi-step LLM applications or any LLM application that would benefit from built-in support for persistent checkpoints, cycles and human-in-the-loop interactions (ie. LLM and human collaboration).

LangGraph shortens the time-to-market for developers using LangGraph, with a one-liner command to start a production-ready HTTP microservice for your LangGraph applications, with built-in persistence. This lets you focus on the logic of your LangGraph graph, and leave the scaling and API design to us. The API is inspired by the OpenAI assistants API, and is designed to fit in alongside your existing services.

## Local Development

### Setup with pip and virtual environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd langgraph-example
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r my_agent/requirements.txt
   ```

4. Create a `.env` file with your API keys:
   ```bash
   cp .env.example .env
   ```
   Then add your API keys for Anthropic, Tavily, and OpenAI.

### Running the agent

You can run the agent using the LangGraph CLI:

```bash
langgraph dev  # Runs the agent defined in langgraph.json
```

Or serve it as an API:

```bash
langgraph serve
```

## Deployment

In order to deploy this agent to LangGraph Cloud you will want to first fork this repo. After that, you can follow the instructions [here](https://langchain-ai.github.io/langgraph/cloud/) to deploy to LangGraph Cloud.
