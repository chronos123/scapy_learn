from bs4 import BeautifulSoup
from locators.page_locators import JobPageLocators


class HomePageParser:
    def __init__(self, page):
        # page: 首页内容
        self.page = BeautifulSoup(page, "html.parser")

    def post_job_classer(self):
        # 从首页post, 得到具体某一个职业的招聘信息界面
        data = {
            
        }

    def locate_job_classifier(self):
        class_wraper = self.page.find(JobPageLocators.job_menu_wrapper[0], JobPageLocators.job_menu_wrapper[1])
        classes = class_wraper.findAll(JobPageLocators.job_menu)
        for job_class in classes:
            link = job_class.a
        pass

    
