#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import time
import datetime


def datetime_strftime(fmt="%Y%m"):
    """datetime格式化时间"""
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


if __name__ == '__main__':
    print(datetime_strftime())