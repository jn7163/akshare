# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/12/17 16:55
contact: jindaxiang@163.com
desc: 获取北京市碳排放权电子交易平台-北京市碳排放权公开交易行情
https://www.bjets.com.cn/article/jyxx/
"""
import pandas as pd
import requests


def energy_carbon():
    """
    北京市碳排放权电子交易平台-北京市碳排放权公开交易行情
    https://www.bjets.com.cn/article/jyxx/
    """
    print("正在采集, 预计10秒左右完成")
    temp_df = pd.DataFrame()
    for i in range(1, 73):
        if i == 1:
            i = ""
        url = f"https://www.bjets.com.cn/article/jyxx/?{i}"
        res = requests.get(url)
        res.encoding = "utf-8"
        df = pd.read_html(res.text)[0]
        temp_df = temp_df.append(df, ignore_index=True)
    return temp_df


if __name__ == '__main__':
    energy_carbon_df = energy_carbon()
    print(energy_carbon_df)
