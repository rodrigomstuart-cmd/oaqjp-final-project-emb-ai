"""Unit tests for the emotion detection package."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate the five supported dominant emotions and error handling."""

    @staticmethod
    def _watson_response(dominant_emotion):
        """Build a Watson-compatible response with the requested dominant emotion."""
        scores = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
        }
        scores[dominant_emotion] = 0.95
        return Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": scores}]}),
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_required_dominant_emotions(self, mock_post):
        """Identify the expected dominant emotion for the five course phrases."""
        expected_by_text = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }

        def response_for_text(*_args, **kwargs):
            text = kwargs["json"]["raw_document"]["text"]
            return self._watson_response(expected_by_text[text])

        mock_post.side_effect = response_for_text

        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request_returns_empty_result(self, mock_post):
        """Return the required None values when Watson responds with HTTP 400."""
        mock_post.return_value = Mock(status_code=400, text="")

        result = emotion_detector("")

        self.assertIsNone(result["anger"])
        self.assertIsNone(result["disgust"])
        self.assertIsNone(result["fear"])
        self.assertIsNone(result["joy"])
        self.assertIsNone(result["sadness"])
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
