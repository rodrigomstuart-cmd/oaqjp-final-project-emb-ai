"""Expose the public interface of the EmotionDetection package."""

# The course rubric requires this package to be named EmotionDetection.
# pylint: disable=invalid-name

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
