# -*- coding: utf-8 -*-
import time
import allure
from minium import MiniProgram, Callback
import minium


@allure.suite('路路游小程序')
@allure.feature('预约景区')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestYuYueJingQu_01(minium.MiniTest):

    def test_Yuyuejingqu(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()
        # 预约景区
        elements = self.page.get_elements(
            '//*[@id="tabBar_2"]')
        for element in elements:
            element.click()
        time.sleep(3)
        # 立即预约
        elements = self.page.get_elements(
            '/page/view/scroll-view[2]/view[1]/view[2]/view[2]/button')
        for element in elements:
            element.click()
        # 立即预约
        elements = self.page.get_elements(
            '/page/view/view[5]/view/button')
        for element in elements:
            element.click()
        # 选择出行日期
        elements = self.page.get_elements(
            '/page/view/view[2]/view[4]/view[2]')
        for element in elements:
            element.click()
        # 选择入园时段
        elements = self.page.get_elements(
            '/page/view/view[2]/view[6]/view[1]')
        for element in elements:
            element.click()
        # 选择预约游客
        elements = self.page.get_elements(
            '/page/view/view[3]/view[2]/view')
        for element in elements:
            element.click()
        # 确认预约
        elements = self.page.get_elements(
            '/page/view/view[5]/button')
        for element in elements:
            element.click()
        time.sleep(6)
        # 关闭弹窗
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[1]/text')
        for element in elements:
            element.click()
        # 点击客服
        elements = self.page.get_elements(
            '/page/view/view[4]')
        for element in elements:
            element.click()
        # 客服弹窗中点击联系客服按钮
        elements = self.page.get_elements(
            '/page/view/biz-service-modal/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view['
            '1]/view[3]/button')
        for element in elements:
            element.click()

        # 确认拨打
    def setUp_01(self) -> None:
        super().setUp()
        if self.page.path != "pages/index/index":
            self.app.redirect_to("pages/index/index")

    def test_handle_modal_01(self):
        callback = Callback()  # 监听回调, 阻塞当前主线程

        # 监听showModal回调, 确认由弹窗弹出
        self.app.hook_wx_method("showModal", callback=callback.callback)
        self.page.get_element('text="拨打4000922669?【仅为模拟】"').tap()  # 触发弹窗
        time.sleep(2)
        self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮

        time.sleep(3)

        # 返回页面至景区详情页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 返回页面至预约景区页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 返回页面至首页
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
