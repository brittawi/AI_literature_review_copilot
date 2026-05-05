from ollama import generate
import json

from archive.src.utils import extract_json_payload

def load_prompt(path):
    with open(path, "r") as f:
        return f.read()
    
def prompt_llm(prompt, llm='llama3:latest'):
    return generate(llm, prompt)


# summarizing the paper
def summarize_paper(paper, prompt_template):
    prompt = prompt_template.format(
        title=paper["title"],
        abstract=paper["abstract"]
    )

    response = generate('llama3:latest', prompt)
    
    try:
        clean_response = extract_json_payload(response["response"])
        return json.loads(clean_response)
    except:
        return {"error": response["response"]}