def detect_formatting(data):
    formatted_words = []
    heights = [h for h in data['height'] if h > 0]
    avg_height = sum(heights) / len(heights)

    for i, text in enumerate(data['text']):
        if text.strip() == "":
            continue

        bold = data['height'][i] > avg_height * 1.15
        italic = False  # heuristic placeholder

        formatted_words.append({
            'text': text + ' ',
            'bold': bold,
            'italic': italic
        })

    return formatted_words
