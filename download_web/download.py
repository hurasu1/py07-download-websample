import os
import pprint
import time
import urllib.error
import urllib.request


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def get_file_name(url):
    file_name = url.split("/")
    return file_name[len(file_name)-1]


def main():
    url = "https://cdn-ak.f.st-hatena.com/images/fotolife/k/knalaboratory/20190422/20190422215930.jpg"
    save_dir = "../image_dir"

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    save_path = save_dir + "/" + get_file_name(url)
    download_file(url, save_path)


if __name__ == "__main__":
    main()
