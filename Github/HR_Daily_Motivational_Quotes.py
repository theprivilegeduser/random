import requests

def get_daily_quote():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        response.raise_for_status()  # Raises an error for bad responses
        quote_data = response.json()
        # Extract and return the quote and author
        quote = f"{quote_data[0]['q']} – {quote_data[0]['a']}"
        return quote
    except requests.RequestException as e:
        print("Error fetching the quote:", e)
        return "Believe in yourself and all that you are. – Christian D. Larson"  # Fallback quote

if __name__ == "__main__":
    print(get_daily_quote())
