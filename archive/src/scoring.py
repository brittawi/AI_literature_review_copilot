from archive.src.prompting import prompt_llm
import re


# scoring the paper

def score_paper(paper, research_question, prompt_template):
    
    # adjust the prompt to the paper and research question
    prompt = prompt_template.format(
        research_question=research_question,
        title=paper["title"],
        abstract=paper["abstract"]
    )
    
    response = prompt_llm(prompt)
    
    return parse_scores(response["response"])
    
    # try:
    #     return json.loads(response["response"])
    # except:
    #     return {"error": response["response"]}
    

def compute_total(score_dict):
    keys = ["topic_match", "method_relevance", "recency", "empirical_strength"]
    return sum(score_dict.get(k, 0) for k in keys if isinstance(score_dict, dict))

def extract_score(text, key):
    match = re.search(rf"{key}[^0-9]*([0-2])", text, re.IGNORECASE)
    return int(match.group(1)) if match else 0


def parse_scores(output):
    return {
        "topic_match": extract_score(output, "topic"),
        "method_relevance": extract_score(output, "method"),
        "recency": extract_score(output, "recency"),
        "empirical_strength": extract_score(output, "empirical"),
        "justification": output
    }

