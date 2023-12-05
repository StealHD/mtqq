# from setuptools import setup, find_packages
#
# setup(
#     name='your_project',
#     version='1.0',
#     packages=find_packages(),
#     install_requires=[
#         # 列出项目的依赖项
#     ],
# )


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import threading
import time

def task1():
    for _ in range(5):
        print("Task 1 is running")
        time.sleep(1)

def task2():
    for _ in range(5):
        print("Task 2 is running")
        time.sleep(1)

# 创建两个线程，分别执行 task1 和 task2
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# 启动线程
thread1.start()
thread2.start()

# 等待两个线程执行完毕
thread1.join()
thread2.join()

print("All tasks are completed.")


# 调用函数并传递URL



