import os
import requests
from urllib.parse import urlparse
import os

# function download_file_from_url

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

    # 简单浏览器请求头，提高源站兼容性（无需设置变量）
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        ),
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    # 统一禁用代理（不读取环境代理）
    session = requests.Session()
    session.trust_env = False

    with session.get(
        url,
        stream=True,
        headers=headers,
        timeout=(20, 120),  # 连接20s，读120s
        verify=False,
        allow_redirects=True,
        proxies={"http": None, "https": None},
    ) as response:
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    return file_path