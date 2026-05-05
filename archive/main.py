from archive.src.retrieval import fetch_papers, clean_papers
from archive.src.prompting import load_prompt, summarize_paper
from archive.src.scoring import score_paper, compute_total
from archive.src.utils import save_csv
from archive.src.retrieval import fetch_papers
from archive.src.group_claims import group_claims_with_llm
from archive.src.generate_markdown import generate_markdown_report

import pandas as pd

# idea => find out what datasets they are using and how they evaluate the results

# define what you are looking for
QUERY = "Amodal Completion"
RESEARCH_QUESTION = "How does the occlusion level affect amodal completion?"
KEY_WORDS=["dataset", "metric", "evaluation"]
# define how many papers you want to retrieve
LIMIT = 5
# TODO year?!

# define where you want to retrieve the data from TODO
SOURCE = ""

# Step 1: Paper retrieval
print("Retrieving papers...")
df = fetch_papers("arxiv",QUERY, limit=10)
print(df[["title", "year"]])


if df.empty:
    raise ValueError("No papers retrieved. Check API or query.")

df = clean_papers(df)
# save the cleaned paper in a csv file
save_csv(df, "data/papers_clean.csv")

# Load prompts
print("Loading prompts...")
relevance_prompt = load_prompt("prompts/relevance_prompt.txt")
summary_prompt = load_prompt("prompts/summary_prompt.txt")
group_claims_prompt = load_prompt("prompts/group_claims_prompt.txt")

# Step 2: Scoring
print("Scoring papers...")
scores = []
for _, row in df.iterrows():
    s = score_paper(row, RESEARCH_QUESTION, relevance_prompt)
    scores.append(s)
    
df["relevance"] = scores
df["total_score"] = df["relevance"].apply(compute_total)
print(df[["title", "total_score"]])

print("Sorting the papers based on scores...")
df = df.sort_values(by="total_score", ascending=False)
save_csv(df, "outputs/papers_scored.csv")

# Step 3: Summaries + claims
claims_log = []

print("Summarizing papers...")
summaries = []
for _, row in df.iterrows():
    summary = summarize_paper(row, summary_prompt)
    print(summary)
    
    if "summary" in summary:
        summaries.append(summary["summary"])
    else:
        summaries.append("")

    if "key_claims" in summary:
        for claim in summary["key_claims"]:
            claims_log.append({
                "paper": row["title"],
                "claim": claim.get("claim"),
                "evidence": claim.get("evidence")
            })

df["summary"] = summaries
claims_df = pd.DataFrame(claims_log)
save_csv(claims_df, "outputs/claims_log.csv")

# Step 4: Group Claims
# Convert claims_df to list of dicts
print("Grouping claims...")
claims_list = claims_df.to_dict(orient="records")
themes = group_claims_with_llm(claims_list, group_claims_prompt)
print(themes)

# Save themes
import json
with open("outputs/themes.json", "w") as f:
    json.dump(themes, f, indent=2)

# Generate report
print("Generating report...")
generate_markdown_report(df, claims_df, themes)

print("Report generated: outputs/report.md")

print("Pipeline complete.")