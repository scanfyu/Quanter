# 寻找最大值
import numpy as np

def get_max_index(a):
    """返回1维数组最大值的索引"""
    return a.argmax()


def test_run():
    a = np.array([9,6,2,3,12,14,7,10],dtype=np.int32) # 32位数组
    print("Array:", a)

    # 找到最大值及其索引
    print("Maximum value:", a.max())
    print("Index of max.:", get_max_index(a))


if __name__ == '__main__':
    test_run()
