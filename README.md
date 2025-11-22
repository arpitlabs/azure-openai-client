(This repository contains a small example CLI to call Azure OpenAI deployments.)

## 1) Create an Azure OpenAI resource and deploy `gpt-4.1-mini` (Azure Portal)

Follow these step-by-step instructions in the Azure Portal to create a new Azure OpenAI resource and add a model deployment named `gpt-4.1-mini`.

1. Sign in to the Azure Portal: https://portal.azure.com
2. Create the resource:
	- Click **Create a resource** in the left-hand menu.
	- Search for **Azure OpenAI** and select the **Azure OpenAI** offering, then click **Create**.
	- Fill the basics:
	  - **Subscription**: choose your subscription.
	  - **Resource group**: select an existing group or create a new one.
	  - **Region**: choose a region (pick one where Azure OpenAI is available).
	  - **Name**: enter a unique name for the resource (this appears in the endpoint URL).
	- Click **Review + create**, then **Create**. Wait for deployment to finish.
3. Open the created Azure OpenAI resource from the portal (click **Go to resource** after creation or find it in **Resources**).
	- From the resource overview, click the **Go to Foundry Portal** link. This opens the resource in the Microsoft Foundry portal where model deployments are managed.
4. In the Foundry Portal create a model deployment for `gpt-4.1-mini`:
	- In the Foundry left menu click **Deployments**.
	- Click **Create** (or **Deploy model** → **Deploy base model** depending on the UI flow).
	- Select **gpt-4.1-mini** as the base model.
	- Pick a short **Deployment name** (for example: `gpt-4-1-mini-deploy`) — this name is the `deployment id` you'll pass to the CLI.
	- Configure instance/scale settings if required, then click **Create** (or **Deploy**). Wait for provisioning to complete (this can take several minutes).
5. Generate/copy credentials and endpoint (if not already copied):
	- Back in the Azure Portal (resource page) open **Keys and Endpoint** in the left menu.
	- Copy one of the **Keys** (you'll use this as the API key).
	- Copy the **Endpoint** URL (it looks like `https://<your-resource>.openai.azure.com/`).

Notes:
- If `gpt-4.1-mini` is not visible, your subscription may not have quota for that model or it may not be available in the selected region — choose a supported model or request access.
- Keep your key secret. Don't commit it to source control.

## 2) How to set up and run this app (local)

These steps assume you're in the repository root.

1. Copy `_.env.example` to `.env` and fill values with the key and endpoint you obtained in the portal, or set environment variables directly.

	Example `.env` (create or edit the file):

	```text
	AZURE_OPENAI_API_KEY=your_api_key_here
	AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
	AZURE_OPENAI_API_VERSION=2023-10-01-preview
	````

	Important: the repo's code accepts either `AZURE_OPENAI_API_KEY` or `AZURE_OPENAI_KEY`. Ensure the endpoint value starts with `https://` and contains no leading characters (remove stray symbols like `√`).

2. Create & activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Verify the environment variables are visible to Python (quick check):

```bash
.venv/bin/python - <<'PY'
from dotenv import load_dotenv
import os
load_dotenv()
print('API_KEY=', os.getenv('AZURE_OPENAI_API_KEY') or os.getenv('AZURE_OPENAI_KEY'))
print('ENDPOINT=', os.getenv('AZURE_OPENAI_ENDPOINT'))
PY
```

4. Run the app example or CLI. The repository contains `app.py` which either runs a short example or exposes simple CLI commands depending on its contents. Example run (the file as shipped contains a sample chat call):

```bash
.venv/bin/python app.py
```

If you have the minimal CLI version of `app.py` (chat/completion subcommands), use:

```bash
.venv/bin/python app.py chat -d <deployment-name> -m "Hello from CLI"
.venv/bin/python app.py completion -d <deployment-name> -p "Write a haiku about autumn"
```

## Troubleshooting
- `Missing credentials` error: ensure `AZURE_OPENAI_API_KEY` / `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` are set in `.env` or exported in your shell.
- `.env` invisible characters: if the endpoint or key contains stray characters, recreate `.env` using the `cat > .env` approach shown below.

Recreate `.env` safely:

```bash
cat > .env <<'EOF'
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-10-01-preview
EOF
```

## Security reminder
- Do not commit `.env` to source control. `.gitignore` includes `.env`.

