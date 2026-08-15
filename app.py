#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""启海号 QIHAI · 本地预览入口

双击运行或 `python app.py`: 启动本地静态服务器并自动打开展示页面。
纯 Python 标准库实现, 无需安装任何依赖。
"""
import functools
import http.server
import os
import threading
import webbrowser

PORT = 8791
ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = f"http://127.0.0.1:{PORT}/web/index.html"


def main():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    try:
        server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    except OSError:
        # 端口被占用多半是预览服务器已在运行, 直接打开页面即可
        print(f"端口 {PORT} 已被占用, 直接打开 {PAGE}")
        webbrowser.open(PAGE)
        return
    print("启海号 QIHAI · 邮轮目的地化展示")
    print(f"预览地址: {PAGE}   (Ctrl+C 停止)")
    threading.Timer(0.8, lambda: webbrowser.open(PAGE)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
        server.server_close()


if __name__ == "__main__":
    main()
