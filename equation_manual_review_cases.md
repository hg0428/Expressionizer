# Equation Path Manual Review Cases

## Case 1 (equation, beginner)

- Problem: $-2 + -9x = -3 + -8x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 1}`

## Step 1
Solve the equation: $$-2 + -9x = -3 + -8x$$

## Step 2
Move all terms to one side: $$ 1 + -1x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{-1}{-1} $$

## Step 4
Therefore, $$ x = 1 $$

---

## Case 2 (rational_equation, intermediate)

- Problem: $\frac{-14 + 10x}{x} = 6$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 3.5}`

## Step 1
Solve the equation: $$\frac{-14 + 10x}{x} = 6$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ -14 + 4x = 0 $$

## Step 5
Solve the linear equation: $$ x = 3.5 $$

## Step 6
Valid solution after domain check: $$ x = 3.5 $$

---

## Case 3 (system, advanced)

- Problem: $\left\{\begin{array}{l}-23x + 23y = 23 \\ -20x + -20y = -980\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 24, 'y': 25}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}-23x + 23y = 23 \\ -20x + -20y = -980\end{array}\right.$$

## Step 2
Normalize row 1 by dividing by $-23$.

## Step 3
Eliminate column 1 in row 2 using factor $-20$.

## Step 4
Normalize row 2 by dividing by $-40$.

## Step 5
Eliminate column 2 in row 1 using factor $-1$.

## Step 6
Unique solution found: $$ x = 24, y = 25 $$

---

## Case 4 (equation, beginner)

- Problem: $1 + 4x = 5 + 8x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -1}`

## Step 1
Solve the equation: $$1 + 4x = 5 + 8x$$

## Step 2
Move all terms to one side: $$ -4 + -4x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{4}{-4} $$

## Step 4
Therefore, $$ x = -1 $$

---

## Case 5 (quadratic_equation, intermediate)

- Problem: $-1(-10 + x)(7 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-7, 10]}`

## Step 1
Solve the equation: $$-1(-10 + x)(7 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ 70 + -1x^2 + 3x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 289$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-7, 10\} $$

---

## Case 6 (equation, advanced)

- Problem: $26 + 6x = -27 + -20x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -2.03846153846154}`

## Step 1
Solve the equation: $$26 + 6x = -27 + -20x$$

## Step 2
Move all terms to one side: $$ 53 + 26x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{-53}{26} $$

## Step 4
Therefore, $$ x = -2.03846153846154 $$

---

## Case 7 (quadratic_equation, beginner)

- Problem: $-5(1 + x)(2 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-2, -1]}`

## Step 1
Solve the equation: $$-5(1 + x)(2 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ -10 + -5x^2 + -15x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 25$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-2, -1\} $$

---

## Case 8 (rational_equation, intermediate)

- Problem: $\frac{10 + -4x}{x} = -10$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -1.66666666666667}`

## Step 1
Solve the equation: $$\frac{10 + -4x}{x} = -10$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ 10 + 6x = 0 $$

## Step 5
Solve the linear equation: $$ x = -1.66666666666667 $$

## Step 6
Valid solution after domain check: $$ x = -1.66666666666667 $$

---

## Case 9 (rational_equation, advanced)

- Problem: $\frac{15 + 19x}{x} = 13$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -2.5}`

## Step 1
Solve the equation: $$\frac{15 + 19x}{x} = 13$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ 15 + 6x = 0 $$

## Step 5
Solve the linear equation: $$ x = -2.5 $$

## Step 6
Valid solution after domain check: $$ x = -2.5 $$

---

## Case 10 (equation, beginner)

- Problem: $3 + 2x = 5 + 7x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -0.4}`

## Step 1
Solve the equation: $$3 + 2x = 5 + 7x$$

## Step 2
Move all terms to one side: $$ -2 + -5x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{2}{-5} $$

## Step 4
Therefore, $$ x = -0.4 $$

---

## Case 11 (quadratic_equation, intermediate)

- Problem: $12(8 + x)x = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-8, 0]}`

## Step 1
Solve the equation: $$12(8 + x)x = 0$$

## Step 2
Rearrange into quadratic form: $$ 12x^2 + 96x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 9216$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-8, 0\} $$

---

## Case 12 (quadratic_equation, advanced)

