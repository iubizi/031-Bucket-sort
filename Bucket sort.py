def bucket_sort(arr, bucket_num=5): # 默认五桶

    arr_min = min(arr)
    arr_max = max(arr)

    # bucket_num = len(arr) # 空间换时间

    bucket_size = (arr_max - arr_min + 1) // bucket_num

    bucket = [ [] for _ in range(bucket_num) ] # 2D方便

    for i in arr: # 分桶
        index = (i - arr_min) // bucket_size
        bucket[index].append(i)

    for i in bucket: # 桶内排序，使用快排或者归并
        i.sort() # 稳定排序方法

    ans = [] # 输出
    for i in bucket: # 拆掉数组合并在一起
        ans.extend(i)

    return ans
        


if __name__ == '__main__':

    arr = list(range(50))

    import random
    random.shuffle(arr)

    print(arr)
    print()
    print(bucket_sort(arr))
