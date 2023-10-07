def mean_median(input_array):
    try:
        mean = sum(input_array) / len(input_array)
        sorted_arr = sorted(input_array)
        n = len(sorted_arr)
        if n % 2 == 0:
            median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
        else:
            median = sorted_arr[n // 2]
        return mean, median
    except ZeroDivisionError:
        return None 

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)
print(mean_median([]))