"""Detect emotions in English text with the Skills Network Watson service."""

import json

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the expected response shape when Watson cannot analyze the text."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion for the supplied text."""
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(
            EMOTION_URL,
            json=payload,
            headers=MODEL_HEADERS,
            timeout=30,
        )
    except requests.RequestException:
        return _empty_result()

    if response.status_code == 400:
        return _empty_result()

    if response.status_code != 200:
        return _empty_result()

    try:
        formatted_response = json.loads(response.text)
        scores = formatted_response["emotionPredictions"][0]["emotion"]
        result = {name: scores[name] for name in EMOTION_NAMES}
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        return _empty_result()

    result["dominant_emotion"] = max(
        EMOTION_NAMES,
        key=lambda name: result[name],
    )
    return result
