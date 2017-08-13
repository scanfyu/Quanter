
import numpy as np

def test_run():

    """
    # 获得索引值
    a = np.random.rand(5)
    print(a)

    # 使用一列索引值以获取数值
    indices = np.array([1,1,2,3])
    print(a[indices])
    """

    # 获取数值
    a = np.array([(20,25,10,23,26,32,10,5,9),(0,2,50,20,0,1,28,5,0)])
    print(a)

    # 计算平均值
    mean = a.mean()
    print(mean)

    # masking
    # print(a[a<mean])
    # 替换小于均值的数值为均值
    a[a<mean] = mean
    print(a)

if __name__ == '__main__':
    test_run()