import json
from collections import defaultdict
from ollama import generate
from archive.src.prompting import load_prompt
from archive.src.utils import extract_json_payload



def group_claims_with_llm(claims, prompt_template):
    """
    claims = list of dicts:
    { "paper": ..., "claim": ..., "evidence": ... }
    """

    # Reduce size for prompt safety
    simplified = [
        f"- {c['claim']} (Source: {c['paper']})"
        for c in claims if c.get("claim")
    ]

    claims_text = "\n".join(simplified[:50])  # limit for safety

    prompt = prompt_template.format(claims_text=claims_text)
    print("Prompt is loaded")

    output = generate("llama3:latest", prompt)

    try:
        cleaned_response = extract_json_payload(output["response"])
        print(cleaned_response)
        return json.loads(cleaned_response)
    except:
        return {
            "themes": [
                {
                    "theme": "Uncategorized",
                    "claims": simplified
                }
            ],
            "error": output["response"]
        }
        
def group_claims_simple(claims):
    themes = defaultdict(list)

    for c in claims:
        text = c.get("claim", "").lower()

        if "improve" in text or "increase" in text:
            themes["Performance"].append(c)
        elif "limit" in text or "challenge" in text:
            themes["Limitations"].append(c)
        elif "method" in text or "approach" in text:
            themes["Methods"].append(c)
        else:
            themes["Other"].append(c)

    return {
        "themes": [
            {
                "theme": k,
                "claims": [x["claim"] for x in v]
            }
            for k, v in themes.items()
        ]
    }