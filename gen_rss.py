#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-

import datetime
import PyRSS2Gen
import json

file_path = "./rss.xml"

code_url = "https://git.zeekling.cn/"


def gen_rss(items):
    items_rss = []
    rss = PyRSS2Gen.RSS2(
        title="private code feed",
        link=code_url,
        description="private code feed",
        lastBuildDate=datetime.datetime.now(),
        items=items_rss
    )
    rss.write_xml(file_path, 'w')


if __name__ == "__main__":
    # main
    print('begin')
