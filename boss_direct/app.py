# 不带登录爬取信息的app, 进行求职信息的爬取和分析
import requests


class Headers():
    def __init__(self) -> None:
        self.headers = {
            'User-Agent':"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }
        
    def add_referer(self, referer):
        if self.headers.get("Referer", None):
            print(f"Change Referer from {self.headers['Referer']}")
    

def main():
    _url = "https://www.zhipin.com/beijing/?sid=sem_pz_bdpc_dasou_title"
    home_page_content = requests.get(_url).content

