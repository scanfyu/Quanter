import numpy as np

def test_run():
    a = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    print("Original array a:\n", a)

    # 将 a 乘以 2
    # print("\nMultiply a by 2:\n", 2 * a)

    # 将 a 乘以 2
    # print("\nDivide a by 2:\n", a / 2)

    b = np.array([(100,200,300,400,500), (1,2,3,4,5)])
    print("\nOriginal array b:\n", b)

    # 将两个数组加总
    # print("\nAdd a + b:\n", a + b)

    # a 除 b
    print("\nDivide a by b:\n", a / b)

if __name__ == '__main__':
    test_run()