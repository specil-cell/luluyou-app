# -*- coding: utf-8 -*-
import minium

class ComponentTest(minium.MiniTest):
    def __init__(self, mini):
        super().__init__()
        self.mini = mini

    def click_elements(self, xpath):
        elements = self.page.get_elements(selector=xpath)
        for element in elements:
            element.click()

    def input_elements(self, xpath, input_text):
        elements = self.page.get_elements(selector=xpath)
        for element in elements:
            if element.tag_name == 'input' and 'value' in element.get_attribute('attributes'):
                element.clear()
                element.send_keys(input_text)