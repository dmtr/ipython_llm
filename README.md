# ipython_llm

The ipython_llm is a library built to integrate the services of OpenAI's Large Language Model (LLM) within the IPython environment. It allows the user to directly i
niti
ate and maintain a conversation with the model from an IPython interface.

## Installation

To install the library, run:

```bash
pip install ipython_llm
```

## Setup

To setup:

1. Install the library.
2. Get your OpenAI API key and set it as an environment variable.
   
```bash
export OPENAI_API_KEY=your_api_key_goes_here
```

## Usage

After setting up, load the extension in IPython:

```python
%load_ext ipython_llm
```

Once the extension has been loaded, a couple of magics are offered:

### Line magic: %llm_prompt

This magic sends a prompt to the LLM in a single IPython line.

To use the line magic, format :

```python
%llm_prompt [optional parameters] your_prompt_here
```

The optional parameters include:

- `-t`, or `--temperature`, adjusts the output's randomness. The values range between 0 (fully deterministic) and 1 (maximum randomness).
- `-c`, or `--clear`, resets the conversation status with the model.
- `-m`, or `--model`, specifies another model alias to use.

Example:

```python
%llm_prompt -t 0.5 -c Code to convert list to string in Python
```

### Cell magic: %%llm_prompt_cell - to be implemented

The cell magic allows extended inputs spanning multiple lines.

To use the cell magic, write your prompt across several lines:

```python
%%llm_prompt_cell
Your prompt here.
It can span multiple lines.
```

You can also include the optional parameters in the first line:

```python
%%llm_prompt_cell -t 0.5 -c
Your prompt goes here.
It can span multiple lines.
```

In both the line and cell magic, if the LLM's response contains code (formatted with ```python```), it is returned in a new IPython cell, ready to be executed. If there's no code, the model's plain text response is printed.

## Version

Current version is 0.0.1
