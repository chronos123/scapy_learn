from bs4 import BeautifulSoup


class HomePageParser:
    def __init__(self, page):
        # page: 首页内容
        self.page = BeautifulSoup(page, "html.parser")

    def post_job_classer(self):
        # 从首页post, 得到具体某一个职业的招聘信息界面
        data = {
            
        }
    
    
