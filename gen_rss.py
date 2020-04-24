#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-

import datetime
import PyRSS2Gen
import json
import requests

file_path = "./rss.xml"

code_url = "https://git.zeekling.cn/"

resp_url = code_url + "api/v1/repos/search"

update_days = 15

params = {
    'sort': 'updated',
    'order': 'desc',
    'limit': 50
}


def gen_rss(items):
    items_rss = []
    for item in items:
        rss_item = PyRSS2Gen.RSSItem(
            title=item['full_name'],
            link=item['url'],
            description=item['des'],
            guid=PyRSS2Gen.Guid(item['url']),
            pubDate=item['update_time']
        )
        items_rss.append(rss_item)
    rss = PyRSS2Gen.RSS2(
        title="private code feed",
        link=code_url,
        description="private code feed",
        lastBuildDate=datetime.datetime.now(),
        items=items_rss
    )
    rss.write_xml(open(file_path, 'w', encoding='utf-8'), encoding='utf-8')


def get_items():
    items = []
    page = 1
    now_time = datetime.datetime.now()
    while True:
        params['page'] = page
        pages = requests.get(resp_url, params=params)
        tmp = json.loads(pages.text)
        data = tmp['data']
        if len(data) == 0:
            break
        use_able_count = 1
        for resp in data:
            update_time = datetime.datetime.strptime(resp['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%SZ')
            end_date = update_time + datetime.timedelta(days=update_days)
            if now_time >= end_date:
                continue
            use_able_count += 1
            entity = {
                'name': resp['name'],
                'url': resp['html_url'],
                'update_time': update_time,
                'full_name': resp['full_name'],
                'des': resp['description']
            }
            items.append(entity)
        page = page + 1
        if use_able_count == 1:
            break
    return items


if __name__ == "__main__":
    # main
    print('begin')
    items = get_items()
    gen_rss(items)
