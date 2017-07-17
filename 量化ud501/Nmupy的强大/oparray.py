# 行列式计算
import numpy as np

def test_run():

    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5*4 random integers in [0, 10)
    print("Array:\n", a)

    # 按行迭代，计算每列总和
    print("Sum of each column:\n", a.sum(axis=0))

    # 按列迭代，计算每行总和
    print("Sum of each row:\n", a.sum(axis=1))

    # 统计最小值，最大值，平均值（通过行、列以及总和）
    print("Minimum of each column:\n", a.min(axis=0)) # 列最小值
    print("Maximum of each row:\n", a.max(axis=1)) # 行最大值
    print("Mean of all elements", a.mean()) # 不设置方向


if __name__ == '__main__':
    test_run()