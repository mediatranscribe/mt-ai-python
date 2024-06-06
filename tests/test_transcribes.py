import sys
import os
import pytest
import requests
from unittest.mock import patch

# Add the parent directory of 'mtai' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from mtai.transcribes import Transcribe


@pytest.fixture
def mock_get():
    with patch("mtai.base.MTAIApiRequests.get") as mock:
        yield mock


@pytest.fixture
def mock_post():
    with patch("mtai.base.MTAIApiRequests.post") as mock:
        yield mock


@pytest.fixture
def mock_delete():
    with patch("mtai.base.MTAIApiRequests.delete") as mock:
        yield mock


def test_list_transcribes(mock_get):
    mock_get.return_value = {"status": "success", "data": []}
    try:
        response = Transcribe.list()
        assert response == {"status": "success", "data": []}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error listing transcribes: {e}")


def test_get_transcribe_by_id(mock_get):
    transcribe_id = "12345"
    mock_get.return_value = {"status": "success", "data": {}}
    try:
        response = Transcribe.get_transcribe_by_id(transcribe_id)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error getting transcribe by id: {e}")


def test_create_transcribe_from_audio_url(mock_post):
    audio_url = "http://example.com/audio.mp3"
    services = ["service1", "service2"]
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Transcribe.create_transcribe_from_audio_url(audio_url, services)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating transcribe from audio URL: {e}")


def test_create_transcribe_from_media_file(mock_post):
    media_file = "/path/to/media/file.mp4"
    services = ["service1", "service2"]
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Transcribe.create_transcribe_from_media_file(media_file, services)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating transcribe from media file: {e}")


def test_create_transcribe_from_youtube_video(mock_post):
    youtube_url = "http://youtube.com/video"
    services = ["service1", "service2"]
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Transcribe.create_transcribe_from_youtube_video(
            youtube_url, services
        )
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating transcribe from YouTube video: {e}")


def test_get_transcribe_by_id_method(mock_get):
    transcribe_id = "67890"
    mock_get.return_value = {"status": "success", "data": {}}
    try:
        response = Transcribe.get_transcribe_by_id(transcribe_id)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error getting transcribe by id: {e}")


def test_delete_transcribe_by_id(mock_delete):
    transcribe_id = "67890"
    mock_delete.return_value = {"status": "success"}
    try:
        response = Transcribe.delete_transcribe_by_id(transcribe_id)
        assert response == {"status": "success"}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error deleting transcribe by id: {e}")
