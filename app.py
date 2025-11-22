import os
from dotenv import load_dotenv
from openai import AzureOpenAI


# Load environment variables from .env (if present)
load_dotenv()

# Set your Azure OpenAI resource details
# You can find these in the Azure portal under your Azure OpenAI resource
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://your-resource-name.openai.azure.com/"
# Accept either AZURE_OPENAI_API_KEY or AZURE_OPENAI_KEY for compatibility
api_key = os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_KEY")
model_name = "gpt-4.1-mini"                # The name of your model deployment (e.g., "gpt-4o-deployment")

print(azure_endpoint, api_key, model_name)

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_version="2024-02-01",  # Use the appropriate API version
    api_key=api_key,
)

print("Welcome to the Azure OpenAI Chat CLI!")
print("Type your questions below (type 'quit', 'exit', or 'q' to stop):")
print("-" * 40)

while True:
    query = input("You: ").strip()
    if query.lower() in {"quit", "exit", "q"}:
        print("Goodbye!")
        break
    if not query:
        continue

    # Define the messages for the chat completion, using the user's query
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": query},
    ]

    try:
        # Create the chat completion
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=100,  # Optional: Limit the number of tokens in the response
            temperature=0.7, # Optional: Control the creativity of the response
        )

        # Print the assistant's response
        print(f"{model_name}: {completion.choices[0].message.content}")
        print("-" * 40)  # Separator for readability

    except Exception as e:
        print(f"An error occurred: {e}")
