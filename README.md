# Azure OpenAI Python CLI

Small example CLI to call an Azure OpenAI deployment using the REST API.

Prereqs
- Python 3.8+
- An Azure OpenAI resource with a deployed model (you have a `deployment id`).

Setup
1. Copy `.env.example` to `.env` and fill `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT`, or set these in your shell:

```bash
export AZURE_OPENAI_KEY="<your-key>"
export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
```

2. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Quick examples

- List deployments:

```bash
python app.py list
```

- Chat (single-turn):

```bash
python app.py chat -d <deployment-name> -m "Hello from my CLI"
```

- Text completion (non-chat):

```bash
python app.py completion -d <deployment-name> -p "Write a haiku about autumn"
```

Notes
- This script calls the Azure OpenAI REST endpoints directly using `requests` and reads the API key from `api-key` header.
- If you prefer the official SDK, replace the REST calls with `azure-ai-openai` usage.
