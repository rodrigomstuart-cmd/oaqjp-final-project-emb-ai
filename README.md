# Emotion Detection Web Application

Final project for the IBM course **Developing AI Applications with Python and
Flask**. The application sends English text to the Skills Network Watson NLP
service and reports scores for anger, disgust, fear, joy, and sadness, together
with the dominant emotion.

## Project structure

```text
EmotionDetection/
  __init__.py
  emotion_detection.py
static/
  mywebscript.js
templates/
  index.html
server.py
test_emotion_detection.py
requirements.txt
```

## Environment

The Watson endpoint is accessible from the IBM Skills Network Cloud IDE. Use
Python 3.11 in that environment:

```bash
python3.11 -m pip install -r requirements.txt
python3.11 -m unittest -v
python3.11 -m pylint server.py EmotionDetection test_emotion_detection.py
python3.11 server.py
```

Open port `5000` through the Skills Network **Launch Application** tool to use
the web interface.
