from scrapegraphai.graphs import SmartScraperGraph
import nest_asyncio
nest_asyncio.apply()

graph_config = {
    "llm":{
        "model":"ollama/llama3.2",
        "temperature":0,
        "format": "json",
        "base_url": "http://localhost:11434"
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specify the model for embeddings
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "verbose": True
}
screener = SmartScraperGraph(
    prompt = "List all the projects with their description",
    source = "https://perinim.github.io/projects",
    config = graph_config
)

result = screener.run()

print("results" , result)

import json

op = json.dumps(result, indent=2)

line_list = op.split("\n")

for line in line_list:
    print(line)
