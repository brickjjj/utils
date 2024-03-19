# -*- coding: utf-8 -*-
# email_sender.py

import datetime
import logging

from wxpusher import WxPusher


def send_wxpusher_message(token, topic_ids, uids, content):
    try:
        result = WxPusher.send_message(content, uids=uids, topic_ids=topic_ids, token=token)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        logging.info(f"{timestamp}微信推送发送成功, {content}")
    except Exception as e:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        logging.info(f"{timestamp}微信推送发送失败: {str(e)}")


if __name__ == '__main__':
    subject = "测试微信推送"
    content = "这是一封测试微信推送的内容"

    # wxpusher 配置
    # 微信扫码下面的二维码，就可以获得通知。
    # https://wxpusher.zjiecode.com/api/qrcode/wyJzTMPwcg6UqF3EKpppDnnp9vHE5o6upkifSvH8NHjVbRFJJsupUZOjclp6NPfK.jpg
    token = 'AT_a5eGRaso7u1VR1yBva1tZ0hzPJJICoeJ'
    topic_ids = ['10164']
    # uids = ['UID_RQmppaCCZnVtLBAycFMt3054NGax']
    uids = None

    send_wxpusher_message(token,topic_ids,uids,content)