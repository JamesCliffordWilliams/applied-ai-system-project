import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

music_db = [
    {"song": "Lo-fi Beats", "mood": "study", "tempo": "slow"},
    {"song": "Chill Vibes", "mood": "relax", "tempo": "slow"},
    {"song": "Hype Energy", "mood": "workout", "tempo": "fast"},
    {"song": "Focus Flow", "mood": "study", "tempo": "medium"},
]

def retrieve(query):
    results = []
    for item in music_db:
        if item["mood"] in query.lower():
            results.append(item)
    return results

def generate_response(query, results):
    if not results:
        return "No useful recommendation found."

    response = "I recommended these songs because they match your mood:\n"
    for r in results:
        response += f"- {r['song']} ({r['tempo']} tempo)\n"
    return response

def main():
    query = input("What kind of music do you want? ")

    retrieved = retrieve(query)

    logging.info(f"User query: {query}")
    logging.info(f"Results: {retrieved}")

    answer = generate_response(query, retrieved)

    print("\n" + answer)

if __name__ == "__main__":
    main()