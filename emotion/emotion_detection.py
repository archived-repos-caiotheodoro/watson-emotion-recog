


from emotion.setup import instanciate_watson


def analyze_emotion(text_to_analyze):
    
    nlu, features = instanciate_watson()

    response = nlu.analyze(
        text=text_to_analyze,
        features=features,
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    max_score = 0
    dominant_emotion = ""

    for emotion, score in emotions.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion

    return emotions, dominant_emotion
