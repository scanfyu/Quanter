# numpy到底多块
import numpy as np
from time import time

def how_long(func, *args):
    # 用给定数据执行程序，测量执行时间
    t0 = time()
    result = func(*args) # all arguments are passed in as-is
    t1 = time()
    return result, t1-t0


def manual_mean(arr):
    # 在二维数组中计算所有的平均值
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size

def numpy_mean(arr):
    # 使用 Numpy 计算平均值
    return arr.mean()

def test_run():
    nd1 = np.random.random((1000, 10000)) # 使用足够大的数据

    # 计算两个功能，返回结果及运行时间
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:.6f} ({:.3f} secs.) vs. Numpy: {:.6f} ({:.3F} secs.)".format(res_manual, t_manual, res_numpy, t_numpy))

    # 保证给的是同样答案
    assert abs(res_manual - res_numpy) <= 10e-6, "Result aren't equal!"

    # 计算 speedup
    speedup = t_manual / t_numpy
    print("Numpy mean is", speedup, "times faster than manual for loops.")



if __name__ == '__main__':
    test_run()
