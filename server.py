from flask import Flask, render_template, request, jsonify
from ibm_cloud_sdk_core.api_exception import ApiException
from emotion.emotion_detection import emotion_detector
from emotion.formatResponse import format_response

app = Flask(__name__)
#function docstring


@app.route('/')
def index():
    '''Renders the home page'''
    return render_template('index.html')

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion_route():
    '''Analyzes the emotion of the text provided in the request body'''

    text_to_analyze = request.json.get('text')
    emotions,dominant = emotion_detector(text_to_analyze)
    return jsonify(format_response(emotions,dominant))

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    '''Analyzes the emotion of the text provided in the query parameter'''
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        response = {
            "status": "error",
            "message": "Input text is blank. Please provide some text to analyze."
        }
        return jsonify(response), 400

    try:
        emotions,dominant = emotion_detector(text_to_analyze)
    except ApiException as api_exception:
        if "not enough text for language id" in str(api_exception):
            response = {
                "status": "error",
                "message": "The provided text is too short for analysis. \
                  Please provide a longer text."
            }
            return jsonify(response), 400
        response = {
            "status": "error",
            "message": "An error occurred while analyzing emotions. Please try again later."
        }
        return jsonify(response), 500

    if emotions is None:
        response = {
            "status": "error",
            "message": "Invalid text! Please try again."
        }
        return jsonify(response), 400
    
    if dominant is None:
        response = {
            "status": "error",
            "message": "Invalid text! Please try again."
        }
        return jsonify(response), 400

    return jsonify(format_response(emotions,dominant))

if __name__ == '__main__':
    app.run(debug=True)
