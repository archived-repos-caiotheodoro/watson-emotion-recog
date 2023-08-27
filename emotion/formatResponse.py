
def format_response(emotions):
    formatted = ""
    for emotion, score in emotions.items():
        formatted += f"{emotion.capitalize()}: {score*100:.2f}%, "
    return formatted[:-2]