- Problem: $-27(-20 + x)(-14 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [14, 20]}`

## Step 1
Solve the equation: $$-27(-20 + x)(-14 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ -7560 + -27x^2 + 918x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 26244$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{14, 20\} $$

---

## Case 13 (system, beginner)

- Problem: $\left\{\begin{array}{l}8x + 2y = -66 \\ 9x + -9y = -108\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -9, 'y': 3}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}8x + 2y = -66 \\ 9x + -9y = -108\end{array}\right.$$

## Step 2
Swap row 1 with row 2.

## Step 3
Normalize row 1 by dividing by $9$.

## Step 4
Eliminate column 1 in row 2 using factor $8$.

## Step 5
Normalize row 2 by dividing by $10$.

## Step 6
Eliminate column 2 in row 1 using factor $-1$.

## Step 7
Unique solution found: $$ x = -9, y = 3 $$

---

## Case 14 (rational_equation, intermediate)

- Problem: $\frac{11 + -9x}{x} = 2$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 1}`

## Step 1
Solve the equation: $$\frac{11 + -9x}{x} = 2$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ 11 + -11x = 0 $$

## Step 5
Solve the linear equation: $$ x = 1 $$

## Step 6
Valid solution after domain check: $$ x = 1 $$

---

## Case 15 (quadratic_equation, advanced)

- Problem: $-17(-23 + x)(-26 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [23, 26]}`

## Step 1
Solve the equation: $$-17(-23 + x)(-26 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ -10166 + -17x^2 + 833x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 2601$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{23, 26\} $$

---

## Case 16 (equation, beginner)

- Problem: $1 + -6x = 1 + 4x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 0}`

## Step 1
Solve the equation: $$1 + -6x = 1 + 4x$$

## Step 2
Move all terms to one side: $$ -10x = 0 $$

## Step 3
Isolate $x$: $$ x = 0 $$

## Step 4
Therefore, $$ x = 0 $$

---

## Case 17 (system, intermediate)

- Problem: $\left\{\begin{array}{l}4x + 5y = -39 \\ -11x + 13y = -187\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 4, 'y': -11}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}4x + 5y = -39 \\ -11x + 13y = -187\end{array}\right.$$

## Step 2
Swap row 1 with row 2.

## Step 3
Normalize row 1 by dividing by $-11$.

## Step 4
Eliminate column 1 in row 2 using factor $4$.

## Step 5
Normalize row 2 by dividing by $\frac{107}{11}$.

## Step 6
Eliminate column 2 in row 1 using factor $-\frac{13}{11}$.

## Step 7
Unique solution found: $$ x = 4, y = -11 $$

---

## Case 18 (system, advanced)

- Problem: $\left\{\begin{array}{l}19x + -21y + 19z = 67 \\ -21x + 14y + 7z = 329 \\ 9x + -2y + -21z = -427\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 0, 'y': 14, 'z': 19}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}19x + -21y + 19z = 67 \\ -21x + 14y + 7z = 329 \\ 9x + -2y + -21z = -427\end{array}\right.$$

## Step 2
Swap row 1 with row 2.

## Step 3
Normalize row 1 by dividing by $-21$.

## Step 4
Eliminate column 1 in row 2 using factor $19$.

## Step 5
Eliminate column 1 in row 3 using factor $9$.

## Step 6
Normalize row 2 by dividing by $-\frac{25}{3}$.

## Step 7
Eliminate column 2 in row 1 using factor $-\frac{2}{3}$.

## Step 8
Eliminate column 2 in row 3 using factor $4$.

## Step 9
Normalize row 3 by dividing by $-\frac{146}{25}$.

## Step 10
Eliminate column 3 in row 1 using factor $-\frac{59}{25}$.

## Step 11
Eliminate column 3 in row 2 using factor $-\frac{76}{25}$.

## Step 12
Unique solution found: $$ x = 0, y = 14, z = 19 $$

---

## Case 19 (rational_equation, beginner)

- Problem: $\frac{5 + 7x}{x} = -1$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -0.625}`

## Step 1
Solve the equation: $$\frac{5 + 7x}{x} = -1$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ 5 + 8x = 0 $$

## Step 5
Solve the linear equation: $$ x = -0.625 $$

## Step 6
Valid solution after domain check: $$ x = -0.625 $$

---

## Case 20 (quadratic_equation, intermediate)

- Problem: $9(-2 + x)(4 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-4, 2]}`

## Step 1
Solve the equation: $$9(-2 + x)(4 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ -72 + 9x^2 + 18x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 2916$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-4, 2\} $$

---

## Case 21 (quadratic_equation, advanced)

- Problem: $-6(-5 + x)(14 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-14, 5]}`

## Step 1
Solve the equation: $$-6(-5 + x)(14 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ 420 + -6x^2 + -54x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 12996$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-14, 5\} $$

---

## Case 22 (quadratic_equation, beginner)

- Problem: $(3 + x)(4 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-4, -3]}`

