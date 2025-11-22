# Artificial-Intelligence

This has all of the core software files. 

## Installing Libraries

Can use a .venv if you want, but the problem with that is that gpiozero is hard to get on a .venv because of the way it accesses the hardware, and I got ome errors, but if you install
it correctly it would work.

pip install -r requirements.txt

## Configuring LLM/AI

There are two ways to get your llm, with different providers. Openrouter can be used, or Ollama can be used. Ollama is a local provider so if you want your llm on your local computer/ locally
installed on the pi then use Ollama

### Openrouter

1. Create openrouter account at https://openrouter.ai
2. Create a new api key
3. Replace your_api_key in .env.example with your actually api key
4. choose a model, with image input and tool calling by going to Models on Openrouter and using hte filters, preferrably a more powerful model
5. Once it is found, click it and then click the little copy icon to get its id Ex: looks like "google/gemini-3-pro-preview"
6. replace model with this so it looks like:
   llm = ChatOpenAI(
    model="meta-llama/llama-4-scout:free", # this is only temporary and it will not work for interpret, for that it requires a more
    # high end lm. But I ran out of free credits, so this is here for now, bu in order for full functionality, change to a more powerful model like gpt-4o-mini or similar
    api_key=my_key, # your api key
    base_url="https://openrouter.ai/api/v1", # default base url for openrouter
)
7. Free credits from a new account should allow interrpet which requires a more poerful model to run.

### Ollama

For installing on pi 5, its easy, but it just requires good space, if there is less space then use the network. For installing it

Locally on Pi 5:
1. Install Ollama on https://ollama.com
2. Browse models that have an image output and find one (I use gemma3:4b)
3. If using Ollama, since local models don't have high performance, and in order to get high performance lots of space mut be used interpret.py won't work
4. Go to the pi terminal and run "ollama run gemma3:4b" or replace gemma3:4B with your model
5. Just use the code as normal without base_url

Through internet by installing on computer: installes on computer then gives it to the pi 5
1.
