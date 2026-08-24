"""Deploy the emotion detection application through Flask."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze the text supplied by the web interface and format the result."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    emotion_result = emotion_detector(text_to_analyse)
    dominant_emotion = emotion_result["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']}, "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )


@app.route("/")
def render_index_page():
    """Render the application's main page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
