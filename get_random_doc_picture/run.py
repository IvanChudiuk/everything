import requests
import os

from config import app_config
from modules import logger

logger = logger.Logger(
    name=os.path.basename(__file__),
    level=app_config["logging"]["level"],
    log_file=app_config["logging"]["file"],
    format_str=app_config["logging"]["format"],
)


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
        logger.info(f"Random Dog Image URL: {data['message']}")
        return data["message"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error occurred: {e}")
    except ValueError as e:
        logger.error(f"Error parsing JSON: {e}")
    except KeyError as e:
        logger.error(f"Unexpected response structure: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_random_dog_image(url=app_config["SOURCE_URL"])
