### The grade school integer multiplication algorithm

---

```
    5678    (x) -> n.x = 4
  x 1234    (y) -> n.y = 4
    ----
   22712    max operations <= 2(n.x): multiplication && carried additions
  17034-    |
 11356--    |
 5678---    | n.y rows
 -------
 7006652

```

- hence the number of operations overall <= `constant.(n.x).(n.y)` ~ `const.(n^2)`

---

### The karatsuba multiplication algorithm

---

```
    5678    (x) -> n.x = 4
  x 1234    (y) -> n.y = 4
    ----
    a = 56
    b = 78
    c = 12
    d = 34
    ------
    1: (a).(c) = 672
    2: (b).(d) = 2652
    3: (a+b).(c+d) = (134).(46) = 6164
    4: 3 - 2 - 1 = 2840
    5: 1 + four zeros => 6720000
       2              =>    2652
       3 + two zeros  =>  284000
                         -------
                         7006652
```

- recursive approach

```
if:
    x = [10^(n/2)].(a) +b
    y = [10^(n/2)].(c) +d
    # ex.: a = 56, b=78, c=12, d=34
then:
    (x).(y) = {[10^(n/2)].(a)+b}.{[10^(n/2)].(c)+d}
            = 10^n.(ac) + 10^(n/2).(ad + bc) + bd
but:
    1 -> recursevely compute (a).(c)
    2 -> recursevely compute (b).(d)
    3 -> recursevely compute (a+b).(c+d) = ac + ad + bc + bd
    4 -> Gauss trick: 3 - 2 - 1 = ac + ad + bc + bd - ac - bd = ad + bc
thus:
    only 3 recursive multiplications
```
