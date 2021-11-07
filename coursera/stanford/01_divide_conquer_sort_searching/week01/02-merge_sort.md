### Merge Sort

---

- `divide & conquer` => break into smaller problems, resolve them recursevely and combine the results to get a solution to the original problem.

```
array = [5,4,1,8,7,2,6,3] # assume distinct numbers - no ties
arr1  = [5,4,1,8]
arr2  = [7,2,6,3]
|
| recursive calls until
V
arr1  = [1,4,5,8]
arr2  = [2,3,6,7]
|
| merge to
V
sortd = [1,2,3,4,5,6,7,8]
```

- pseudocode

```
0 - base case: array is either len 0 || 1
1 - recursevely sort 1st half of input array
2 - recursevely sort 2nd half of input array
3 - merge 2 sorted sublists into one

# merge pseudocode
A = 1st sorted array    => Array(n/2)
i = index of A          => 0            [+1 operation]
B = 2nd sorted array    => Array(n/2)
j = index of B          => 0            [+1 operation]
C = output array        => Array(n)

for k in range(n):                      [+1 operation]
    if A[i] < B[j]:                     [+1 operation]
        C[k] = A[i]                     [+1 operation]
        i++                             [+1 operation]
    else:
        C[k] = B[j]
        j++
```

- `Running Time` => [# operations]

  - merging:
    - upshot: `<= 4m + 2`
      - 4 operations per loop
      - 2 initialization operations
    - and since `m >= 1` then `<= 6m`
  - Total
    - `(6n).[log2(n)] + 6n`

- Analysis

  - recursion tree:

    ```
    root                            O (n)
                            ______/ \______
                            /               \
    level 1          (n/2) O                 O (n/2)
                        / \               / \
    level 2        (n/4) O   O (n/4) (n/4) O   O (n/4)
                        ...               ...
    level j: # of subproblems (O) => 2^j, each of size [n/(2^j)]

    level log2(n) O O O O .................... O O O O
    ```

  - Total of operations at `level j`:
    - not counting the recursions themselves
    - analysis on merge: `~ <= 6m`
    ```
    <= 2^j x 6.(n/2^j)
    # cancelling 2^j...
    <= 6.(n)
    ```
    - therefore it does `not depend on level j`
    - TOTAL: `<= 6.(n).[log2(n) + 1]`