## Step 1
Solve the equation: $$(3 + x)(4 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ 12 + x^2 + 7x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 1$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-4, -3\} $$

---

## Case 23 (system, intermediate)

- Problem: $\left\{\begin{array}{l}3x + 3y = -30 \\ -5y = 5\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -9, 'y': -1}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}3x + 3y = -30 \\ -5y = 5\end{array}\right.$$

## Step 2
Normalize row 1 by dividing by $3$.

## Step 3
Normalize row 2 by dividing by $-5$.

## Step 4
Eliminate column 2 in row 1 using factor $1$.

## Step 5
Unique solution found: $$ x = -9, y = -1 $$

---

## Case 24 (equation, advanced)

- Problem: $3 + -28x = -9 + -27x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 12}`

## Step 1
Solve the equation: $$3 + -28x = -9 + -27x$$

## Step 2
Move all terms to one side: $$ 12 + -1x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{-12}{-1} $$

## Step 4
Therefore, $$ x = 12 $$

---

## Case 25 (equation, beginner)

- Problem: $-1 + -5x = -6 + -8x$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -1.66666666666667}`

## Step 1
Solve the equation: $$-1 + -5x = -6 + -8x$$

## Step 2
Move all terms to one side: $$ 5 + 3x = 0 $$

## Step 3
Isolate $x$: $$ x = \frac{-5}{3} $$

## Step 4
Therefore, $$ x = -1.66666666666667 $$

---

## Case 26 (rational_equation, intermediate)

- Problem: $\frac{-13 + -8x}{x} = -13$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 2.6}`

## Step 1
Solve the equation: $$\frac{-13 + -8x}{x} = -13$$

## Step 2
Domain restriction: $x \neq 0$ because it appears in a denominator.

## Step 3
Multiply both sides by $x$ to clear the denominator.

## Step 4
After clearing denominators: $$ -13 + 5x = 0 $$

## Step 5
Solve the linear equation: $$ x = 2.6 $$

## Step 6
Valid solution after domain check: $$ x = 2.6 $$

---

## Case 27 (quadratic_equation, advanced)

- Problem: $-15(-23 + x)(-26 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [23, 26]}`

## Step 1
Solve the equation: $$-15(-23 + x)(-26 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ -8970 + -15x^2 + 735x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 2025$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{23, 26\} $$

---

## Case 28 (system, beginner)

- Problem: $\left\{\begin{array}{l}7x + -2y = 70 \\ 5x = 40\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': 8, 'y': -7}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}7x + -2y = 70 \\ 5x = 40\end{array}\right.$$

## Step 2
Normalize row 1 by dividing by $7$.

## Step 3
Eliminate column 1 in row 2 using factor $5$.

## Step 4
Normalize row 2 by dividing by $\frac{10}{7}$.

## Step 5
Eliminate column 2 in row 1 using factor $-\frac{2}{7}$.

## Step 6
Unique solution found: $$ x = 8, y = -7 $$

---

## Case 29 (system, intermediate)

- Problem: $\left\{\begin{array}{l}-1x + 7y = 67 \\ -3x + -8y = -60\end{array}\right.$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': -4, 'y': 9}`

## Step 1
Solve the system:
$$\left\{\begin{array}{l}-1x + 7y = 67 \\ -3x + -8y = -60\end{array}\right.$$

## Step 2
Swap row 1 with row 2.

## Step 3
Normalize row 1 by dividing by $-3$.

## Step 4
Eliminate column 1 in row 2 using factor $-1$.

## Step 5
Normalize row 2 by dividing by $\frac{29}{3}$.

## Step 6
Eliminate column 2 in row 1 using factor $\frac{8}{3}$.

## Step 7
Unique solution found: $$ x = -4, y = 9 $$

---

## Case 30 (quadratic_equation, advanced)

- Problem: $15(22 + x)(6 + x) = 0$
- Solve status: `exact` | reason_code: `-` | sympy: `equivalent`
- Values: `{'x': [-22, -6]}`

## Step 1
Solve the equation: $$15(22 + x)(6 + x) = 0$$

## Step 2
Rearrange into quadratic form: $$ 1980 + 15x^2 + 420x = 0 $$

## Step 3
Compute the discriminant: $$\Delta = b^2 - 4ac = 57600$$

## Step 4
Apply the quadratic formula: $$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

## Step 5
Therefore, $$ x \in \{-22, -6\} $$

---
