import pandas as pd

def save_csv(df, path):
    df.to_csv(path, index=False)


def load_csv(path):
    return pd.read_csv(path)

def extract_json_payload(text):
    """Extracts a JSON string from a block of text by finding the first '{' and last '}'."""
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return text[start:end + 1]
    return text