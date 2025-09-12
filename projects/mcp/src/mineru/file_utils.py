import os
import requests
from urllib.parse import urlparse
import os

def download_file_from_url(url: str, download_dir: str = None) -> str:
    """
    Download a remote file and save it to the specified directory.

    Args:
        url (str): The URL of the file to download.
        download_dir (str): Local directory to save the downloaded file.

    Returns:
        str: Absolute path to the downloaded file.
    """
    download_dir = download_dir or "./downloads"
    os.makedirs(download_dir, exist_ok=True)

    parsed = urlparse(url)
    file_name = os.path.basename(parsed.path) or "downloaded_file"
    file_path = os.path.join(download_dir, file_name)

    print(f"Downloading {url} to {file_path}")
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    return file_path