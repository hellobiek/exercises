def get_circles(val, arrs):
    circles = [val]
    while True:
        if val != arrs[val] and arrs[val] not in circles:
            circles.append(arrs[val])
            val = arrs[val]
        else:
            break
    return circles


def compute_min_times(arrs):
    visited_nums = []
    min_times = 0
    for val in arrs:
        if val not in visited_nums:
            circles = get_circles(val, arrs)
            visited_nums.extend(circles)
            if len(circles) > 1:
                if 0 not in circles:
                    min_times = min_times + len(circles) + 1
                else:
                    min_times += len(circles) - 1
    else:
        return min_times


if __name__ == '__main__':
    arrs = [0, 1, 3, 5, 6, 8, 9, 7, 2, 4]
    print(compute_min_times(arrs))
