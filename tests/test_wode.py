# -*- coding: utf-8 -*-
import time
import allure
from minium import MiniProgram, Callback
import minium


@allure.suite('路路游小程序')
@allure.feature('我的')
@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class TestWode_01(minium.MiniTest):

    def test_wode(self):
        mini = MiniProgram()
        mini.start()
        time.sleep(3)
        mini.current_page()

        # 我的
        elements = self.page.get_elements(
            '/page/view/biz-tab-bar/view/view/view/view/view[5]')
        for element in elements:
            element.click()
        time.sleep(3)
        # 查看个人信息
        elements = self.page.get_elements(
            '/page/view/biz-tab-bar/view/view/view/view/view[2]')
        for element in elements:
            element.click()
        time.sleep(3)
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 查看卡包
        elements = self.page.get_elements(
            '/page/view/view[1]/view[2]/view/button')
        for element in elements:
            element.click()
        # 点击卡片绑定
        elements = self.page.get_elements(
            '/page/view/button')
        for element in elements:
            element.click()
        # 输入卡密(卡片激活码)
        elements = self.page.get_elements(
            '/page/view/view[2]/view[1]/input')
        for element in elements:
            element.send_keys('123456789')
        # 输入姓名
        elements = self.page.get_elements(
            '/page/view/view[2]/view[2]/input')
        for element in elements:
            element.send_keys('张民')
        # 输入手机号
        elements = self.page.get_elements(
            '/page/view/view[2]/view[3]/input')
        for element in elements:
            element.send_keys('15970710891')
        # 输入身份证号
        elements = self.page.get_elements(
            '/page/view/view[2]/view[4]/input')
        for element in elements:
            element.send_keys('110105197001137135')
        # 勾选协议
        elements = self.page.get_elements(
            '/page/view/view[3]/checkbox-group/label/checkbox')
        for element in elements:
            element.click()
        # # 点击查看协议内容
        # elements = self.page.get_elements(
        #     '/page/view/view[3]/navigator')
        # for element in elements:
        #     element.click()

        # 点击“点我购卡”
        elements = self.page.get_elements(
            '/page/view/view[4]/navigator')
        for element in elements:
            element.click()
        # 返回至卡片激活页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 确认绑定
        elements = self.page.get_elements(
            '/page/view/view[2]/button')
        for element in elements:
            element.click()
        # 确认弹窗中点击确认绑定
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[3]/button[2]')
        for element in elements:
            element.click()
        # 绑定成功后关闭弹窗
        elements = self.page.get_elements(
            '/page/view/ml-popup-modal/uni-popup/view/view/uni-transition[2]/view/view/view[1]/view[1]/text')
        for element in elements:
            element.click()
        # 页面返回至我的卡包
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 页面返回至我的
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 我的预约
        elements = self.page.get_elements(
            '/page/view/view[1]/view[3]/view[1]')
        for element in elements:
            element.click()
        # 我的预约查看可使用
        elements = self.page.get_elements(
            '/page/view/view/view[2]')
        for element in elements:
            element.click()
        # 点击入园码
        elements = self.page.get_elements(
            '/page/view/swiper/swiper-item[2]/scroll-view/view[1]/view[1]/view[2]/view[4]/button')
        for element in elements:
            element.click()
        # 返回至我的预约页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # TAB栏切至已失效页面
        elements = self.page.get_elements(
            '/page/view/view/view[3]')
        for element in elements:
            element.click()
        # 查看已逾期订单
        elements = self.page.get_elements(
            '/page/view/swiper/swiper-item[3]/scroll-view/view[1]/view[1]/view[2]/view[2]')
        for element in elements:
            element.click()
        # 返回至我的预约页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # TAB栏切至已核销页面
        elements = self.page.get_elements(
            '/page/view/view/view[4]')
        for element in elements:
            element.click()
        # 查看已核销订单
        elements = self.page.get_elements(
            '/page/view/swiper/swiper-item[3]/scroll-view/view[1]/view[1]/view[2]/view[2]')
        for element in elements:
            element.click()
        # 返回至我的预约页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 页面返回至我的
        elements = self.page.get_elements(
            '/page/view/view/view[3]')
        for element in elements:
            element.click()
        # 查看年卡订单
        elements = self.page.get_elements(
            '/page/view/view[1]/view[3]/view[2]')
        for element in elements:
            element.click()
        # 点击再来一单
        elements = self.page.get_elements(
            '/page/view/scroll-view/view[1]/view[2]/view[3]/view[2]/view')
        for element in elements:
            element.click()
        # 从购卡页面返回至年卡订单页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 查看待支付信息
        elements = self.page.get_elements(
            '/page/view/view/view/view[2]')
        for element in elements:
            element.click()
        # 查看已支付信息
        elements = self.page.get_elements(
            '/page/view/view/view/view[3]')
        for element in elements:
            element.click()
        # 查看已取消信息
        elements = self.page.get_elements(
            '/page/view/view/view/view[4]')
        for element in elements:
            element.click()
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 点击景区订单
        elements = self.page.get_elements(
            '/page/view/view[1]/view[3]/view[3]')
        for element in elements:
            element.click()
        # 查看订单详情
        elements = self.page.get_elements(
            '/page/view/swiper/swiper-item[1]/scroll-view/view[1]/view[1]')
        for element in elements:
            element.click()
        # 返回至景区订单页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 查看待支付订单信息
        elements = self.page.get_elements(
            '/page/view/view/view[2]')
        for element in elements:
            element.click()
        # 查看已支付订单信息
        elements = self.page.get_elements(
            '/page/view/view/view[3]')
        for element in elements:
            element.click()
        # 查看退款订单信息
        elements = self.page.get_elements(
            '/page/view/view/view[4]')
        for element in elements:
            element.click()
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # # 点击查看我的权益包
        # elements = self.page.get_elements(
        #     '/page/view/view[1]/view[3]/view[4]')
        # for element in elements:
        #     element.click()
        # # 查看未选取权益包信息
        # elements = self.page.get_elements(
        #     '/page/view/view[1]/view[2]')
        # for element in elements:
        #     element.click()
        # # 查看未使用权益包信息
        # elements = self.page.get_elements(
        #     '/page/view/view[1]/view[3]')
        # for element in elements:
        #     element.click()
        # # 查看已使用权益包信息
        # elements = self.page.get_elements(
        #     '/page/view/view[1]/view[4]')
        # for element in elements:
        #     element.click()
        # # 返回至我的页面
        # elements = self.page.get_elements(
        #     '')
        # for element in elements:
        #     element.click()
        # 查看我的激活码
        elements = self.page.get_elements(
            '/page/view/view[2]/navigator[2]')
        for element in elements:
            element.click()
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 查看出行人
        elements = self.page.get_elements(
            '/page/view/view[2]/navigator[3]')
        for element in elements:
            element.click()
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 查看消息通知
        elements = self.page.get_elements(
            '/page/view/view[2]/navigator[7]')
        for element in elements:
            element.click()
        # 查看通知详情
        elements = self.page.get_elements(
            '/page/view/scroll-view/view[1]')
        for element in elements:
            element.click()
        # 返回页面至消息通知
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()
        # 返回至我的页面
        elements = self.page.get_elements(
            '/page/view/ml-title/view/view/view/view[1]/text')
        for element in elements:
            element.click()


