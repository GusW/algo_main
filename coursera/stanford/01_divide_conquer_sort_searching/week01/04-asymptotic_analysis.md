### Asymptotic Analysis

---

- `high level idea` => suppress constant factors and lower-order terms.

  - `6.(n).[log2(n)] + 6n` -> `n.log(n)`
  - `Big-Oh of n.log(n)`

  ```
  T(n) = function on positive n=1,2,3,...
  question: when is T(n) = Big-Oh(f(n))?
  assumption: T(n) is bounded above by a constant multiple of f(n)
  thus: if and only if there exist constants c, n0 > 0 such that
        T(n) <= c.(f(n)) for all n >= n0
        c, n0 cannot depend on n
  ```

- `Omega` notation (bigger or equals to)

  ```
  T(n) = Big-Omega(f(n))
  if and only if exists constants c, n0 such that
  T(n) >= c.f(n), for every n >= n0
  ```

- `Theta` notation (equals to)

  - T(n) = Big-Oh(f(n)) `&&` T(n) = Big-Omega(f(n))

  ```
  exists c1 < c2, n0 such that
  c1.f(n) <= T(n) <= c2.f(n) for all n >= n0
  ```

- `Little-Oh`
  ```
  T(n) = Little-Oh(f(n))
  if and only if for all constants c > 0
  there is a constant n0 such that
  T(n) <= c.f(n) for every n >= n0
  ```

```
T(n) = 1/2.(n^2) + 3.(n)

T(n) = Big-Omega of n   proof with [n0 = 1, c = 1/2]
T(n) = Big-Theta of n^2 proof with [n0 = 1, c1 = 1/2, c2 = 4]
T(n) = Big-Oh    of n^3 proof with [n0 = 1, c = 4]
```

- Examples

  - Big-Oh

    ```
    claim: 2^(n+10) = O(2^n)
    proof: find constants c, n0 such that
    (*) 2^(n+10) <= c.(2^n), for every n >= n0
    2^(n+10) = (2^n)*(2^10) = 1024.(2^n)
    if: c = 1024
        n0 = 1
    then: 2^(1+10) <= 1024.(2^1)
    Q.E.D! quod erat demonstrandum
    ```

    ```
    claim: 2^10n is not O(2^n)
    proof: by contradiction
           if 2^10n = O(2^n)
           then exists c, n0 > 0 such that
           2^10n <= c.(2^n), for every n >= n0
    cancelling 2^n:
          2^9n <= c, for every n >= n0
    then: right hand side is a fixed constant independent than n
          left hand side goes to infinity as n goes large
          false. Q.E.D!
    ```

    ```

    ```
