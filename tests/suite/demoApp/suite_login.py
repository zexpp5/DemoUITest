# -*- coding: utf-8 -
from tests.page.demoApp.page_home import HomePage


def login(driver, data):
    phone = data['phone']
    password = data['password']
    # 点击首页apply按钮,进入CheckPhone页面
    HomePage(driver).click_apply_action()