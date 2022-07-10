def trapping_rain_water(heights):
    if len(heights) < 3:
        return 0

    # create 2 dynamic arrays with the max values seen so far for both left and right
    left_max = [heights[idx] if idx == 0 else 0 for idx in range(len(heights))]
    right_max = [
        heights[idx] if idx == len(heights) - 1 else 0 for idx in range(len(heights))
    ]

    # no water can be trapped in the boundaries
    left = 1
    right = len(heights) - 2

    # init stock
    trapped = 0

    # calculate and persit max left and right, per idx
    while left < len(heights):
        curr_left = heights[left]
        left_max[left] = max(left_max[left - 1], curr_left)

        curr_right = heights[right]
        right_max[right] = max(right_max[right + 1], curr_right)

        left += 1
        right -= 1

    for idx, h in enumerate(heights):
        trapped += max(0, min(left_max[idx], right_max[idx]) - h)

    return trapped


print(trapping_rain_water([2, 1, 3, 1, 4]))  # 3
print(trapping_rain_water([4, 1, 3, 1, 5]))  # 7
print(trapping_rain_water([1, 0, 2, 1, 3, 1, 2, 0, 3]))  # 8
