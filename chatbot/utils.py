def format_result(result):
    return {
        "patent_id": result["patent_id"],
        "section": result["section"],
        "text": result["text"],
        "citation": f"{result['patent_id']} — §[{result['section']}]: {result['text'][:100]}..."
    }
