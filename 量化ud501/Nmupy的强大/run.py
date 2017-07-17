import numpy as np
import time

"""
# 使用时间模块计算运算时间
def test_run():
    t1 = time.time()
    print("ML4T")
    t2 = time.time()
    print("The time taken by print statement is", t2-t1,"seconds")
"""

# 赋值与取值
def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # 通过指定位置获取值
    a[0, 0] = 1
    print("\nModified (replaced one element):\n", a)

    # 将某值赋予一整行
    a[0, :] = 2
    print("\nModified (replaced a row with a single value):\n", a)

    # 将一个列表赋值给一列
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\nModified (replaced a column with a list):\n", a)

if __name__ == '__main__':
    test_run()