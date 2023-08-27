import unittest
from emotion_detection import analyze_emotion


testCases  = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear")
]
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        for text, expected in testCases:
            with self.subTest(text=text, expected=expected):
                _, dominant_emotion = analyze_emotion(text)
                self.assertEqual(dominant_emotion, expected)

if __name__ == '__main__':
    unittest.main()
