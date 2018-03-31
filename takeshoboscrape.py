import requests
import parse
import os

HEADERS = { 'Referer': 'http://staticfilemanga.takeshobo.co.jp/global-image/manga/tsukushiakihito/madeinabyss/0047/book/_SWF_Window.html',
            'Save-Data': 'on',
            'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'X-Requested-With': 'ShockwaveFlash/29.0.0.113'}

# Pattern Sample: http://mangalifewin.takeshobo.co.jp/global-image/manga/tsukushiakihito/madeinabyss/034/book/
PARSE_PATTERN = "http://mangalifewin.takeshobo.co.jp/global-image/manga/{author}/{series}/{bookid}/book/"

# Translation Sample: http://staticfilemanga.takeshobo.co.jp/global-image/manga/tsukushiakihito/madeinabyss/034/book/books/images/2/1.jpg
TRANSLATION_SAMPLE = "http://staticfilemanga.takeshobo.co.jp/global-image/manga/{author}/{series}/{bookid}/book/books/images/2/{page}.jpg"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def download(url, path=""):
    xtract = parse.parse(PARSE_PATTERN, url)
    print(f"Details: {xtract}")
    bookid = xtract['bookid']
    series = xtract["series"]
    author = xtract["author"]
    directory = os.path.join(path, author, series, bookid)
    create_directory(directory)
    print(f"Saving To: {directory}")
    status_code = 200
    page = 1

    while status_code == 200:
        print(f"Downloading Page: {page}")
        r_url = TRANSLATION_SAMPLE.format(bookid=bookid, page=page, author=author, series=series)
        print(f"RawURL: {r_url}")
        req = requests.get(r_url, headers=HEADERS)
        status_code = req.status_code
        print(f"Status Code: {status_code}")
        if status_code == 200:
            with open(os.path.join(directory, f"{page}.jpg"), "wb") as f:
                f.write(req.content)
        page += 1
    print("Done")

if __name__ == "__main__":
    print("Takeshobo Scraper")
    print("Made for Made in Abyss")
    print("-----Sample Link------")
    print("http://mangalifewin.takeshobo.co.jp/global-image/manga/tsukushiakihito/madeinabyss/034/book/\n")
    download(input("Enter Link: "))
