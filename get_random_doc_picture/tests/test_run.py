from unittest.mock import patch, MagicMock

from run import get_random_dog_image


@patch("run.requests.get")
@patch("run.logger")
def test_get_random_dog_image_success(mock_logger, mock_get):
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {"message": "https://example.com/dog.jpg"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Call the function
    result = get_random_dog_image("https://api.example.com/random")

    # Assert the result
    assert result == "https://example.com/dog.jpg"
    mock_logger.info.assert_called_once_with(
        "Random Dog Image URL: https://example.com/dog.jpg"
    )


@patch("run.requests.get")
@patch("run.logger")
def test_get_random_dog_image_request_exception(mock_logger, mock_get):
    # Mock request exception
    mock_get.side_effect = Exception("Network error")

    # Call the function
    result = get_random_dog_image("https://api.example.com/random")

    # Assert no result (function doesn't return on error)
    assert result is None
    mock_logger.error.assert_called_once_with(
        "An unexpected error occurred: Network error"
    )


@patch("run.requests.get")
@patch("run.logger")
def test_get_random_dog_image_json_error(mock_logger, mock_get):
    # Mock response with invalid JSON
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response

    # Call the function
    result = get_random_dog_image("https://api.example.com/random")

    # Assert
    assert result is None
    mock_logger.error.assert_called_once_with("Error parsing JSON: Invalid JSON")


@patch("run.requests.get")
@patch("run.logger")
def test_get_random_dog_image_key_error(mock_logger, mock_get):
    # Mock response without 'message' key
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"error": "No message"}
    mock_get.return_value = mock_response

    # Call the function
    result = get_random_dog_image("https://api.example.com/random")

    # Assert
    assert result is None
    mock_logger.error.assert_called_once_with(
        "Unexpected response structure: 'message'"
    )
