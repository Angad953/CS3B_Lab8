def rotate(nums, k):
    n = len(nums)
    k = k % n
    if k != 0:
        return nums[-k:] + nums[:-k]
    return nums


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    new_arr = rotate(arr, 3)
    print(new_arr)


if __name__ == '__main__':
    main()
