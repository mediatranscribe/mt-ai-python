import sys
import os
import pytest
import requests
from unittest.mock import patch

# Add the parent directory of 'mtai' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from mtai.tags import Tag


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


def test_list_tags(mock_get):
    mock_get.return_value = {"status": "success", "data": []}
    try:
        response = Tag.list()
        assert response == {"status": "success", "data": []}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error listing tags: {e}")


def test_create_tag_from_title(mock_post):
    title = "Sample Tag"
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Tag.create_from_title(title)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating tag from title: {e}")


def test_create_tag_from_title_summary(mock_post):
    title = "Sample Tag"
    summary = "Sample Summary"
    count = 5
    mock_post.return_value = {"status": "success", "data": {}}
    try:
        response = Tag.create_from_title_summary(title, summary, count)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error creating tag from title and summary: {e}")


def test_get_tag_by_id(mock_get):
    tag_id = "12345"
    mock_get.return_value = {"status": "success", "data": {}}
    try:
        response = Tag.get_tag_by_id(tag_id)
        assert response == {"status": "success", "data": {}}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error getting tag by ID: {e}")


def test_delete_tag_by_id(mock_delete):
    tag_id = "67890"
    mock_delete.return_value = {"status": "success"}
    try:
        response = Tag.delete_tag_by_id(tag_id)
        assert response == {"status": "success"}
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error deleting tag by ID: {e}")
