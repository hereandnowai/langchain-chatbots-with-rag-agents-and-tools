<p align="center">
  <a href="https://hereandnowai.com" target="_blank">
    <img src="https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/HNAI%20Title%20-Teal%20%26%20Golden%20Logo%20-%20DESIGN%203%20-%20Raj-07.png" alt="HERE AND NOW AI Logo" width="400"/>
  </a>
</p>

<h1 align="center">LangChain: Chatbots with RAG, Agents, and Tools</h1>

<p align="center">
  <em>A project-based tutorial by <a href="https://hereandnowai.com" target="_blank">HERE AND NOW AI</a>, designed with a passion for innovation.</em>
</p>

---

This repository contains a comprehensive, project-based tutorial that guides you through building sophisticated chatbots and AI applications using LangChain. You will learn everything from the fundamentals of chat models to advanced concepts like Retrieval-Augmented Generation (RAG), agents, and custom tools.

## 🚀 What You'll Learn

This course is structured into five key areas, each building upon the last:

1.  **Chat Models:** Understand the core components of LangChain and how to interact with different Large Language Models (LLMs) like OpenAI, Anthropic, and Google Gemini.
2.  **Prompt Templates:** Master the art of prompt engineering by creating dynamic, reusable prompt templates to guide LLM responses effectively.
3.  **Chains (using LangChain Expression Language - LCEL):** Learn to chain components together to create complex and powerful logic flows. Explore sequential, parallel, and branching chains to build sophisticated applications.
4.  **Retrieval-Augmented Generation (RAG):** Dive deep into the RAG architecture. You'll learn how to connect your LLM to external data sources, including:
    *   Loading and splitting documents (text files, web pages).
    *   Creating and storing vector embeddings using models like ChromaDB.
    *   Building retrievers to fetch relevant information for your chatbot.
    *   Implementing conversational RAG systems that can remember past interactions.
5.  **Agents and Tools:** Go beyond simple chains by building intelligent agents that can use tools to interact with the outside world. Learn how to create custom tools and leverage pre-built ones (like Wikipedia or Tavily Search) to give your agents powerful new capabilities.

## 🛠️ Getting Started

This project is configured to use `uv`, a fast and modern Python package manager.

### Prerequisites

- Python 3.10+
- `uv` installed on your system. You can find installation instructions [here](https://github.com/astral-sh/uv).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hereandnowai/langchain-chatbots-with-rag-agents-and-tools.git
    cd langchain-chatbots-with-rag-agents-and-tools
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    `uv` will install all required packages from the `pyproject.toml` file.
    ```bash
    uv pip install -e .
    ```

5.  **Set up your API keys:**
    Create a `.env` file by copying the example file:
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and add your API keys for services like OpenAI, Google, Firecrawl, etc.

## 📂 Project Structure

The tutorial code is organized into numbered directories, each focusing on a specific concept:

```
.
├── 1_chat_models/         # Basics of interacting with LLMs
├── 2_prompt_templates/    # Crafting effective prompts
├── 3_chains/              # Building application logic with LCEL
├── 4_rag/                 # All about Retrieval-Augmented Generation
│   ├── books/             # Sample text files for RAG
│   └── utils/             # Utility scripts
└── 5_agents_and_tools/    # Creating intelligent agents and tools
```

Each file is a self-contained script that you can run and experiment with.

---

## About HERE AND NOW AI

**HERE AND NOW AI** is an Artificial Intelligence Research Institute dedicated to pushing the boundaries of AI through cutting-edge research and practical application.

*   **Website:** [hereandnowai.com](https://hereandnowai.com)
*   **Email:** [info@hereandnowai.com](mailto:info@hereandnowai.com)
*   **Slogan:** *designed with passion for innovation*

### Connect with Us

Stay up-to-date with our latest research, projects, and tutorials:

*   [**GitHub**](https://github.com/hereandnowai)
*   [**LinkedIn**](https://www.linkedin.com/company/hereandnowai/)
*   [**X (formerly Twitter)**](https://x.com/hereandnow_ai)
*   [**Instagram**](https://instagram.com/hereandnow_ai)
*   [**YouTube**](https://youtube.com/@hereandnow_ai)
*   [**Blog**](https://hereandnowai.com/blog)