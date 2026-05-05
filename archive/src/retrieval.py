import requests
import pandas as pd
import time
import arxiv


API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# TODO add year?! If I want to focus on year

def fetch_papers(source, query, limit=20):
    if source == "arxiv":
        return fetch_arxiv_papers(query, max_results=limit)
    
    elif source == "semantic_scholar":
        return fetch_papers_semantic_scholar(query, limit)
    
    else:
        raise ValueError(f"Unknown source: {source}")

def fetch_arxiv_papers(query, max_results=10):
    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []

        for result in search.results():
            results.append({
                "title": result.title,
                "abstract": result.summary,
                "year": result.published.year,
                "doi": result.doi,
                "url": result.entry_id,
                "source": "arxiv"
            })

        df = pd.DataFrame(results)
        return df

    except Exception as e:
        print(f"Error fetching arXiv papers: {e}")
        return pd.DataFrame()

def fetch_papers_semantic_scholar(query, limit=5, retries=3):
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,abstract,url,citationCount",
        #year,
        #minCitationCount,
        #venue
        
        
    }
    
    headers = {
        "Connection": "keep-alive",
            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36",
            "X-S2-UI-Version": "20166f1745c44b856b4f85865c96d8406e69e24f",
            "sec-ch-ua-platform": '"Android"',
            "Accept": "*/*",
            "Origin": "https://www.semanticscholar.org",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.semanticscholar.org/search?year%5B0%5D=2018&year%5B1%5D=2022&q=multi%20label%20text%20classification&sort=relevance",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    # if api_key:
    #     headers["x-api-key"] = api_key
        
    for attempt in range(retries):
        try:
            response = requests.get(API_URL, params=params, headers=headers)

            # 🔍 Check status early
            if response.status_code == 200:
                data = response.json()
                papers = data.get("data", [])
                return pd.DataFrame(papers)

            elif response.status_code == 429:
                print(f"Rate limited. Waiting before retry... (attempt {attempt+1})")
                time.sleep(5 * (attempt + 1))  # exponential backoff

            else:
                print(f"Error {response.status_code}: {response.text}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(2)

    print("Failed to fetch papers after retries.")
    return pd.DataFrame()

def clean_papers(df):
    #df = df[["title", "abstract", "year", "doi", "url"]]
    df = df[["title", "abstract", "year", "url"]]
    df = df.dropna(subset=["abstract"])
    return df