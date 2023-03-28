import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """
        Checks whether 'url' is a valid URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    Returns all image URLs on a single 'url'
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    webpage = requests.get(url, headers=headers)
    soup = bs(webpage.content, 'html.parser')

    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
         # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # try:
        #     pos = img_url.index("?")
        #     img_url = img_url[:pos]
        # except ValueError:
        #     pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname, filename):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # join the filename to the pathname
    filepath = os.path.join(pathname, filename)
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024),
                    f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filepath, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for i, img in enumerate(imgs):
        filename = f'{i}.png'
        # for each image, download it
        download(img, path, filename)


if __name__ == '__main__':
    url = "https://discord.com/channels/924589763820945439/924589763820945443"
    main(url, "yandex")
