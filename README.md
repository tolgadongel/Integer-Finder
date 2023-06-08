# Integer-Finder

A simple python code to find all integers `n` for which the expression `(an+b)/(cn-d)` is an integer.

## How to Use

1. Run the code and provide the values of `a`, `b`, `c`, and `d` when prompted.
2. The code will iterate through a range of possible values for `n`.
3. For each value of `n`, it will check if the expression is an integer.
4. If the expression is an integer, the corresponding value of `n` will be added to the result list.
5. Once all values of `n` have been checked, the code will return the resulting list of integers.
6. The resulting integers will be printed to the console.

## Example

Let's say we want to find integers `n` for the expression `(17n+9)/(4n-5)`.

Running the code and entering `a = 17`, `b = 19`, `c = 4`, and `d = -5`, we will get the following result:
[-39, 1, 3, 7]


This means that for the given expression, the integers `-39` , `1`, `3` and `7` satisfy the condition.


## Note
I'm not particularly happy with using `range`, but since it gets the job done, I didn't dwell on it too much. I will try to implement some bounds based on the given values to improve it in the future.


## License
This project is licensed under the [MIT License](LICENSE).


