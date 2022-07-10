# Algorithms and Data Structures in Python

## Data Structures

![Data Sructures](./images/ds_01.png)
![Data Sructures](./images/ds_02.png)
![Data Sructures](./images/ds_03.png)
![Data Sructures](./images/ds_04.png)
![Data Sructures](./images/ds_05.png)
![Data Sructures](./images/ds_06.png)

### Arrays/Lists

![Arrays](./images/array_01.png)
![Arrays](./images/array_02.png)
![Arrays](./images/array_03.png)
![Arrays](./images/array_04.png)
![Arrays](./images/array_05.png)
![Arrays](./images/array_06.png)
![Arrays](./images/array_07.png)

#### Array Operations

![Array Operations](./images/array_ops_01.png)
![Array Operations](./images/array_ops_02.png)
![Array Operations](./images/array_ops_03.png)
![Array Operations](./images/array_ops_04.png)
![Array Operations](./images/array_ops_05.png)
![Array Operations](./images/array_ops_06.png)
![Array Operations](./images/array_ops_07.png)
![Array Operations](./images/array_ops_08.png)

#### Arrays in Python

![Array in Python](./images/array_python_01.png)
![Array in Python](./images/array_python_02.png)

##### Questions

- Invert integer

```python
num = 123
reverse = 0

while num > 0:
    num, rem = divmod(num, 10)      # 12, 3 | 1, 2  | 0, 1
    reverse = reverse * 10 + rem    # 3     | 32    | 321

return reverse
```

- Dutch National Flag (sort 3 set of 3 values)
  - manage 3 partitions:
    - pivot (middle)
    - left `l`
    - right `r`
  - create 3 pointers, `left`, `right` and `current`
  - if value[current] < pivot:
    - swap value[left] with value[current]
    - left++
    - current++
  - elif value[current] > pivot:
    - swap value[right] with value[current]
    - right--
  - else:
    - current++

```python
# suppose only [0,1,2] available in the nums array
def dutch_national_flag(nums: list[int], pivot: num = 1) -> list[int]:
    left = current = 0
    right = len(nums) - 1
    while current <= right:
        if nums[current] < pivot:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] > pivot:
            nums[current], nums[right] = nums[right], nums[current]
            right -=1
        else:
            current += 1

    return nums
```

- Trapping Rain Water

  - We need at least 3 bars to trap water
  - There's no water being trapped in the boundary bars
    ![Trapping Rain Water](./images/trapping_rain_water_01.png)
    ![Trapping Rain Water](./images/trapping_rain_water_02.png)
    ![Trapping Rain Water](./images/trapping_rain_water_03.png)
    ![Trapping Rain Water](./images/trapping_rain_water_04.png)

    ```python
    def trapping_rain_water(heights):
        # if there's no 3 heights then it's impossible to trap water
        if len(heigths) < 3:
            return 0

        # generate initial dynamic arrays
        left_max = [0] * len(heights)
        right_max = [*left_max]

        # populate dynamic arrays
        for idx in range(len(heights)):
            # if idx == 0 then the max to the left is itself
            # else it's the max between itself and the last max
            left_max[idx] = height[idx] if idx == 0 else max(left_max[idx], left_max[idx - 1])

            # if idx == len(heigth) - 1 then the max to the right is itself
            # else it's the max between itself and the last max
            right_max[idx] = height[idx] if idx == len(heights) -1 else max(right_max[idx], right_max[idx + 1])

        # initialize stock
        trapped = 0

        # borders do not trap water [1:-1]!
        for idx, h in enumerate(heights[1:-1]):
            # for each idx, the result is the min between left and right max minus the current height
            # if this result is negative then the local result is 0
            trapped += max(0, min(left_max[idx], right_max[idx]) - h)

        return trapped

    ```
