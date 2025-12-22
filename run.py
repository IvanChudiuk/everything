import requests

from config import app_config


def get_random_dog_image(url: str) -> str:
    """
    Fetches a link to the random dog image from the provided URL.
    
    Args:
        url (str): a link to the data source with random pictures of dogs
    Returns:
        str: URL of a random dog image
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        print("Random Dog Image URL:", data["message"])
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: {e}")


if __name__ == "__main__":
    get_random_dog_image(
        url=app_config["SOURCE_URL"]
        )