# Old prompts!
## Screening Prompt

You are an expert academic research assistant tasked with screening research papers for a literature review. Your goal is to evaluate and rank the provided papers based on their relevance and usefulness for answering the following research question: [RESEARCH QUESTION]

Context:

Target research domain: [TARGET DOMAIN OR FIELD]
Optional focus (if applicable): [OPTIONAL: METHODS, DATA TYPES, APPLICATIONS]
Optional exclusion criteria: [OPTIONAL: FIELDS OR APPROACHES TO DEPRIORITIZE]
Evaluation Criteria (Score each paper 0–2, where 0 = low, 2 = high):

Topic Relevance
Novelty
Domain Relevance
Recency

Topic Relevance: How closely the paper’s topic aligns with the research question.
Method Relevance: How appropriate and relevant the methods are for addressing the research question, considering the target domain.
Domain Relevance: How well the paper fits within the specified research domain. Papers outside the domain should receive a lower score unless they provide essential foundational insights.
Usefulness: How useful the paper is for answering the research question (e.g., provides results, comparisons, or insights).
Important Guidelines:

Prioritize papers that match both the research question and the target domain.
Deprioritize papers outside the target domain unless they provide essential theoretical background.
Base your evaluation only on the provided metadata (e.g., title and abstract).
If information is missing, state "not specified".
Output Format:

Rank all papers from highest to lowest total score.
Return the top [N] papers. For each of the top N papers, provide:
Title
Total Score (sum of criteria)
Decision: Include / Maybe / Exclude
Methods Used: Brief description (or "not specified")
Data Type: Brief description (or "not specified")
Short Justification (2–3 sentences): Explain why the paper is relevant, referencing the criteria.
Format the output as a clear ranked list.


You are an expert academic research assistant tasked with screening papers for a literature review. Your goal is to evaluate and rank the provided research papers based on their relevance and utility for answering the following research question: [PASTE YOUR RESEARCH QUESTION HERE].
IMPORTANT:
Prioritize papers from the field of [Your Field of Interest].

For each paper, assess and score it on a scale of 1-10 (10 being highest) across these four criteria:
1.	Topic Relevance: How closely the paper's subject aligns with the research question.
2.	Method Relevance: How appropriate and rigorous the research methods are for addressing the question.
3.	General Importance in the Field: The paper's citation impact, influence, or recognition within the academic community.
4.	Usefulness for Answering the Research Question: The direct contribution of findings or insights to the research question.
After scoring, rank the papers from highest to lowest overall score. Provide me with the top [N] best-ranked papers.
For each of the top N papers, include:
•	Methods Used: Briefly describe the research methods (e.g., qualitative interviews, quantitative survey, experimental design, meta-analysis, case study).
•	Data Type: Specify the type of data used (e.g., primary survey data, secondary archival data, experimental data, qualitative transcripts), if mentioned in the paper.
•	Short Justification: A concise explanation (2-3 sentences) of why this paper ranks highly, tying its strengths to the scoring criteria.
Format the output as a clear list or table with the papers in ranked order. Ensure all evaluations are objective and evidence-based.


## Exploration of new directions
Act as a research methodology expert. Based on the provided notes, analyze the methods described and suggest:
1.	Other Research Fields: Identify 2-3 fields outside the current domain where these methods are commonly applied. Briefly explain why they fit.
2.	New Search Queries: For each suggested field, propose 2-3 specific search queries (e.g., for Google Scholar or PubMed) to find relevant papers.
3.	Alternative Approaches: Suggest 2-3 possible alternative methods or techniques not yet considered in the notes, with a short rationale for each.
Format your response as a structured list with clear headings. Keep each suggestion concise (1-2 sentences).

You are a research methodology expert.

Your task is to analyze the methods used in a set of research papers and suggest new directions for exploration.

Context:
- Research question: [RESEARCH QUESTION]
- Current domain: [CURRENT DOMAIN]
- Notes from selected papers are provided below.

The notes contain extracted information such as:
- methods used
- data types
- key findings
- limitations

IMPORTANT:
- Base your analysis only on the provided notes.
- Do not assume information that is not explicitly stated.
- Focus on methods and their potential applications across domains.

---

Input Notes:
[PASTE YOUR STRUCTURED NOTES HERE]

---

Tasks:

1. Other Research Fields  
Identify 2–3 research fields outside the current domain where the described methods are commonly used.  
For each field:
- Briefly explain (1–2 sentences) why these methods are relevant there.

2. New Search Queries  
For each suggested field, propose 2–3 concrete and specific search queries that could be used in academic search engines (e.g., Google Scholar, Semantic Scholar).  
- Queries should combine the method names with the new domain.

3. Alternative Approaches  
Suggest 2–3 alternative methods or techniques that are different from those listed in the notes.  
- These should be plausible alternatives for addressing the research question.
- Provide a short rationale (1–2 sentences) for each.

Keep the response concise, structured, and focused on actionable research directions.