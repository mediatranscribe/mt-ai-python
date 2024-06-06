import sys
import os
import pytest
import requests
from unittest.mock import patch

# Add the parent directory of 'mtai' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from mtai.prompts import Prompt


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


def test_list_prompts(mock_get):
    mock_get.return_value = {"status": "success", "data": []}
    try:
        response = Prompt.list()
        assert response == {"status": "success", "data": []}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error listing prompts: {e}")


def test_ask_question(mock_post):
    prompt = "What is the capital of India?"
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Prompt.ask_question(prompt)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error asking question: {e}")


def test_get_prompt_by_id(mock_get):
    prompt_id = "12345"
    mock_get.return_value = {"status": "success", "data": {}}
    try:
        response = Prompt.get_prompt_by_id(prompt_id)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error getting prompt by ID: {e}")


def test_delete_prompt_by_id(mock_delete):
    prompt_id = "67890"
    mock_delete.return_value = {"status": "success"}
    try:
        response = Prompt.delete_prompt_by_id(prompt_id)
        assert response == {"status": "success"}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error deleting prompt by ID: {e}")
