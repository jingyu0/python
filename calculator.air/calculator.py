# -*- encoding=utf8 -*-
__author__ = "sunjingyu14"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()

poco('com.google.android.calculator:id/digit_1').click()
poco('com.google.android.calculator:id/op_add').click()
poco('com.google.android.calculator:id/digit_1').click()
poco('com.google.android.calculator:id/eq').click()

result = poco('com.google.android.calculator:id/formula').get_text()
self.assertEqual(result, '2', '1+1=2 ^^')
