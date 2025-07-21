#coding:utf-8
from ftplib import FTP,error_perm
import time
import os
import requests
import json
import random
import shutil
from queue import Queue
import threading


# ssl._create_default_https_context = ssl._create_unverified_context
# # 创建目录文件夹
# os.makedirs('./image/', exist_ok=True)
# # 构造请求头
# headers={
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
# }


def request_download(img_url, img_name, proxy):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer':'https://www.dongmanmanhua.cn/',
    }
    r = requests.get(img_url, proxies=proxy, headers=headers)
    with open('./image/' + img_name, 'wb') as f:
        f.write(r.content)





def download_aws(url):
    all_text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(10):
        session_id = 'session-' + ''.join(random.sample(all_text, 15))
    country = 'US'
    proxy = {"http": "user-zone-custom-region-{country}-sessTime-30-{time_session}:password@643cfb36cf37ef59.na.ipidea.online:2333".format(
                            country=country, time_session=session_id)
                    }

    # 发送get请求图片url
    filename = url.split('?')[0].split('/')[-1]
    # print(filename)
    request_download(url, filename, proxy)

def worker():
    while True:
        url = url_queue.get()
        download_aws(url)
        url_queue.task_done()

if __name__ == '__main__':
    url_queue = Queue()
    with open('img.txt', 'r') as f:
        for line in f:
            url_queue.put(line.strip())
        print(url_queue.qsize())



    for i in range(5):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # 等待队列完成
    url_queue.join()
