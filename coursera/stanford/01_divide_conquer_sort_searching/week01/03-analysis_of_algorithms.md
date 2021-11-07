### Analysis of Algorithms

---

- `"worst-case" analysis`

  - general purpose routines
  - others requires domain knowledge:
    - "average case" analysis
    - benchmarks

- `constants factors` and `lower-order terms` are secondary

  - easier to keep track
  - dependant on architecture/compiler/programmer
  - little predictive power

- `asymptotic analysis`

  - focus on running time for assumed large input size

  ```
  6n.(log2(n)) + 6n "better than" 1/2.(n^2)
  ```

  - only big problems are interesting and challenging

- `fast` algorithm:
  - worst-case running rime grows slowly with input size
  - `sweet spot`: mathematical tractability and predictive power
