#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:2021/8/4 6:22
# Description:

import yaml

# yaml.safe_dump()

with open("./datas/data.yaml", mode="r", encoding='utf-8') as f:
    print(yaml.safe_load(f))

dic1 = {'name': 'hogwt', 'age': '20', 'gender': 'male'}
with open("./datas/data2.yaml", mode='w', encoding='utf-8') as f:
    data2 = yaml.safe_dump(dic1, f)
