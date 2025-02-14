import re
import requests
import json

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"


def expand_query(user_query):
    """
    Expands a search query using Llama via Ollama API.
    """

    prompt = (
        f"Expand this search query into a **short and concise** descriptive phrase for image search. "
        "Do **not** provide multiple variations or explanations. "
        "Just return a single refined phrase that is useful for finding an image. "
        f"Query: {user_query}"
    )

    try:
        # Send request to Ollama
        response = requests.post(
            OLLAMA_URL,
            json={"model": "llama3.2:3b", "prompt": prompt}
        )
        response.raise_for_status()
        response_text = response.text.strip()

        # Split the response by lines (each expected to be a JSON object)
        lines = response_text.splitlines()
        responses = []
        for line in lines:
            try:
                obj = json.loads(line)
                resp = obj.get("response", "").strip()
                responses.append(resp)
            except json.JSONDecodeError:
                continue

        # Combine all fragments
        final_expansion = " ".join(responses).strip()

        # Clean extra whitespace
        final_expansion = re.sub(r"\s+", " ", final_expansion).strip()

        # Fallback if too short
        if not final_expansion or len(final_expansion.split()) < 3:
            final_expansion = f"A high-quality image of {user_query}"

        return final_expansion

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        return f"A relevant image of {user_query}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"A relevant image of {user_query}"


if __name__ == "__main__":
    test_queries = ["Ball"]
    for query in test_queries:
        expanded = expand_query(query)
        print(f"Original: {query} | Expanded: {expanded}")
