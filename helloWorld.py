import numpy as np


def say_hello():
    print("Hello World!\nHope you're doing well!")
    return


def print_arr_backwards(arr):
    if isinstance(arr, np.ndarray):
        print(arr[::-1])
    else:
        print('You didn\'t give me a numpy array you goof!')
    return



def main():

    say_hello()

    a = np.arange(5)
    print_arr_backwards(a)

    return



if __name__=="__main__":
    main()
