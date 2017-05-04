import requests
from bs4 import BeautifulSoup

def get_head_text(url, head_tag):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup.find(head_tag).text
    except Exception as e:
        return None

def main():
    url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    button = get_head_text(url, 'button.text') # 讀取不存在的標籤
    print(button)
    title = get_head_text(url, 'title')
    print('網頁的標題 (title) = {}'.format(title))
    p = get_head_text(url, 'p')
    print('段落 (p) = {}'.format(p))

if __name__ == '__main__':
    main()