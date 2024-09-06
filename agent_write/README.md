# AgentWrite LangGraph

AgentWrite LangGraph is a rewrite and extension of AgentWrite using LangGraph, designed to create an advanced writing assistant powered by language models and graph-based workflows.

## Description

This project leverages LangGraph to orchestrate a series of language model interactions, creating a powerful tool for automated content generation. It breaks down complex writing tasks into manageable steps, including planning, writing, and refining content.

## Features

- Automated content planning
- Paragraph-by-paragraph content generation
- Integration with multiple language models (OpenAI, GROQ, OLLaMA)
- Flexible workflow management using LangGraph
- Markdown output for generated content

## Installation

1. Ensure you have Python 3.11 or later installed.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/AgentWrite-LangGraph.git
   cd AgentWrite-LangGraph
   ```
3. Install Poetry if you haven't already:
   ```
   pip install poetry
   ```
4. Install project dependencies:
   ```
   poetry install
   ```

## Usage

1. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

2. Run the main script:
   ```
   poetry run python -m agentwrite
   ```

## Configuration

You can configure the project by modifying the `config.py` file. This includes settings for:

- Test instructions
- Language model selection
- Output file paths

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LangChain and LangGraph for providing the foundational tools
- OpenAI, GROQ, and OLLaMA for their language models

