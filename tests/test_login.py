# -*- coding: utf-8 -*-
import time
import allure
from minium import MiniProgram, Callback
import minium
import pyautogui


@allure.suite('路路游小程序')
@allure.feature('首页')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestShouYe_01(minium.MiniTest):

    def test_shouye(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()

    def setUp_01(self) -> None:
        super().setUp()
        if self.page.path != "pages/index/index":
            self.app.redirect_to("pages/index/index")

    def test_handle_modal_01(self):
        callback = Callback()  # 监听回调, 阻塞当前主线程

        # 监听showModal回调, 确认由弹窗弹出
        self.app.hook_wx_method("showModal", callback=callback.callback)
        self.page.get_element('text="当前为测试模拟环境，请勿进行真实业务行为!"').tap()  # 触发弹窗
        time.sleep(2)
        self.native.handle_modal("知道了")  # 点击弹窗的"确定"按钮
        # 定位
        elements = self.page.get_elements('/page/view/biz-index-head/view/view')
        for element in elements:
            element.click()
        time.sleep(2)
        # # 通过 XPath 获取并点击“选择城市”按钮
        elements = self.page.get_elements('/page/lee-select-city/view/view/view/scroll-view[1]/view/view[2]')
        for element in elements:
            element.click()

        time.sleep(2)
        # 选择省份(安徽)
        elements = self.page.get_elements(
            '/page/lee-select-city/view/view/view/scroll-view[1]/view/lee-latter-list/view/view[1]/view[2]/view[1]')
        for element in elements:
            element.click()
        time.sleep(2)
        # 选择城市(安庆市)
        elements = self.page.get_elements(
            '/page/lee-select-city/view/view[2]/view/scroll-view[2]/view/lee-latter-list/view/view[1]/view[2]/view')
        for element in elements:
            element.click()
        time.sleep(2)

        # 确认选择

    def test_handle_modal_02(self):
        callback = Callback()  # 监听回调, 阻塞当前主线程

        # 监听showModal回调, 确认由弹窗弹出
        self.app.hook_wx_method("showModal", callback=callback.callback)
        self.page.get_element('text="安徽省-安庆市!"').tap()  # 触发弹窗
        time.sleep(2)
        self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
    #
    # #     # 搜索
    # #     time.sleep(3)
    # #     elements = self.page.get_elements(
    # #         '/page/view/biz-index-head/view/navigator')
    # #     for element in elements:
    # #         element.click()
    # #     time.sleep(3)
    # #     #     # 选择景点进行搜索
    # #     #     time.sleep(3)
    # #     #     elements = self.page.get_elements(
    # #     #         '/page/view/view[1]/picker/view')
    # #     #     for element in elements:
    # #     #         element.click()
    # #     #
    # #     # def test_handle_modal_03(self):
    # #     #     callback = Callback()  # 监听回调, 阻塞当前主线程
    # #     #
    # #     #     # 监听showModal回调, 确认由弹窗弹出
    # #     #     self.app.hook_wx_method("showModal", callback=callback.callback)
    # #     #
    # #     #     self.page.get_element('text="景点"').tap()  # 触发弹窗
    # #     #     pyautogui.scroll(2)
    # #     #     time.sleep(2)
    # #     #     self.native.handle_modal("确定")  # 点击弹窗的"确定"按钮
    # #     #
    # #     #     time.sleep(3)
    # #     #     elements = self.page.get_elements(
    # #     #         '/page/view/biz-index-head/view/navigator')
    # #     #     for element in elements:
    # #     #         element.send_keys('武侯祠')
    # #     #     # 返回首页
    # #     # 武侯祠(历史记录)
    # #     elements = self.page.get_elements(
    # #         '/page/view/view[2]/view/view[2]/view')
    # #     for element in elements:
    # #         element.click()
    # #     # 武侯祠(确定选择)
    # #     elements = self.page.get_elements(
    # #         '/page/view/view[2]/list/view/view/navigator')
    # #     for element in elements:
    # #         element.click()
    # #
    # #     # 立即预约
    # #     elements = self.page.get_elements(
    # #         '/page/view/view[5]/view/button')
    # #     for element in elements:
    # #         element.click()
    # #     time.sleep(3)
    # #     # 确认预约
    # #     elements = self.page.get_elements(
    # #         '/page/view/view[5]/button')
    # #     for element in elements:
    # #         element.click()
    # #     time.sleep(8)
    # #     # 关闭弹窗
    # #     elements = self.page.get_elements(
    # #         '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[1]/text')
    # #     for element in elements:
    # #         element.click()
    # #     # 返回上一页(返回至景点页面)
    # #     elements = self.page.get_elements(
    # #         '/page/view/ml-title/view/view/view/view[1]/text')
    # #     for element in elements:
    # #         element.click()
    # #     # 返回上一页(返回至搜索页面)
    # #     elements = self.page.get_elements(
    # #         '/page/view/ml-title/view/view/view/view[1]')
    # #     for element in elements:
    # #         element.click()
    # #     # 返回首页(页面路径跳转)
    # #
    # # def setUp_03(self):
    # #     if self.page.path != "pages/index/index":
    # #         self.app.navigate_to("pages/index/index")
    # #     time.sleep(3)


@allure.suite('首页')
@allure.feature('购买年卡')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestShouYe_02(minium.MiniTest):
    def test_goumainianka(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()

        # 购买年卡
        time.sleep(3)
        elements = self.page.get_elements(
            '//*[@id="nav-item-notice"]/navigator[1]/view')
        for element in elements:
            element.click()
        time.sleep(2)
        # 滑动轮播图
        elements = self.page.get_elements('/page/view/swiper')
        for i in range(min(3, len(elements))):
            element = elements[i]
            element.drag_and_drop_by_offset(100, 0)
        time.sleep(2)
        # 返回
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        time.sleep(2)


@allure.suite('首页')
@allure.feature('立即绑卡')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestShouYe_03(minium.MiniTest):
    def test_goumainianka(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()
        # 立即绑卡
        elements = self.page.get_elements(
            '//*[@id="nav-item-notice"]/navigator[2]/view')
        for element in elements:
            element.click()
        # 输入卡片激活码
        elements = self.page.get_elements(
            '/page/view/view[2]/view[1]/input')
        for element in elements:
            element.send_keys('QTSCEPAK')
        # 姓名
        elements = self.page.get_elements(
            '/page/view/view[2]/view[2]/input')
        for element in elements:
            element.send_keys('刘永信')
        # 手机号
        elements = self.page.get_elements(
            '/page/view/view[2]/view[3]/input')
        for element in elements:
            element.send_keys('15970710891')
        # 身份证号
        elements = self.page.get_elements(
            '/page/view/view[2]/view[4]/input')
        for element in elements:
            element.click('342124196412235417')
        # 勾选协议
        elements = self.page.get_elements(
            '/page/view/view[3]/checkbox-group/label/checkbox')
        for element in elements:
            element.click()
        # # 查看用户协议
        # elements = self.page.get_elements(
        #     '/page/view/view[3]/navigator')
        # for element in elements:
        #     element.click()
        # 确定绑定
        elements = self.page.get_elements(
            '/page/view/view[3]/checkbox-group/label/checkbox')
        for element in elements:
            element.click()
        # 弹窗中确定
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[3]/button[2]')
        for element in elements:
            element.click()
        # 关闭绑定成功弹窗
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[1]/text')
        for element in elements:
            element.click()
        # 返回首页
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()


@allure.suite('首页')
@allure.feature('我的预约')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestShouYe_04(minium.MiniTest):
    def test_lijibangka(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()
        time.sleep(3)
        # 我的预约
        elements = self.page.get_elements(
            '//*[@id="nav-item-notice"]/navigator[3]/view')
        for element in elements:
            element.click()
        # 可使用
        elements = self.page.get_elements(
            '/page/view/view/view[2]')
        for element in elements:
            element.click()
        # 入园码
        elements = self.page.get_elements(
            '/page/view/swiper/swiper-item[2]/scroll-view/view[1]/view[2]/view[2]/view[4]/button')
        for element in elements:
            element.click()
        # 取消预约
        elements = self.page.get_elements(
            '/page/view/view[4]/button')
        for element in elements:
            element.click()
        # 确认取消
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[3]/button[2]')
        for element in elements:
            element.click()
        time.sleep(5)
        # 关闭取消成功弹窗
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[3]/button')
        for element in elements:
            element.click()
        # 返回上一页(返回至我的预约)
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 返回上一页(返回至首页)
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()


# @allure.suite('首页')
# @allure.feature('公告')
# @minium.ddt_class(testNameFormat="%(name)s_%(index)s")
# class TestShouYe_05(minium.MiniTest):
#     def test_gonggao(self):
#         mini = MiniProgram()
#         mini.start()
#         time.sleep(3)
#         mini.current_page()
#         time.sleep(3)
#         # 点击公告
#         elements = self.page.get_elements(
#             '//*[@id="nav-item-notice"]/navigator[4]/view')
#         for element in elements:
#             element.click()
#         # 返回首页

