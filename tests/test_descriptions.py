import sys
import os
import pytest
import requests
from unittest.mock import patch

# Add the parent directory of 'mtai' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from mtai.descriptions import Description


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


def test_list_description(mock_get):
    mock_get.return_value = {"status": "success", "data": []}
    try:
        response = Description.list()
        assert response == {"status": "success", "data": []}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error listing description: {e}")


def test_create_description_from_title(mock_post):
    title = "Sample Description"
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Description.create_from_title(title)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating Description from title: {e}")


def test_create_description_from_title_summary(mock_post):
    title = "Sample Description"
    summary = "Sample Summary"
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Description.create_from_title_summary(title, summary)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating Description from title and summary: {e}")


def test_get_description_by_id(mock_get):
    description_id = "664e033837511b57fa93dd2e"
    mock_get.return_value = {"status": "success", "data": {}}
    try:
        response = Description.get_description_by_id(description_id)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error getting Description by ID: {e}")


def test_delete_description_by_id(mock_delete):
    description_id = "664e033837511b57fa93dd2e"
    mock_delete.return_value = {"status": "success"}
    try:
        response = Description.delete_description_by_id(description_id)
        assert response == {"status": "success"}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error deleting Description by ID: {e}")
