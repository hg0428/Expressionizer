# Manual Verification Cases

Use this file to manually review generated problems, answers, and step-by-step explanations.

## Case 1 (seed=17000, difficulty=beginner, guarantee_solvable=True)

- Problem: $\frac{d^{2}}{dp^{2}}3 + 6p^4$
- Answer: $25447.68$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Differentiate with respect to $p$ (order 2) using the applicable differentiation rules.

Compute $18.8 \cdot 18.8$ by place-value decomposition: form partial products, then add them.
Rewrite $18.8$ as an integer-scaled value times $10^{-1}$.

**Partial-product table:**
|                  | $1 \cdot 10^{2}$ | $8 \cdot 10^{1}$  | $8 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- | ----------------- |
| $1 \cdot 10^{2}$ | $1 \cdot 10^{4}$ | $8 \cdot 10^{3}$  | $8 \cdot 10^{2}$  |
| $8 \cdot 10^{1}$ | $8 \cdot 10^{3}$ | $64 \cdot 10^{2}$ | $64 \cdot 10^{1}$ |
| $8 \cdot 10^{0}$ | $8 \cdot 10^{2}$ | $64 \cdot 10^{1}$ | $64 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
10000
08000
08000
00800
06400
00800
00640
00640
00064
```
$10^{0}$: $4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{1}$: $6 + 4 + 4 + 0 + 0 + 0 + 0 + 0 + 0 = 14$, so carry 1 to the next column.
$10^{2}$: $0 + 6 + 6 + 8 + 4 + 8 + 0 + 0 + 0 + 1 = 33$, so carry 3 to the next column.
$10^{3}$: $0 + 0 + 0 + 0 + 6 + 0 + 8 + 8 + 0 + 3 = 25$, so carry 2 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 2 = 3$
Combine the place-value columns to obtain $35344$.
Compute $353.44 \cdot 72$ by place-value decomposition: form partial products, then add them.
Rewrite $353.44$ as an integer-scaled value times $10^{-2}$.

**Partial-product table:**
|                  | $3 \cdot 10^{4}$  | $5 \cdot 10^{3}$  | $3 \cdot 10^{2}$  | $4 \cdot 10^{1}$  | $4 \cdot 10^{0}$  |
| ---------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $7 \cdot 10^{1}$ | $21 \cdot 10^{5}$ | $35 \cdot 10^{4}$ | $21 \cdot 10^{3}$ | $28 \cdot 10^{2}$ | $28 \cdot 10^{1}$ |
| $2 \cdot 10^{0}$ | $6 \cdot 10^{4}$  | $1 \cdot 10^{4}$  | $6 \cdot 10^{2}$  | $8 \cdot 10^{1}$  | $8 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
2100000
0350000
0060000
0021000
0010000
0002800
0000600
0000280
0000080
0000008
```
$10^{0}$: $8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{1}$: $0 + 8 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 16$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 2 + 6 + 8 + 0 + 0 + 0 + 0 + 0 + 1 = 17$, so carry 1 to the next column.
$10^{3}$: $0 + 0 + 0 + 0 + 2 + 0 + 1 + 0 + 0 + 0 + 1 = 4$
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 1 + 2 + 6 + 5 + 0 = 14$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 1 + 1 = 5$
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 = 2$
Combine the place-value columns to obtain $2544768$.

---

## Case 2 (seed=17001, difficulty=intermediate, guarantee_solvable=False)

- Problem: $2 + 4 + \frac{d}{dx}4.57$
- Answer: $6$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ 2 + 4 + \frac{d}{dx}4.57 \\
= 2 + 4 + \frac{d}{dx}4.57 \\
= 6 + \frac{d}{dx}4.57 $$

## Step 2
Differentiate with respect to $x$ using the applicable differentiation rules.

## Step 3
$$ 6 + 0 \\
= 6 $$



---

## Case 3 (seed=17002, difficulty=advanced, guarantee_solvable=True)

- Problem: $b + 17.5$
- Answer: $5.5$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $b = -12$.
$$ b + 17.5 \\
= b + 17.5 \\
= -12 + 17.5 $$

Decompose $-12$ and $17.5$ into place-value components.
$$ b + 17.5 \\
= -12 + 17.5 \\
= -10 - 2 + 10 + 7 + 0.5 $$

```
-10.0
-02.0
 10.0
 07.0
 00.5
```
$10^{-1}$: $5 + 0 + 0 + 0 + 0 = 5$
$10^{0}$: $0 + 7 + 0 - 2 + 0 = 5$
Combine the place-value columns to obtain $5.5$.
$$ -10 - 2 + 10 + 7 + 0.5 \\
= 5.5 $$


---

## Case 4 (seed=17003, difficulty=beginner, guarantee_solvable=False)

- Problem: $10(-20)31(13.6)$
- Answer: $-84320$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ 10(-20)31(13.6) \\
= 10(-20)31(13.6) \\
= -200(31(13.6)) $$

Compute $31 \cdot 13.6$ by place-value decomposition: form partial products, then add them.
Rewrite $13.6$ as an integer-scaled value times $10^{-1}$.
## Step 2
$$ -200(31(13.6)) \\
= \frac{-843200}{10} \\
= \frac{-200(30 + 1)(100 + 30 + 6)}{10} $$


**Partial-product table:**
|                  | $3 \cdot 10^{1}$  | $1 \cdot 10^{0}$ |
| ---------------- | ----------------- | ---------------- |
| $1 \cdot 10^{2}$ | $3 \cdot 10^{3}$  | $1 \cdot 10^{2}$ |
| $3 \cdot 10^{1}$ | $9 \cdot 10^{2}$  | $3 \cdot 10^{1}$ |
| $6 \cdot 10^{0}$ | $18 \cdot 10^{1}$ | $6 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
3000
0100
0900
0030
0180
0006
```
$10^{0}$: $6 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{1}$: $0 + 8 + 3 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{2}$: $0 + 1 + 0 + 9 + 1 + 0 + 1 = 12$, so carry 1 to the next column.
$10^{3}$: $0 + 0 + 0 + 0 + 0 + 3 + 1 = 4$
Combine the place-value columns to obtain $4216$.
## Step 3
$$ \frac{-200(3000 + 100 + 900 + 30 + 180 + 6)}{10} \\
= \frac{-843200}{10} \\
= 421.6(200)(-1) $$

Compute $421.6 \cdot -200$ by place-value decomposition: form partial products, then add them.
Rewrite $421.6$ as an integer-scaled value times $10^{-1}$.
Rewrite $-200$ as an integer-scaled value times $10^{2}$.
## Step 4
$$ 421.6(200)(-1) \\
= 4216(-2)(10^1) \\
= (4000 + 200 + 10 + 6)(-2)10^1 $$


**Partial-product table:**
|                   | $4 \cdot 10^{3}$  | $2 \cdot 10^{2}$  | $1 \cdot 10^{1}$  | $6 \cdot 10^{0}$   |
| ----------------- | ----------------- | ----------------- | ----------------- | ------------------ |
| $-2 \cdot 10^{0}$ | $-8 \cdot 10^{3}$ | $-4 \cdot 10^{2}$ | $-2 \cdot 10^{1}$ | $-12 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-8000
-0400
-0020
-0012
```
$10^{0}$: $-2 + 0 + 0 + 0 = -2$, so borrow 1 from the next column and write 8 here.
$10^{1}$: $-1 - 2 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{2}$: $0 + 0 - 4 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{3}$: $0 + 0 + 0 - 8 - 1 = -9$, so borrow 1 from the next column and write 1 here.
Combine the place-value columns to obtain $-8432$.
## Step 5
$$ (-8000 - 400 - 20 - 12)10^1 \\
= -8432(10^1) \\
= -84320 $$

$$ -8432(10^1) \\
= -84320 $$



---

## Case 5 (seed=17004, difficulty=intermediate, guarantee_solvable=True)

- Problem: $26 - 22 + 4.4 + (28.22 + 6)(-30.5a(-26)(0.39))$
- Answer: $116424.84$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
Substitute the given values: $a = 11$.
$$ 26 - 22 + 4.4 + (28.22 + 6)(-30.5a(-26)(0.39)) \\
= 26 - 22 + 4.4 + (28.22 + 6)(-30.5a(-26)(0.39)) \\
= 26 - 22 + 4.4 + (28.22 + 6)(-30.5(11)(-26)(0.39)) \\
= 4 + 4.4 + (28.22 + 6)(-30.5(11)(-26)(0.39)) $$

## Step 2
$$ 26 - 22 + 4.4 + (28.22 + 6)(-30.5(11)(-26)(0.39)) \\
= 4 + 4.4 + (28.22 + 6)(-30.5(11)(-26)(0.39)) \\
= 8.4 + (28.22 + 6)(-30.5(11)(-26)(0.39)) $$

Decompose $28.22$ and $6$ into place-value components.
## Step 3
```
20.00
08.00
00.20
00.02
06.00
```
$10^{-2}$: $0 + 2 + 0 + 0 + 0 = 2$
$10^{-1}$: $0 + 0 + 2 + 0 + 0 = 2$
$10^{0}$: $6 + 0 + 0 + 8 + 0 = 14$, so carry 1 to the next column.
$10^{1}$: $0 + 0 + 0 + 0 + 2 + 1 = 3$
Combine the place-value columns to obtain $34.22$.
Compute $11 \cdot 0.39$ by place-value decomposition: form partial products, then add them.
Rewrite $0.39$ as an integer-scaled value times $10^{-2}$.
## Step 4
$$ 8.4 + 34.22(-30.5(11)(-26)(0.39)) \\
= 8.4 + \frac{11641541.34}{10^2} \\
= 8.4 + \frac{27136.46(10 + 1)(30 + 9)}{10^2} $$


**Partial-product table:**
|                  | $1 \cdot 10^{1}$ | $1 \cdot 10^{0}$ |
| ---------------- | ---------------- | ---------------- |
| $3 \cdot 10^{1}$ | $3 \cdot 10^{2}$ | $3 \cdot 10^{1}$ |
| $9 \cdot 10^{0}$ | $9 \cdot 10^{1}$ | $9 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
300
030
090
009
```
$10^{0}$: $9 + 0 + 0 + 0 = 9$
$10^{1}$: $0 + 9 + 3 + 0 = 12$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 0 + 3 + 1 = 4$
Combine the place-value columns to obtain $429$.
## Step 5
$$ 8.4 + \frac{27136.46(300 + 30 + 90 + 9)}{10^2} \\
= 8.4 + \frac{11641541.34}{10^2} \\
= 8.4 + 4.29(34.22)(30.5)(26) $$

Compute $4.29 \cdot -26$ by place-value decomposition: form partial products, then add them.
Rewrite $4.29$ as an integer-scaled value times $10^{-2}$.
## Step 6
$$ 8.4 + 4.29(34.22)(30.5)(26) \\
= 8.4 + \frac{11641541.34}{10^2} \\
= 8.4 + \frac{-1043.71(400 + 20 + 9)(-20 - 6)}{10^2} $$


**Partial-product table:**
|                   | $4 \cdot 10^{2}$   | $2 \cdot 10^{1}$   | $9 \cdot 10^{0}$   |
| ----------------- | ------------------ | ------------------ | ------------------ |
| $-2 \cdot 10^{1}$ | $-8 \cdot 10^{3}$  | $-4 \cdot 10^{2}$  | $-18 \cdot 10^{1}$ |
| $-6 \cdot 10^{0}$ | $-24 \cdot 10^{2}$ | $-12 \cdot 10^{1}$ | $-54 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-8000
-0400
-2400
-0180
-0120
-0054
```
$10^{0}$: $-4 + 0 + 0 + 0 + 0 + 0 = -4$, so borrow 1 from the next column and write 6 here.
$10^{1}$: $-5 - 2 - 8 + 0 + 0 + 0 - 1 = -16$, so borrow 2 from the next column and write 4 here.
$10^{2}$: $0 - 1 - 1 - 4 - 4 + 0 - 2 = -12$, so borrow 2 from the next column and write 8 here.
$10^{3}$: $0 + 0 + 0 - 2 + 0 - 8 - 2 = -12$, so borrow 2 from the next column and write 8 here.
Combine the place-value columns to obtain $-11154$.
## Step 7
$$ 8.4 + \frac{-1043.71(-8000 - 400 - 2400 - 180 - 120 - 54)}{10^2} \\
= 8.4 - \frac{-11641541.34}{10^2} \\
= 8.4 - -116415.4134 $$

Compute $-111.54 \cdot -30.5$ by place-value decomposition: form partial products, then add them.
Rewrite $-111.54$ as an integer-scaled value times $10^{-2}$.
Rewrite $-30.5$ as an integer-scaled value times $10^{-1}$.
## Step 8
$$ 8.4 - -116415.4134 \\
= 8.4 - \frac{-116415413.4}{10^3} \\
= 8.4 + \frac{34.22(-10000 - 1000 - 100 - 50 - 4)(-300 - 5)}{10^3} $$


**Partial-product table:**
|                   | $-1 \cdot 10^{4}$ | $-1 \cdot 10^{3}$ | $-1 \cdot 10^{2}$ | $-5 \cdot 10^{1}$ | $-4 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $-3 \cdot 10^{2}$ | $3 \cdot 10^{6}$  | $3 \cdot 10^{5}$  | $3 \cdot 10^{4}$  | $15 \cdot 10^{3}$ | $12 \cdot 10^{2}$ |
| $-5 \cdot 10^{0}$ | $5 \cdot 10^{4}$  | $5 \cdot 10^{3}$  | $5 \cdot 10^{2}$  | $25 \cdot 10^{1}$ | $2 \cdot 10^{1}$  |
**Add these partial values by place value:**
```
3000000
0300000
0050000
0030000
0005000
0015000
0000500
0001200
0000250
0000020
```
$10^{1}$: $2 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{2}$: $0 + 2 + 2 + 5 + 0 + 0 + 0 + 0 + 0 + 0 = 9$
$10^{3}$: $0 + 0 + 1 + 0 + 5 + 5 + 0 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 1 + 0 + 3 + 5 + 0 + 0 + 1 = 10$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 0 + 1 = 4$
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 = 3$
Combine the place-value columns to obtain $3401970$.
## Step 9
$$ 8.4 + \frac{34.22(3000000 + 300000 + 50000 + 30000 + 5000 + 15000 + 500 + 1200 + 250 + 20)}{10^3} \\
= 8.4 + \frac{116415413.4}{10^3} \\
= 8.4 + 3401.97(34.22) $$

Compute $3401.9700000000003 \cdot 34.22$ by place-value decomposition: form partial products, then add them.
Approximate $3401.9700000000003$ as $3402.0$ to control intermediate precision during multiplication.

Rewrite $34.22$ as an integer-scaled value times $10^{-2}$.
## Step 10
$$ 8.4 + 3402(34.22) \\
= 8.4 + \frac{11641644}{10^2} \\
= 8.4 + \frac{(3000 + 400 + 2)(3000 + 400 + 20 + 2)}{10^2} $$


**Partial-product table:**
|                  | $3 \cdot 10^{3}$  | $4 \cdot 10^{2}$  | $2 \cdot 10^{0}$ |
| ---------------- | ----------------- | ----------------- | ---------------- |
| $3 \cdot 10^{3}$ | $9 \cdot 10^{6}$  | $12 \cdot 10^{5}$ | $6 \cdot 10^{3}$ |
| $4 \cdot 10^{2}$ | $12 \cdot 10^{5}$ | $16 \cdot 10^{4}$ | $8 \cdot 10^{2}$ |
| $2 \cdot 10^{1}$ | $6 \cdot 10^{4}$  | $8 \cdot 10^{3}$  | $4 \cdot 10^{1}$ |
| $2 \cdot 10^{0}$ | $6 \cdot 10^{3}$  | $8 \cdot 10^{2}$  | $4 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
9000000
1200000
1200000
0006000
0160000
0060000
0000800
0008000
0006000
0000040
0000800
0000004
```
$10^{0}$: $4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{1}$: $0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{2}$: $0 + 8 + 0 + 0 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 = 16$, so carry 1 to the next column.
$10^{3}$: $0 + 0 + 0 + 6 + 8 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 1 = 21$, so carry 2 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 6 + 6 + 0 + 0 + 0 + 0 + 2 = 14$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 2 + 2 + 0 + 1 = 6$
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 1 + 9 = 11$, so carry 1 to the next column.
$10^{7}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $11641644$.
## Step 11
$$ 8.4 + \frac{9000000 + 1200000 + 1200000 + 6000 + 160000 + 60000 + 800 + 8000 + 6000 + 40 + 800 + 4}{10^2} \\
= 8.4 + \frac{11641644}{10^2} \\
= 8.4 + 116416.44 $$

Decompose $8.4$ and $116416.44$ into place-value components.
## Step 12
```
000008.00
000000.40
100000.00
010000.00
006000.00
000400.00
000010.00
000006.00
000000.40
000000.04
```
$10^{-2}$: $4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-1}$: $0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 = 8$
$10^{0}$: $0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 8 = 14$, so carry 1 to the next column.
$10^{1}$: $0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 2$
$10^{2}$: $0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{3}$: $0 + 0 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 0 = 6$
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 = 1$
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 = 1$
Combine the place-value columns to obtain $116424.84$.
$$ 8 + 0.4 + 100000 + 10000 + 6000 + 400 + 10 + 6 + 0.4 + 0.04 \\
= 116424.84 $$



---

## Case 6 (seed=17005, difficulty=advanced, guarantee_solvable=False)

- Problem: $15.2 + -49.6 + 15$
- Answer: $-19.4$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Decompose $-49.6$ and $15$ into place-value components.
$$ 15.2 + -49.6 + 15 \\
= 15.2 + -49.6 + 15 \\
= -40 - 9 - 0.6 + 10 + 5 + 15.2 $$

```
-40.0
-09.0
-00.6
 10.0
 05.0
```
$10^{-1}$: $0 + 0 - 6 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{0}$: $5 + 0 + 0 - 9 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{1}$: $0 + 1 + 0 + 0 - 4 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-34.599999999999994$.
Decompose $15.2$ and $-34.599999999999994$ into place-value components.
## Step 2
```
 10.0
 05.0
 00.2
-30.0
-04.0
-00.6
```
$10^{-1}$: $-6 + 0 + 0 + 2 + 0 + 0 = -4$, so borrow 1 from the next column and write 6 here.
$10^{1}$: $0 + 0 - 3 + 0 + 0 + 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $-19.400000000000006$.
$$ 10 + 5 + 0.2 - 30 - 4 - 0.6 \\
= -19.4 $$



---

## Case 7 (seed=17006, difficulty=beginner, guarantee_solvable=True)

- Problem: $5.2(8(11))$
- Answer: $457.6$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ 5.2(8(11)) \\
= 5.2(8(11)) \\
= 88(5.2) $$

Compute $88 \cdot 5.2$ by place-value decomposition: form partial products, then add them.
Rewrite $5.2$ as an integer-scaled value times $10^{-1}$.
## Step 2
$$ 88(5.2) \\
= \frac{4576}{10} \\
= \frac{(80 + 8)(50 + 2)}{10} $$


**Partial-product table:**
|                  | $8 \cdot 10^{1}$  | $8 \cdot 10^{0}$  |
| ---------------- | ----------------- | ----------------- |
| $5 \cdot 10^{1}$ | $4 \cdot 10^{3}$  | $4 \cdot 10^{2}$  |
| $2 \cdot 10^{0}$ | $16 \cdot 10^{1}$ | $16 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
4000
0400
0160
0016
```
$10^{0}$: $6 + 0 + 0 + 0 = 6$
$10^{1}$: $1 + 6 + 0 + 0 = 7$
$10^{2}$: $0 + 1 + 4 + 0 = 5$
$10^{3}$: $0 + 0 + 0 + 4 = 4$
Combine the place-value columns to obtain $4576$.
## Step 3
$$ \frac{4000 + 400 + 160 + 16}{10} \\
= \frac{4576}{10} \\
= 457.6 $$

$$ \frac{4576}{10} \\
= 457.6 $$



---

## Case 8 (seed=17007, difficulty=intermediate, guarantee_solvable=False)

- Problem: $27.8^{λ}$
- Answer: $6.07257458 \times 10^{-21}$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $λ = -14$.
$$ 27.8^{λ} \\
= 27.8^{λ} \\
= \frac{1}{27.8^14} \\
= 0.00000000000000000000607257457821796 $$


---

## Case 9 (seed=17008, difficulty=advanced, guarantee_solvable=True)

- Problem: $6 + 36.6(-22(-9 + q + 38))$
- Answer: $-38643.6$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $q = 19$.
$$ 6 + 36.6(-22(-9 + q + 38)) \\
= 6 + 36.6(-22(-9 + q + 38)) \\
= 6 + 36.6(-22(-9 + 19 + 38)) \\
= 6 + 36.6(-22(10 + 38)) $$

## Step 2
$$ 6 + 36.6(-22(-9 + 19 + 38)) \\
= 6 + 36.6(-22(10 + 38)) \\
= 6 + 36.6(-22(48)) $$

Compute $48 \cdot -22$ by place-value decomposition: form partial products, then add them.
## Step 3

**Partial-product table:**
|                   | $4 \cdot 10^{1}$  | $8 \cdot 10^{0}$   |
| ----------------- | ----------------- | ------------------ |
| $-2 \cdot 10^{1}$ | $-8 \cdot 10^{2}$ | $-16 \cdot 10^{1}$ |
| $-2 \cdot 10^{0}$ | $-8 \cdot 10^{1}$ | $-16 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-800
-160
-080
-016
```
$10^{0}$: $-6 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{1}$: $-1 - 8 - 6 + 0 - 1 = -16$, so borrow 2 from the next column and write 4 here.
$10^{2}$: $0 + 0 - 1 - 8 - 2 = -11$, so borrow 2 from the next column and write 9 here.
Combine the place-value columns to obtain $-1056$.
Compute $36.6 \cdot -1056$ by place-value decomposition: form partial products, then add them.
Rewrite $36.6$ as an integer-scaled value times $10^{-1}$.
## Step 4
$$ 6 - 38649.6 \\
= 6 + \frac{-386496}{10} \\
= 6 + \frac{(300 + 60 + 6)(-1000 - 50 - 6)}{10} $$


**Partial-product table:**
|                   | $3 \cdot 10^{2}$   | $6 \cdot 10^{1}$   | $6 \cdot 10^{0}$   |
| ----------------- | ------------------ | ------------------ | ------------------ |
| $-1 \cdot 10^{3}$ | $-3 \cdot 10^{5}$  | $-6 \cdot 10^{4}$  | $-6 \cdot 10^{3}$  |
| $-5 \cdot 10^{1}$ | $-15 \cdot 10^{3}$ | $-3 \cdot 10^{3}$  | $-3 \cdot 10^{2}$  |
| $-6 \cdot 10^{0}$ | $-18 \cdot 10^{2}$ | $-36 \cdot 10^{1}$ | $-36 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-300000
-060000
-015000
-006000
-003000
-001800
-000300
-000360
-000036
```
$10^{0}$: $-6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{1}$: $-3 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{2}$: $0 - 3 - 3 - 8 + 0 + 0 + 0 + 0 + 0 - 1 = -15$, so borrow 2 from the next column and write 5 here.
$10^{3}$: $0 + 0 + 0 - 1 - 3 - 6 - 5 + 0 + 0 - 2 = -17$, so borrow 2 from the next column and write 3 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 - 1 - 6 + 0 - 2 = -9$, so borrow 1 from the next column and write 1 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-386496$.
## Step 5
$$ 6 + \frac{-300000 - 60000 - 15000 - 6000 - 3000 - 1800 - 300 - 360 - 36}{10} \\
= 6 - \frac{386496}{10} \\
= 6 - 38649.6 $$

Decompose $6$ and $-38649.6$ into place-value components.
## Step 6
```
 00006.0
-30000.0
-08000.0
-00600.0
-00040.0
-00009.0
-00000.6
```
$10^{-1}$: $-6 + 0 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{0}$: $0 - 9 + 0 + 0 + 0 + 0 + 6 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{1}$: $0 + 0 - 4 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{2}$: $0 + 0 + 0 - 6 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{3}$: $0 + 0 + 0 + 0 - 8 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 3 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-38643.6$.
$$ 6 - 30000 - 8000 - 600 - 40 - 9 - 0.6 \\
= -38643.6 $$



---

## Case 10 (seed=17009, difficulty=beginner, guarantee_solvable=False)

- Problem: $17 + 11$
- Answer: $28$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

$$ 17 + 11 \\
= 17 + 11 \\
= 28 $$


---

## Case 11 (seed=17010, difficulty=intermediate, guarantee_solvable=True)

- Problem: $\frac{d^{2}}{dρ^{2}}8ρ^2$
- Answer: $16$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Differentiate with respect to $ρ$ (order 2) using the applicable differentiation rules.

$$ \frac{d^{2}}{dρ^{2}}8ρ^2 $$


---

## Case 12 (seed=17011, difficulty=advanced, guarantee_solvable=False)

- Problem: $2 + \int_{-27.5}^{13} \cos{32.6} \, dλ$
- Answer: $17.2748514381417$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
Apply the Fundamental Theorem of Calculus: evaluate the antiderivative at the bounds and subtract, $F(13) - F(-27.5)$.

Compute $13 \cdot 0.377155325023334$ by place-value decomposition: form partial products, then add them.
Approximate $0.377155325023334$ as $0.37716000000000005$ to control intermediate precision during multiplication.

Rewrite $0.37716000000000005$ as an integer-scaled value times $10^{-5}$.
## Step 2
$$ 2 + 10.3717714381417 + 0.37716(13) \\
= 2 + 10.3717714381417 + \frac{490308}{10^5} \\
= 2 + 10.3717714381417 + \frac{(10 + 3)(30000 + 7000 + 700 + 10 + 6)}{10^5} $$


**Partial-product table:**
|                  | $1 \cdot 10^{1}$ | $3 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- |
| $3 \cdot 10^{4}$ | $3 \cdot 10^{5}$ | $9 \cdot 10^{4}$  |
| $7 \cdot 10^{3}$ | $7 \cdot 10^{4}$ | $21 \cdot 10^{3}$ |
| $7 \cdot 10^{2}$ | $7 \cdot 10^{3}$ | $21 \cdot 10^{2}$ |
| $1 \cdot 10^{1}$ | $1 \cdot 10^{2}$ | $3 \cdot 10^{1}$  |
| $6 \cdot 10^{0}$ | $6 \cdot 10^{1}$ | $18 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
300000
090000
070000
021000
007000
002100
000100
000030
000060
000018
```
$10^{0}$: $8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{1}$: $1 + 6 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 10$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 0 + 1 + 1 + 0 + 0 + 0 + 0 + 0 + 1 = 3$
$10^{3}$: $0 + 0 + 0 + 0 + 2 + 7 + 1 + 0 + 0 + 0 = 10$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 2 + 7 + 9 + 0 + 1 = 19$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 1 = 4$
Combine the place-value columns to obtain $490308$.
## Step 3
$$ 2 + 10.3717714381417 + \frac{300000 + 90000 + 70000 + 21000 + 7000 + 2100 + 100 + 30 + 60 + 18}{10^5} \\
= 2 + 10.3717714381417 + \frac{490308}{10^5} \\
= 2 + 10.3717714381417 + 4.90308 $$

Decompose $10.3717714381417$ and $4.90308$ into place-value components.
## Step 4
```
10.0000000000000
00.3000000000000
00.0700000000000
00.0010000000000
00.0007000000000
00.0000700000000
00.0000010000000
00.0000004000000
00.0000000300000
00.0000000080000
00.0000000001000
00.0000000000400
00.0000000000010
00.0000000000007
04.0000000000000
00.9000000000000
00.0030000000000
00.0000800000000
```
$10^{-13}$: $0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-12}$: $0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-11}$: $0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 3$
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-5}$: $8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 = 15$, so carry 1 to the next column.
$10^{-4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 1 = 8$
$10^{-3}$: $0 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 = 4$
$10^{-2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 = 7$
$10^{-1}$: $0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 12$, so carry 1 to the next column.
$10^{0}$: $0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 5$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 1$
Combine the place-value columns to obtain $15.2748514381417$.
Decompose $2$ and $15.2748514381417$ into place-value components.
## Step 5
```
02.0000000000000
10.0000000000000
05.0000000000000
00.2000000000000
00.0700000000000
00.0040000000000
00.0008000000000
00.0000500000000
00.0000010000000
00.0000004000000
00.0000000300000
00.0000000080000
00.0000000001000
00.0000000000400
00.0000000000010
00.0000000000007
```
$10^{-13}$: $7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-12}$: $0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-11}$: $0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-10}$: $0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-9}$: $0 + 0 + 0 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 3$
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{-4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{-3}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 = 7$
$10^{-1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 0 + 0 + 0 = 2$
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 5 + 0 + 2 = 7$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 = 1$
Combine the place-value columns to obtain $17.2748514381417$.
$$ 2 + 10 + 5 + 0.2 + 0.07 + 0.004 + 0.0008 + 0.00005 + 0.000001 + 0.0000004 + 0.00000003 + 0.000000008 + 0.0000000001 + 0.00000000004 + 0.000000000001 + 0.0000000000007 \\
= 17.2748514381417 $$



---

## Case 13 (seed=17012, difficulty=beginner, guarantee_solvable=True)

- Problem: $14y + \frac{d}{dy}6y^2$
- Answer: $338$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $y = 13$.
$$ 14y + \frac{d}{dy}6y^2 \\
= 14y + \frac{d}{dy}6y^2 \\
= 14(13) + \frac{d}{dy}6y^2 $$

Compute $14 \cdot 13$ by place-value decomposition: form partial products, then add them.
$$ 14y + \frac{d}{dy}6y^2 \\
= 14(13) + \frac{d}{dy}6y^2 \\
= (10 + 4)(10 + 3) + \frac{d}{dy}6y^2 $$


**Partial-product table:**
|                  | $1 \cdot 10^{1}$ | $4 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- |
| $1 \cdot 10^{1}$ | $1 \cdot 10^{2}$ | $4 \cdot 10^{1}$  |
| $3 \cdot 10^{0}$ | $3 \cdot 10^{1}$ | $12 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
100
040
030
012
```
$10^{0}$: $2 + 0 + 0 + 0 = 2$
$10^{1}$: $1 + 3 + 4 + 0 = 8$
$10^{2}$: $0 + 0 + 0 + 1 = 1$
Combine the place-value columns to obtain $182$.
Differentiate with respect to $y$ using the applicable differentiation rules.

Decompose $182$ and $156$ into place-value components.
```
100
080
002
100
050
006
```
$10^{0}$: $6 + 0 + 0 + 2 + 0 + 0 = 8$
$10^{1}$: $0 + 5 + 0 + 0 + 8 + 0 = 13$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 1 + 0 + 0 + 1 + 1 = 3$
Combine the place-value columns to obtain $338$.

---

## Case 14 (seed=17013, difficulty=intermediate, guarantee_solvable=False)

- Problem: $b41 + \atan2{26, 20.2(0)}$
- Answer: $493.570796326795$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $b = 12$.
$$ b41 + \atan2{26, 20.2(0)} \\
= b41 + \atan2{26, 20.2(0)} \\
= 12(41) + \atan2{26, 20.2(0)} \\
= 492 + \atan2{26, 20.2(0)} $$

## Step 2
$$ 12(41) + \atan2{26, 20.2(0)} \\
= 492 + \atan2{26, 20.2(0)} \\
= 492 + \atan2{26, 0} $$

## Step 3
$$ 492 + \atan2{26, 20.2(0)} \\
= 492 + \atan2{26, 0} \\
= 492 + 1.5707963267949 $$

Decompose $492$ and $1.5707963267948966$ into place-value components.
## Step 4
```
400.0000000000000
090.0000000000000
002.0000000000000
001.0000000000000
000.5000000000000
000.0700000000000
000.0007000000000
000.0000900000000
000.0000060000000
000.0000003000000
000.0000000200000
000.0000000060000
000.0000000007000
000.0000000000900
000.0000000000040
000.0000000000009
```
$10^{-13}$: $9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 9$
$10^{-12}$: $0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-11}$: $0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 9$
$10^{-10}$: $0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-9}$: $0 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 3$
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{-5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 9$
$10^{-4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 = 5$
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 0 = 3$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 = 9$
$10^{2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 = 4$
Combine the place-value columns to obtain $493.5707963267949$.
$$ 400 + 90 + 2 + 1 + 0.5 + 0.07 + 0.0007 + 0.00009 + 0.000006 + 0.0000003 + 0.00000002 + 0.000000006 + 0.0000000007 + 0.00000000009 + 0.000000000004 + 0.0000000000009 \\
= 493.570796326795 $$



---

## Case 15 (seed=17014, difficulty=advanced, guarantee_solvable=True)

- Problem: $0 + 36$
- Answer: $36$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

$$ 0 + 36 \\
= 0 + 36 \\
= 36 $$


---

## Case 16 (seed=17015, difficulty=beginner, guarantee_solvable=False)

- Problem: $\abs{-11.6} + 19.7$
- Answer: $31.3$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ \abs{-11.6} + 19.7 \\
= \abs{-11.6} + 19.7 \\
= 11.6 + 19.7 $$

Decompose $11.6$ and $19.7$ into place-value components.
## Step 2
```
10.0
01.0
00.6
10.0
09.0
00.7
```
$10^{-1}$: $7 + 0 + 0 + 6 + 0 + 0 = 13$, so carry 1 to the next column.
$10^{0}$: $0 + 9 + 0 + 0 + 1 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{1}$: $0 + 0 + 1 + 0 + 0 + 1 + 1 = 3$
Combine the place-value columns to obtain $31.3$.
$$ 10 + 1 + 0.6 + 10 + 9 + 0.7 \\
= 31.3 $$



---

## Case 17 (seed=17016, difficulty=intermediate, guarantee_solvable=True)

- Problem: $3 + x$
- Answer: $2$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $x = -1$.
$$ 3 + x \\
= 3 + x \\
= 3 - 1 \\
= 2 $$


---

## Case 18 (seed=17017, difficulty=advanced, guarantee_solvable=False)

- Problem: $-8 + 12(-5)$
- Answer: $-68$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ -8 + 12(-5) \\
= -8 + 12(-5) \\
= -8 - 60 $$

## Step 2
$$ -8 + 12(-5) \\
= -8 - 60 \\
= -68 $$



---

## Case 19 (seed=17018, difficulty=beginner, guarantee_solvable=True)

- Problem: $-2.8(0)(-13)z(-14)$
- Answer: $0$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $z = 1$.
$$ -2.8(0)(-13)z(-14) \\
= -2.8(0)(-13)z(-14) \\
= -2.8(0)(-13)1(-14) \\
= 0(1)(-14) \\
= 0(1)(14)(-1) $$

## Step 2
$$ 0(1)(-14) \\
= 0(1)(14)(-1) \\
= 0 $$



---

## Case 20 (seed=17019, difficulty=intermediate, guarantee_solvable=False)

- Problem: $-22(34)$
- Answer: $-748$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Compute $34 \cdot -22$ by place-value decomposition: form partial products, then add them.
$$ -22(34) \\
= -22(34) \\
= (30 + 4)(-20 - 2) $$


**Partial-product table:**
|                   | $3 \cdot 10^{1}$  | $4 \cdot 10^{0}$  |
| ----------------- | ----------------- | ----------------- |
| $-2 \cdot 10^{1}$ | $-6 \cdot 10^{2}$ | $-8 \cdot 10^{1}$ |
| $-2 \cdot 10^{0}$ | $-6 \cdot 10^{1}$ | $-8 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-600
-080
-060
-008
```
$10^{0}$: $-8 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 - 6 - 8 + 0 - 1 = -15$, so borrow 2 from the next column and write 5 here.
$10^{2}$: $0 + 0 + 0 - 6 - 2 = -8$, so borrow 1 from the next column and write 2 here.
Combine the place-value columns to obtain $-748$.
$$ -600 - 80 - 60 - 8 \\
= -748 $$


---

## Case 21 (seed=17020, difficulty=advanced, guarantee_solvable=True)

- Problem: $(23.2 + 23.1)\erfc{1}2.9(0)(32(4.02))^{32 + 14 + 23.8 + c + 7^4}c + 27.6445$
- Answer: $0^{2470.8 + c}c + 27.6445$
- Solve status: `partial` | reason_code: `zero_base_symbolic_exponent` | approximate: `False`

$$ (23.2 + 23.1)\erfc{1}2.9(0)(32(4.02))^{32 + 14 + 23.8 + c + 7^4}c + 27.6445 \\
= (23.2 + 23.1)\erfc{1}2.9(0)(32(4.02))^{32 + 14 + 23.8 + c + 7^4}c + 27.6445 \\
= 0^{32 + 14 + 23.8 + c + 7^4}c + 27.6445 $$


---

## Case 22 (seed=17021, difficulty=beginner, guarantee_solvable=False)

- Problem: $34 + τ$
- Answer: $8.1$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $τ = -25.9$.
$$ 34 + τ \\
= 34 + τ \\
= 34 - 25.9 $$

Decompose $34$ and $-25.9$ into place-value components.
$$ 34 + τ \\
= 34 - 25.9 \\
= 30 + 4 - 20 - 5 - 0.9 $$

```
 30.0
 04.0
-20.0
-05.0
-00.9
```
$10^{-1}$: $-9 + 0 + 0 + 0 + 0 = -9$, so borrow 1 from the next column and write 1 here.
$10^{0}$: $0 - 5 + 0 + 4 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $8.1$.
$$ 30 + 4 - 20 - 5 - 0.9 \\
= 8.1 $$


---

## Case 23 (seed=17022, difficulty=intermediate, guarantee_solvable=True)

- Problem: $(\int_{-52}^{18.5} 6 + 4ג_y^3 \, dג_y)\erfc{ג_y}$
- Answer: $-4.07414176 \times 10^{-289}$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
Substitute the given values: $ג_y = 26$.
$$ (\int_{-52}^{18.5} 6 + 4ג_y^3 \, dג_y)\erfc{ג_y} \\
= (\int_{-52}^{18.5} 6 + 4ג_y^3 \, dג_y)\erfc{ג_y} \\
= (\int_{-52}^{18.5} 6 + 4ג_y^3 \, dג_y)\erfc{26} $$

Apply the Fundamental Theorem of Calculus: evaluate the antiderivative at the bounds and subtract, $F(18.5) - F(-52)$.

Compute $18.5 \cdot 6$ by place-value decomposition: form partial products, then add them.
Rewrite $18.5$ as an integer-scaled value times $10^{-1}$.
$$ (6(18.5) + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (\frac{1110}{10} + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (\frac{(100 + 80 + 5)(6)}{10} + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$


**Partial-product table:**
|                  | $1 \cdot 10^{2}$ | $8 \cdot 10^{1}$  | $5 \cdot 10^{0}$ |
| ---------------- | ---------------- | ----------------- | ---------------- |
| $6 \cdot 10^{0}$ | $6 \cdot 10^{2}$ | $48 \cdot 10^{1}$ | $3 \cdot 10^{1}$ |
**Add these partial values by place value:**
```
600
480
030
```
$10^{1}$: $3 + 8 + 0 = 11$, so carry 1 to the next column.
$10^{2}$: $0 + 4 + 6 + 1 = 11$, so carry 1 to the next column.
$10^{3}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $1110$.
## Step 2
$$ (\frac{600 + 480 + 30}{10} + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (\frac{1110}{10} + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$

$$ (\frac{1110}{10} + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{4(18.5^4)}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468540.25}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$

Compute $18.5 \cdot 18.5$ by place-value decomposition: form partial products, then add them.
Rewrite $18.5$ as an integer-scaled value times $10^{-1}$.
$$ (111 + \frac{468540.25}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{46854025}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{1369(100 + 80 + 5)^2}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$


**Partial-product table:**
|                  | $1 \cdot 10^{2}$ | $8 \cdot 10^{1}$  | $5 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- | ----------------- |
| $1 \cdot 10^{2}$ | $1 \cdot 10^{4}$ | $8 \cdot 10^{3}$  | $5 \cdot 10^{2}$  |
| $8 \cdot 10^{1}$ | $8 \cdot 10^{3}$ | $64 \cdot 10^{2}$ | $4 \cdot 10^{2}$  |
| $5 \cdot 10^{0}$ | $5 \cdot 10^{2}$ | $4 \cdot 10^{2}$  | $25 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
10000
08000
08000
00500
06400
00500
00400
00400
00025
```
$10^{0}$: $5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{1}$: $2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{2}$: $0 + 4 + 4 + 5 + 4 + 5 + 0 + 0 + 0 = 22$, so carry 2 to the next column.
$10^{3}$: $0 + 0 + 0 + 0 + 6 + 0 + 8 + 8 + 0 + 2 = 24$, so carry 2 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 2 = 3$
Combine the place-value columns to obtain $34225$.
## Step 3
$$ (111 + \frac{1369(10000 + 8000 + 8000 + 500 + 6400 + 500 + 400 + 400 + 25)}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{46854025}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468540.25}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$

Compute $342.25 \cdot 18.5$ by place-value decomposition: form partial products, then add them.
Rewrite $342.25$ as an integer-scaled value times $10^{-2}$.
Rewrite $18.5$ as an integer-scaled value times $10^{-1}$.
## Step 4
$$ (111 + \frac{468540.25}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468540250}{4(10^3)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{74(30000 + 4000 + 200 + 20 + 5)(100 + 80 + 5)}{4(10^3)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$


**Partial-product table:**
|                  | $3 \cdot 10^{4}$  | $4 \cdot 10^{3}$  | $2 \cdot 10^{2}$  | $2 \cdot 10^{1}$  | $5 \cdot 10^{0}$  |
| ---------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $1 \cdot 10^{2}$ | $3 \cdot 10^{6}$  | $4 \cdot 10^{5}$  | $2 \cdot 10^{4}$  | $2 \cdot 10^{3}$  | $5 \cdot 10^{2}$  |
| $8 \cdot 10^{1}$ | $24 \cdot 10^{5}$ | $32 \cdot 10^{4}$ | $16 \cdot 10^{3}$ | $16 \cdot 10^{2}$ | $4 \cdot 10^{2}$  |
| $5 \cdot 10^{0}$ | $15 \cdot 10^{4}$ | $2 \cdot 10^{4}$  | $1 \cdot 10^{3}$  | $1 \cdot 10^{2}$  | $25 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
3000000
0400000
2400000
0020000
0320000
0150000
0002000
0016000
0020000
0000500
0001600
0001000
0000400
0000100
0000025
```
$10^{0}$: $5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{1}$: $2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{2}$: $0 + 1 + 4 + 0 + 6 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 16$, so carry 1 to the next column.
$10^{3}$: $0 + 0 + 0 + 1 + 1 + 0 + 0 + 6 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 2 + 1 + 0 + 5 + 2 + 2 + 0 + 0 + 0 + 1 = 13$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 3 + 0 + 4 + 4 + 0 + 1 = 13$, so carry 1 to the next column.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 0 + 3 + 1 = 6$
Combine the place-value columns to obtain $6331625$.
## Step 5
$$ (111 + \frac{74(3000000 + 400000 + 2400000 + 20000 + 320000 + 150000 + 2000 + 16000 + 20000 + 500 + 1600 + 1000 + 400 + 100 + 25)}{4(10^3)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468540250}{4(10^3)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468540.25}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$

Compute $6331.625 \cdot 18.5$ by place-value decomposition: form partial products, then add them.
Approximate $6331.625$ as $6331.6$ to control intermediate precision during multiplication.

Rewrite $6331.6$ as an integer-scaled value times $10^{-1}$.
Rewrite $18.5$ as an integer-scaled value times $10^{-1}$.
## Step 6
$$ (111 + \frac{468538.4}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{46853840}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{4(60000 + 3000 + 300 + 10 + 6)(100 + 80 + 5)}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$


**Partial-product table:**
|                  | $6 \cdot 10^{4}$  | $3 \cdot 10^{3}$  | $3 \cdot 10^{2}$  | $1 \cdot 10^{1}$ | $6 \cdot 10^{0}$  |
| ---------------- | ----------------- | ----------------- | ----------------- | ---------------- | ----------------- |
| $1 \cdot 10^{2}$ | $6 \cdot 10^{6}$  | $3 \cdot 10^{5}$  | $3 \cdot 10^{4}$  | $1 \cdot 10^{3}$ | $6 \cdot 10^{2}$  |
| $8 \cdot 10^{1}$ | $48 \cdot 10^{5}$ | $24 \cdot 10^{4}$ | $24 \cdot 10^{3}$ | $8 \cdot 10^{2}$ | $48 \cdot 10^{1}$ |
| $5 \cdot 10^{0}$ | $3 \cdot 10^{5}$  | $15 \cdot 10^{3}$ | $15 \cdot 10^{2}$ | $5 \cdot 10^{1}$ | $3 \cdot 10^{1}$  |
**Add these partial values by place value:**
```
6000000
0300000
4800000
0030000
0240000
0300000
0001000
0024000
0015000
0000600
0000800
0001500
0000480
0000050
0000030
```
$10^{1}$: $3 + 5 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 16$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 4 + 5 + 8 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 24$, so carry 2 to the next column.
$10^{3}$: $0 + 0 + 0 + 1 + 0 + 0 + 5 + 4 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 2 = 13$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 0 + 4 + 3 + 0 + 0 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 + 2 + 0 + 8 + 3 + 0 + 1 = 17$, so carry 1 to the next column.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 6 + 1 = 11$, so carry 1 to the next column.
$10^{7}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $11713460$.
## Step 7
$$ (111 + \frac{4(6000000 + 300000 + 4800000 + 30000 + 240000 + 300000 + 1000 + 24000 + 15000 + 600 + 800 + 1500 + 480 + 50 + 30)}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{46853840}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468538.4}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} $$

$$ (111 + \frac{46853840}{4(10^2)} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + \frac{468538.4}{4} - 6(-52) + \frac{4(-52^4)}{4})\erfc{26} \\
= (111 + 117134.6(4)(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} $$

Compute $117134.6 \cdot 4$ by place-value decomposition: form partial products, then add them.
## Step 8
Approximate $117134.6$ as $117130.0$ to control intermediate precision during multiplication.

Rewrite $117130.0$ as an integer-scaled value times $10^{1}$.
## Step 9
$$ (111 + 117130(4)(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 11713(4)(10^1)(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + (10000 + 1000 + 700 + 10 + 3)(4)10^1(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} $$


**Partial-product table:**
|                  | $1 \cdot 10^{4}$ | $1 \cdot 10^{3}$ | $7 \cdot 10^{2}$  | $1 \cdot 10^{1}$ | $3 \cdot 10^{0}$  |
| ---------------- | ---------------- | ---------------- | ----------------- | ---------------- | ----------------- |
| $4 \cdot 10^{0}$ | $4 \cdot 10^{4}$ | $4 \cdot 10^{3}$ | $28 \cdot 10^{2}$ | $4 \cdot 10^{1}$ | $12 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
40000
04000
02800
00040
00012
```
$10^{0}$: $2 + 0 + 0 + 0 + 0 = 2$
$10^{1}$: $1 + 4 + 0 + 0 + 0 = 5$
$10^{2}$: $0 + 0 + 8 + 0 + 0 = 8$
$10^{3}$: $0 + 0 + 2 + 4 + 0 = 6$
$10^{4}$: $0 + 0 + 0 + 0 + 4 = 4$
Combine the place-value columns to obtain $46852$.
## Step 10
$$ (111 + (40000 + 4000 + 2800 + 40 + 12)10^1(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 46852(10^1)(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 468520(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} $$

Compute $468520 \cdot 0.25$ by place-value decomposition: form partial products, then add them.
Rewrite $468520$ as an integer-scaled value times $10^{1}$.
Rewrite $0.25$ as an integer-scaled value times $10^{-2}$.
## Step 11
$$ (111 + 468520(0.25) - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + \frac{1171300}{10} - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + \frac{(40000 + 6000 + 800 + 50 + 2)(20 + 5)}{10} - 6(-52) + 4(-52^4)(0.25))\erfc{26} $$


**Partial-product table:**
|                  | $4 \cdot 10^{4}$ | $6 \cdot 10^{3}$  | $8 \cdot 10^{2}$  | $5 \cdot 10^{1}$  | $2 \cdot 10^{0}$ |
| ---------------- | ---------------- | ----------------- | ----------------- | ----------------- | ---------------- |
| $2 \cdot 10^{1}$ | $8 \cdot 10^{5}$ | $12 \cdot 10^{4}$ | $16 \cdot 10^{3}$ | $1 \cdot 10^{3}$  | $4 \cdot 10^{1}$ |
| $5 \cdot 10^{0}$ | $2 \cdot 10^{5}$ | $3 \cdot 10^{4}$  | $4 \cdot 10^{3}$  | $25 \cdot 10^{1}$ | $1 \cdot 10^{1}$ |
**Add these partial values by place value:**
```
800000
120000
200000
016000
030000
001000
004000
000040
000250
000010
```
$10^{1}$: $1 + 5 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 10$, so carry 1 to the next column.
$10^{2}$: $0 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 3$
$10^{3}$: $0 + 0 + 0 + 4 + 1 + 0 + 6 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 3 + 1 + 0 + 2 + 0 + 1 = 7$
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 1 + 8 = 11$, so carry 1 to the next column.
$10^{6}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $1171300$.
## Step 12
$$ (111 + \frac{800000 + 120000 + 200000 + 16000 + 30000 + 1000 + 4000 + 40 + 250 + 10}{10} - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + \frac{1171300}{10} - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - 6(-52) + 4(-52^4)(0.25))\erfc{26} $$

$$ (111 + \frac{1171300}{10} - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 4(-52^4)(0.25))\erfc{26} $$

## Step 13
$$ (111 + 117130 - 6(-52) + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 4(-52(-52)(-52)(-52))0.25)\erfc{26} $$

Compute $-52 \cdot -52$ by place-value decomposition: form partial products, then add them.
$$ (111 + 117130 - -312 + 4(-52^4)(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 4(-52(-52)(-52)(-52))0.25)\erfc{26} \\
= (111 + 117130 - -312 + 4(-50 - 2)(-50 - 2)52(52)0.25)\erfc{26} $$


**Partial-product table:**
|                   | $-5 \cdot 10^{1}$ | $-2 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- |
| $-5 \cdot 10^{1}$ | $25 \cdot 10^{2}$ | $1 \cdot 10^{2}$  |
| $-2 \cdot 10^{0}$ | $1 \cdot 10^{2}$  | $4 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
2500
0100
0100
0004
```
$10^{0}$: $4 + 0 + 0 + 0 = 4$
$10^{2}$: $0 + 1 + 1 + 5 = 7$
$10^{3}$: $0 + 0 + 0 + 2 = 2$
Combine the place-value columns to obtain $2704$.
Compute $2704 \cdot -52$ by place-value decomposition: form partial products, then add them.
## Step 14

**Partial-product table:**
|                   | $2 \cdot 10^{3}$  | $7 \cdot 10^{2}$   | $4 \cdot 10^{0}$  |
| ----------------- | ----------------- | ------------------ | ----------------- |
| $-5 \cdot 10^{1}$ | $-1 \cdot 10^{5}$ | $-35 \cdot 10^{3}$ | $-2 \cdot 10^{2}$ |
| $-2 \cdot 10^{0}$ | $-4 \cdot 10^{3}$ | $-14 \cdot 10^{2}$ | $-8 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-100000
-035000
-004000
-000200
-001400
-000008
```
$10^{0}$: $-8 + 0 + 0 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{2}$: $0 - 4 - 2 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{3}$: $0 - 1 + 0 - 4 - 5 + 0 - 1 = -11$, so borrow 2 from the next column and write 9 here.
$10^{4}$: $0 + 0 + 0 + 0 - 3 + 0 - 2 = -5$, so borrow 1 from the next column and write 5 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 - 1 - 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $-140608$.
Compute $-140608 \cdot -52$ by place-value decomposition: form partial products, then add them.
## Step 15

**Partial-product table:**
|                   | $-1 \cdot 10^{5}$ | $-4 \cdot 10^{4}$ | $-6 \cdot 10^{2}$ | $-8 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $-5 \cdot 10^{1}$ | $5 \cdot 10^{6}$  | $2 \cdot 10^{6}$  | $3 \cdot 10^{4}$  | $4 \cdot 10^{2}$  |
| $-2 \cdot 10^{0}$ | $2 \cdot 10^{5}$  | $8 \cdot 10^{4}$  | $12 \cdot 10^{2}$ | $16 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
5000000
2000000
0200000
0030000
0080000
0000400
0001200
0000016
```
$10^{0}$: $6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{1}$: $1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{2}$: $0 + 2 + 4 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{3}$: $0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{4}$: $0 + 0 + 0 + 8 + 3 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 2 + 0 + 0 + 1 = 3$
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 2 + 5 = 7$
Combine the place-value columns to obtain $7311616$.
$$ (111 + 117130 - -312 + (5000000 + 2000000 + 200000 + 30000 + 80000 + 400 + 1200 + 16)4(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 7311616(4)(0.25))\erfc{26} \\
= (111 + 117130 - -312 + 29246464(0.25))\erfc{26} $$

Compute $29246464 \cdot 0.25$ by place-value decomposition: form partial products, then add them.
Rewrite $0.25$ as an integer-scaled value times $10^{-2}$.
## Step 16
$$ (111 + 117130 - -312 + 29246464(0.25))\erfc{26} \\
= (111 + 117130 - -312 + \frac{731161600}{10^2})\erfc{26} \\
= (111 + 117130 - -312 + \frac{(20000000 + 9000000 + 200000 + 40000 + 6000 + 400 + 60 + 4)(20 + 5)}{10^2})\erfc{26} $$


**Partial-product table:**
|                  | $2 \cdot 10^{7}$ | $9 \cdot 10^{6}$  | $2 \cdot 10^{5}$ | $4 \cdot 10^{4}$ | $6 \cdot 10^{3}$  | $4 \cdot 10^{2}$ | $6 \cdot 10^{1}$  | $4 \cdot 10^{0}$ |
| ---------------- | ---------------- | ----------------- | ---------------- | ---------------- | ----------------- | ---------------- | ----------------- | ---------------- |
| $2 \cdot 10^{1}$ | $4 \cdot 10^{8}$ | $18 \cdot 10^{7}$ | $4 \cdot 10^{6}$ | $8 \cdot 10^{5}$ | $12 \cdot 10^{4}$ | $8 \cdot 10^{3}$ | $12 \cdot 10^{2}$ | $8 \cdot 10^{1}$ |
| $5 \cdot 10^{0}$ | $1 \cdot 10^{8}$ | $45 \cdot 10^{6}$ | $1 \cdot 10^{6}$ | $2 \cdot 10^{5}$ | $3 \cdot 10^{4}$  | $2 \cdot 10^{3}$ | $3 \cdot 10^{2}$  | $2 \cdot 10^{1}$ |
**Add these partial values by place value:**
```
400000000
180000000
100000000
004000000
045000000
000800000
001000000
000120000
000200000
000008000
000030000
000001200
000002000
000000080
000000300
000000020
```
$10^{1}$: $2 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 10$, so carry 1 to the next column.
$10^{2}$: $0 + 3 + 0 + 0 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 6$
$10^{3}$: $0 + 0 + 0 + 2 + 1 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 6$
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 1 + 0 + 8 + 0 + 0 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 5 + 4 + 0 + 0 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 8 + 0 + 1 = 13$, so carry 1 to the next column.
$10^{8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 1 + 4 + 1 = 7$
Combine the place-value columns to obtain $731161600$.
## Step 17
$$ (111 + 117130 - -312 + \frac{400000000 + 180000000 + 100000000 + 4000000 + 45000000 + 800000 + 1000000 + 120000 + 200000 + 8000 + 30000 + 1200 + 2000 + 80 + 300 + 20}{10^2})\erfc{26} \\
= (111 + 117130 - -312 + \frac{731161600}{10^2})\erfc{26} \\
= (111 + 117130 - -312 + 7311616)\erfc{26} $$

Decompose $-312$ and $7311616.0$ into place-value components.
## Step 18
```
-0000300
-0000010
-0000002
 7000000
 0300000
 0010000
 0001000
 0000600
 0000010
 0000006
```
$10^{0}$: $6 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 = 4$
$10^{2}$: $0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 - 3 = 3$
$10^{3}$: $0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{4}$: $0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 0 + 0 = 3$
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 + 0 = 7$
Combine the place-value columns to obtain $7311304$.
Decompose $111.0$ and $117130.0$ into place-value components.
## Step 19
```
000100
000010
000001
100000
010000
007000
000100
000030
```
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 = 1$
$10^{1}$: $3 + 0 + 0 + 0 + 0 + 0 + 1 + 0 = 4$
$10^{2}$: $0 + 1 + 0 + 0 + 0 + 0 + 0 + 1 = 2$
$10^{3}$: $0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{4}$: $0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 = 1$
$10^{5}$: $0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 = 1$
Combine the place-value columns to obtain $117241$.
Decompose $117241$ and $-7311304$ into place-value components.
## Step 20
```
 0100000
 0010000
 0007000
 0000200
 0000040
 0000001
-7000000
-0300000
-0010000
-0001000
-0000300
-0000004
```
$10^{0}$: $-4 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 = -3$, so borrow 1 from the next column and write 7 here.
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 - 1 = 3$
$10^{2}$: $0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 0 + 0 + 0 = -1$, so borrow 1 from the next column and write 9 here.
$10^{3}$: $0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 7 + 0 + 0 - 1 = 5$
$10^{5}$: $0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{6}$: $0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
Combine the place-value columns to obtain $-7194063$.
$$ (100000 + 10000 + 7000 + 200 + 40 + 1 - 7000000 - 300000 - 10000 - 1000 - 300 - 4)\erfc{26} \\
= -7194063\erfc{26} \\
= -7194063(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000566319240885614) $$

Compute $5.663192408856143e-296 \cdot -7194063$ by place-value decomposition: form partial products, then add them.
Approximate $5.663192408856143e-296$ as $5.663199999999983e-296$ to control intermediate precision during multiplication.

Rewrite $5.663199999999983e-296$ as an integer-scaled value times $10^{-310}$.
## Step 21
$$ -7194063(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000566319999999998) \\
= \frac{-4074141758159985611874}{10^310} \\
= \frac{(500000000000000 + 60000000000000 + 6000000000000 + 300000000000 + 10000000000 + 9000000000 + 900000000 + 90000000 + 9000000 + 900000 + 90000 + 9000 + 900 + 90 + 8)(-7000000 - 100000 - 90000 - 4000 - 60 - 3)}{10^310} $$


**Partial-product table:**
|                   | $5 \cdot 10^{14}$   | $6 \cdot 10^{13}$   | $6 \cdot 10^{12}$   | $3 \cdot 10^{11}$   | $1 \cdot 10^{10}$  | $9 \cdot 10^{9}$    | $9 \cdot 10^{8}$    | $9 \cdot 10^{7}$    | $9 \cdot 10^{6}$    | $9 \cdot 10^{5}$    | $9 \cdot 10^{4}$    | $9 \cdot 10^{3}$   | $9 \cdot 10^{2}$   | $9 \cdot 10^{1}$   | $8 \cdot 10^{0}$   |
| ----------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------ | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------ | ------------------ | ------------------ | ------------------ |
| $-7 \cdot 10^{6}$ | $-35 \cdot 10^{20}$ | $-42 \cdot 10^{19}$ | $-42 \cdot 10^{18}$ | $-21 \cdot 10^{17}$ | $-7 \cdot 10^{16}$ | $-63 \cdot 10^{15}$ | $-63 \cdot 10^{14}$ | $-63 \cdot 10^{13}$ | $-63 \cdot 10^{12}$ | $-63 \cdot 10^{11}$ | $-63 \cdot 10^{10}$ | $-63 \cdot 10^{9}$ | $-63 \cdot 10^{8}$ | $-63 \cdot 10^{7}$ | $-56 \cdot 10^{6}$ |
| $-1 \cdot 10^{5}$ | $-5 \cdot 10^{19}$  | $-6 \cdot 10^{18}$  | $-6 \cdot 10^{17}$  | $-3 \cdot 10^{16}$  | $-1 \cdot 10^{15}$ | $-9 \cdot 10^{14}$  | $-9 \cdot 10^{13}$  | $-9 \cdot 10^{12}$  | $-9 \cdot 10^{11}$  | $-9 \cdot 10^{10}$  | $-9 \cdot 10^{9}$   | $-9 \cdot 10^{8}$  | $-9 \cdot 10^{7}$  | $-9 \cdot 10^{6}$  | $-8 \cdot 10^{5}$  |
| $-9 \cdot 10^{4}$ | $-45 \cdot 10^{18}$ | $-54 \cdot 10^{17}$ | $-54 \cdot 10^{16}$ | $-27 \cdot 10^{15}$ | $-9 \cdot 10^{14}$ | $-81 \cdot 10^{13}$ | $-81 \cdot 10^{12}$ | $-81 \cdot 10^{11}$ | $-81 \cdot 10^{10}$ | $-81 \cdot 10^{9}$  | $-81 \cdot 10^{8}$  | $-81 \cdot 10^{7}$ | $-81 \cdot 10^{6}$ | $-81 \cdot 10^{5}$ | $-72 \cdot 10^{4}$ |
| $-4 \cdot 10^{3}$ | $-2 \cdot 10^{18}$  | $-24 \cdot 10^{16}$ | $-24 \cdot 10^{15}$ | $-12 \cdot 10^{14}$ | $-4 \cdot 10^{13}$ | $-36 \cdot 10^{12}$ | $-36 \cdot 10^{11}$ | $-36 \cdot 10^{10}$ | $-36 \cdot 10^{9}$  | $-36 \cdot 10^{8}$  | $-36 \cdot 10^{7}$  | $-36 \cdot 10^{6}$ | $-36 \cdot 10^{5}$ | $-36 \cdot 10^{4}$ | $-32 \cdot 10^{3}$ |
| $-6 \cdot 10^{1}$ | $-3 \cdot 10^{16}$  | $-36 \cdot 10^{14}$ | $-36 \cdot 10^{13}$ | $-18 \cdot 10^{12}$ | $-6 \cdot 10^{11}$ | $-54 \cdot 10^{10}$ | $-54 \cdot 10^{9}$  | $-54 \cdot 10^{8}$  | $-54 \cdot 10^{7}$  | $-54 \cdot 10^{6}$  | $-54 \cdot 10^{5}$  | $-54 \cdot 10^{4}$ | $-54 \cdot 10^{3}$ | $-54 \cdot 10^{2}$ | $-48 \cdot 10^{1}$ |
| $-3 \cdot 10^{0}$ | $-15 \cdot 10^{14}$ | $-18 \cdot 10^{13}$ | $-18 \cdot 10^{12}$ | $-9 \cdot 10^{11}$  | $-3 \cdot 10^{10}$ | $-27 \cdot 10^{9}$  | $-27 \cdot 10^{8}$  | $-27 \cdot 10^{7}$  | $-27 \cdot 10^{6}$  | $-27 \cdot 10^{5}$  | $-27 \cdot 10^{4}$  | $-27 \cdot 10^{3}$ | $-27 \cdot 10^{2}$ | $-27 \cdot 10^{1}$ | $-24 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-3500000000000000000000
-0420000000000000000000
-0050000000000000000000
-0042000000000000000000
-0006000000000000000000
-0045000000000000000000
-0002100000000000000000
-0000600000000000000000
-0005400000000000000000
-0002000000000000000000
-0000070000000000000000
-0000030000000000000000
-0000540000000000000000
-0000240000000000000000
-0000030000000000000000
-0000063000000000000000
-0000001000000000000000
-0000027000000000000000
-0000024000000000000000
-0000003600000000000000
-0000001500000000000000
-0000006300000000000000
-0000000900000000000000
-0000000900000000000000
-0000001200000000000000
-0000000360000000000000
-0000000180000000000000
-0000000630000000000000
-0000000090000000000000
-0000000810000000000000
-0000000040000000000000
-0000000018000000000000
-0000000018000000000000
-0000000063000000000000
-0000000009000000000000
-0000000081000000000000
-0000000036000000000000
-0000000000600000000000
-0000000000900000000000
-0000000006300000000000
-0000000000900000000000
-0000000008100000000000
-0000000003600000000000
-0000000000540000000000
-0000000000030000000000
-0000000000630000000000
-0000000000090000000000
-0000000000810000000000
-0000000000360000000000
-0000000000054000000000
-0000000000027000000000
-0000000000063000000000
-0000000000009000000000
-0000000000081000000000
-0000000000036000000000
-0000000000005400000000
-0000000000002700000000
-0000000000006300000000
-0000000000000900000000
-0000000000008100000000
-0000000000003600000000
-0000000000000540000000
-0000000000000270000000
-0000000000000630000000
-0000000000000090000000
-0000000000000810000000
-0000000000000360000000
-0000000000000054000000
-0000000000000027000000
-0000000000000056000000
-0000000000000009000000
-0000000000000081000000
-0000000000000036000000
-0000000000000005400000
-0000000000000002700000
-0000000000000000800000
-0000000000000008100000
-0000000000000003600000
-0000000000000000540000
-0000000000000000270000
-0000000000000000720000
-0000000000000000360000
-0000000000000000054000
-0000000000000000027000
-0000000000000000032000
-0000000000000000005400
-0000000000000000002700
-0000000000000000000480
-0000000000000000000270
-0000000000000000000024
```
$10^{0}$: $-4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -4$, so borrow 1 from the next column and write 6 here.
$10^{1}$: $-2 - 7 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -18$, so borrow 2 from the next column and write 2 here.
$10^{2}$: $0 - 2 - 4 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -19$, so borrow 2 from the next column and write 1 here.
$10^{3}$: $0 + 0 + 0 - 2 - 5 - 2 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -22$, so borrow 3 from the next column and write 8 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 3 - 2 - 5 - 6 - 2 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 = -32$, so borrow 4 from the next column and write 8 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 7 - 2 - 5 - 6 - 1 - 8 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 = -47$, so borrow 5 from the next column and write 3 here.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 2 - 5 - 6 - 1 - 9 - 6 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 = -56$, so borrow 6 from the next column and write 4 here.
$10^{7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 5 - 2 - 5 - 6 - 1 - 9 - 3 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -59$, so borrow 6 from the next column and write 1 here.
$10^{8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 - 2 - 5 - 6 - 1 - 9 - 3 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -60$, so borrow 6 from the next column and write 0 here.
$10^{9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 - 2 - 5 - 6 - 1 - 9 - 3 - 7 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -60$, so borrow 6 from the next column and write 0 here.
$10^{10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 - 2 - 5 - 6 - 1 - 9 - 3 - 3 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -56$, so borrow 6 from the next column and write 4 here.
$10^{11}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 + 0 - 5 - 6 - 1 - 9 - 3 - 9 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -62$, so borrow 7 from the next column and write 8 here.
$10^{12}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 + 0 + 0 - 6 - 1 - 9 - 3 - 8 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 = -59$, so borrow 6 from the next column and write 1 here.
$10^{13}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 - 6 - 1 - 1 - 4 - 1 - 9 - 3 - 8 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -56$, so borrow 6 from the next column and write 4 here.
$10^{14}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 - 6 - 1 - 3 - 2 - 9 - 9 - 3 - 5 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -58$, so borrow 6 from the next column and write 2 here.
$10^{15}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 - 6 - 1 - 3 - 4 - 7 - 1 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 = -32$, so borrow 4 from the next column and write 8 here.
$10^{16}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 2 + 0 - 6 - 3 - 4 - 4 - 3 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 = -35$, so borrow 4 from the next column and write 5 here.
$10^{17}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 5 + 0 + 0 + 0 - 4 - 6 - 1 + 0 + 0 + 0 + 0 + 0 + 0 - 4 = -22$, so borrow 3 from the next column and write 8 here.
$10^{18}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 5 + 0 - 2 - 5 - 6 - 2 + 0 + 0 + 0 - 3 = -25$, so borrow 3 from the next column and write 5 here.
$10^{19}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 - 4 - 5 - 2 + 0 - 3 = -18$, so borrow 2 from the next column and write 2 here.
$10^{20}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 - 5 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{21}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 2 = -5$, so borrow 1 from the next column and write 5 here.
Combine the place-value columns to obtain $-4074141758159985611874$.
## Step 22
$$ \frac{-3500000000000000000000 - 420000000000000000000 - 50000000000000000000 - 42000000000000000000 - 6000000000000000000 - 45000000000000000000 - 2100000000000000000 - 600000000000000000 - 5400000000000000000 - 2000000000000000000 - 70000000000000000 - 30000000000000000 - 540000000000000000 - 240000000000000000 - 30000000000000000 - 63000000000000000 - 1000000000000000 - 27000000000000000 - 24000000000000000 - 3600000000000000 - 1500000000000000 - 6300000000000000 - 900000000000000 - 900000000000000 - 1200000000000000 - 360000000000000 - 180000000000000 - 630000000000000 - 90000000000000 - 810000000000000 - 40000000000000 - 18000000000000 - 18000000000000 - 63000000000000 - 9000000000000 - 81000000000000 - 36000000000000 - 600000000000 - 900000000000 - 6300000000000 - 900000000000 - 8100000000000 - 3600000000000 - 540000000000 - 30000000000 - 630000000000 - 90000000000 - 810000000000 - 360000000000 - 54000000000 - 27000000000 - 63000000000 - 9000000000 - 81000000000 - 36000000000 - 5400000000 - 2700000000 - 6300000000 - 900000000 - 8100000000 - 3600000000 - 540000000 - 270000000 - 630000000 - 90000000 - 810000000 - 360000000 - 54000000 - 27000000 - 56000000 - 9000000 - 81000000 - 36000000 - 5400000 - 2700000 - 800000 - 8100000 - 3600000 - 540000 - 270000 - 720000 - 360000 - 54000 - 27000 - 32000 - 5400 - 2700 - 480 - 270 - 24}{10^310} \\
= \frac{-4074141758159985611874}{10^310} \\
= -0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000407414175815997 $$

$$ \frac{-4074141758159985611874}{10^310} \\
= -0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000407414175815997 $$



---

## Case 24 (seed=17023, difficulty=advanced, guarantee_solvable=False)

- Problem: $13 - 11.6 - 5 + γ^{\acosh{3.7}}$
- Answer: $92.4941489154742$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $γ = 10$.
$$ 13 - 11.6 - 5 + γ^{\acosh{3.7}} \\
= 13 - 11.6 - 5 + γ^{\acosh{3.7}} \\
= 13 - 11.6 - 5 + 10^{\acosh{3.7}} $$

Decompose $13$ and $-11.6$ into place-value components.
$$ 13 - 11.6 - 5 + γ^{\acosh{3.7}} \\
= 13 - 11.6 - 5 + 10^{\acosh{3.7}} \\
= 10 + 3 - 10 - 1 - 0.6 - 5 + 10^{\acosh{3.7}} $$

```
 10.0
 03.0
-10.0
-01.0
-00.6
```
$10^{-1}$: $-6 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{0}$: $0 - 1 + 0 + 3 + 0 - 1 = 1$
Combine the place-value columns to obtain $1.4$.
$$ 10 + 3 - 10 - 1 - 0.6 - 5 + 10^{\acosh{3.7}} \\
= 1.4 - 5 + 10^{\acosh{3.7}} \\
= 1.4 - 5 + 10^1.9826969446812 $$

## Step 2
$$ 1.4 - 5 + 10^{\acosh{3.7}} \\
= 1.4 - 5 + 10^1.9826969446812 \\
= 1.4 - 5 + 96.0941489154742 $$

## Step 3
$$ 1.4 - 5 + 10^1.9826969446812 \\
= 1.4 - 5 + 96.0941489154742 \\
= -3.6 + 96.0941489154742 $$

Decompose $-3.6$ and $96.09414891547418$ into place-value components.
## Step 4
```
-03.0000000000000
-00.6000000000000
 90.0000000000000
 06.0000000000000
 00.0900000000000
 00.0040000000000
 00.0001000000000
 00.0000400000000
 00.0000080000000
 00.0000009000000
 00.0000000100000
 00.0000000050000
 00.0000000004000
 00.0000000000700
 00.0000000000040
 00.0000000000002
```
$10^{-13}$: $2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{-12}$: $0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-11}$: $0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7$
$10^{-10}$: $0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-9}$: $0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 9$
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{-5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-3}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 = 9$
$10^{-1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 6 + 0 + 0 - 3 - 1 = 2$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 + 0 = 9$
Combine the place-value columns to obtain $92.4941489154742$.
$$ -3 - 0.6 + 90 + 6 + 0.09 + 0.004 + 0.0001 + 0.00004 + 0.000008 + 0.0000009 + 0.00000001 + 0.000000005 + 0.0000000004 + 0.00000000007 + 0.000000000004 + 0.0000000000002 \\
= 92.4941489154742 $$



---

## Case 25 (seed=17024, difficulty=beginner, guarantee_solvable=True)

- Problem: $(-3 - 15.1)4(3)$
- Answer: $-217.2$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Decompose $-3$ and $-15.1$ into place-value components.
$$ (-3 - 15.1)4(3) \\
= (-3 - 15.1)4(3) \\
= (-3 - 10 - 5 - 0.1)4(3) $$

```
-03.0
-10.0
-05.0
-00.1
```
$10^{-1}$: $-1 + 0 + 0 + 0 = -1$, so borrow 1 from the next column and write 9 here.
$10^{0}$: $0 - 5 + 0 - 3 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{1}$: $0 + 0 - 1 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $-18.099999999999994$.
Compute $4 \cdot -18.099999999999994$ by place-value decomposition: form partial products, then add them.
Rewrite $-18.099999999999994$ as an integer-scaled value times $10^{-1}$.
## Step 2
$$ -18.1(4)3 \\
= (\frac{-724}{10})3 \\
= (\frac{(4)(-100 - 80 - 1)}{10})3 $$


**Partial-product table:**
|                   | $4 \cdot 10^{0}$   |
| ----------------- | ------------------ |
| $-1 \cdot 10^{2}$ | $-4 \cdot 10^{2}$  |
| $-8 \cdot 10^{1}$ | $-32 \cdot 10^{1}$ |
| $-1 \cdot 10^{0}$ | $-4 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
-400
-320
-004
```
$10^{0}$: $-4 + 0 + 0 = -4$, so borrow 1 from the next column and write 6 here.
$10^{1}$: $0 - 2 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{2}$: $0 - 3 - 4 - 1 = -8$, so borrow 1 from the next column and write 2 here.
Combine the place-value columns to obtain $-724$.
## Step 3
$$ (\frac{-400 - 320 - 4}{10})3 \\
= (\frac{-724}{10})3 \\
= -72.4(3) $$

Compute $3 \cdot -72.4$ by place-value decomposition: form partial products, then add them.
Rewrite $-72.4$ as an integer-scaled value times $10^{-1}$.
## Step 4
$$ -72.4(3) \\
= \frac{-2172}{10} \\
= \frac{(3)(-700 - 20 - 4)}{10} $$


**Partial-product table:**
|                   | $3 \cdot 10^{0}$   |
| ----------------- | ------------------ |
| $-7 \cdot 10^{2}$ | $-21 \cdot 10^{2}$ |
| $-2 \cdot 10^{1}$ | $-6 \cdot 10^{1}$  |
| $-4 \cdot 10^{0}$ | $-12 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-2100
-0060
-0012
```
$10^{0}$: $-2 + 0 + 0 = -2$, so borrow 1 from the next column and write 8 here.
$10^{1}$: $-1 - 6 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{2}$: $0 + 0 - 1 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{3}$: $0 + 0 - 2 - 1 = -3$, so borrow 1 from the next column and write 7 here.
Combine the place-value columns to obtain $-2172$.
## Step 5
$$ \frac{-2100 - 60 - 12}{10} \\
= \frac{-2172}{10} \\
= -217.2 $$

$$ \frac{-2172}{10} \\
= -217.2 $$



---

## Case 26 (seed=17025, difficulty=intermediate, guarantee_solvable=False)

- Problem: $-10 + 12.65$
- Answer: $2.65$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Decompose $-10$ and $12.65$ into place-value components.
$$ -10 + 12.65 \\
= -10 + 12.65 \\
= -10 + 10 + 2 + 0.6 + 0.05 $$

```
-10.00
 10.00
 02.00
 00.60
 00.05
```
$10^{-2}$: $5 + 0 + 0 + 0 + 0 = 5$
$10^{-1}$: $0 + 6 + 0 + 0 + 0 = 6$
$10^{0}$: $0 + 0 + 2 + 0 + 0 = 2$
Combine the place-value columns to obtain $2.65$.
$$ -10 + 10 + 2 + 0.6 + 0.05 \\
= 2.65 $$


---

## Case 27 (seed=17026, difficulty=advanced, guarantee_solvable=True)

- Problem: $(33 + 4.2 + 13)((c - 19)0.9 + 2.7)1$
- Answer: $-722.88 + 45.18c$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ (33 + 4.2 + 13)((c - 19)0.9 + 2.7)1 \\
= (33 + 4.2 + 13)((c - 19)0.9 + 2.7)1 \\
= (17.2 + 33)((c - 19)0.9 + 2.7)1 $$

Decompose $33$ and $17.2$ into place-value components.
## Step 2
```
30.0
03.0
10.0
07.0
00.2
```
$10^{-1}$: $2 + 0 + 0 + 0 + 0 = 2$
$10^{0}$: $0 + 7 + 0 + 3 + 0 = 10$, so carry 1 to the next column.
$10^{1}$: $0 + 0 + 1 + 0 + 3 + 1 = 5$
Combine the place-value columns to obtain $50.2$.
$$ (30 + 3 + 10 + 7 + 0.2)((c - 19)0.9 + 2.7)1 \\
= 50.2((c - 19)0.9 + 2.7)1 \\
= 50.2(0.9c - 17.1 + 2.7)1 $$

## Step 3
$$ 50.2((c - 19)0.9 + 2.7)1 \\
= 50.2(0.9c - 17.1 + 2.7)1 \\
= 50.2(0.9c - 17.1 + 2.7)1 $$

Decompose $-17.1$ and $2.7$ into place-value components.
$$ 50.2(0.9c - 17.1 + 2.7)1 \\
= 50.2(0.9c - 17.1 + 2.7)1 \\
= 50.2(-10 - 7 - 0.1 + 2 + 0.7 + 0.9c)1 $$

```
-10.0
-07.0
-00.1
 02.0
 00.7
```
$10^{-1}$: $7 + 0 - 1 + 0 + 0 = 6$
$10^{0}$: $0 + 2 + 0 - 7 + 0 = -5$, so borrow 1 from the next column and write 5 here.
$10^{1}$: $0 + 0 + 0 + 0 - 1 - 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $-14.400000000000006$.
$$ 50.2(-10 - 7 - 0.1 + 2 + 0.7 + 0.9c)1 \\
= 50.2(-14.4 + 0.9c)1 \\
= (-14.4 + 0.9c)50.2(1) \\
= -722.88 + 45.18c $$



---

## Case 28 (seed=17027, difficulty=beginner, guarantee_solvable=False)

- Problem: $(3 + 4.4)20(1 - -187)$
- Answer: $27824$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
$$ (3 + 4.4)20(1 - -187) \\
= (3 + 4.4)20(1 - -187) \\
= 7.4(20)(1 - -187) $$

Compute $20 \cdot 7.4$ by place-value decomposition: form partial products, then add them.
Rewrite $20$ as an integer-scaled value times $10^{1}$.
Rewrite $7.4$ as an integer-scaled value times $10^{-1}$.
## Step 2
$$ 7.4(20)(1 - -187) \\
= 2(74)(10^0)(1 - -187) \\
= (2)(70 + 4)10^0(1 - -187) $$


**Partial-product table:**
|                  | $2 \cdot 10^{0}$  |
| ---------------- | ----------------- |
| $7 \cdot 10^{1}$ | $14 \cdot 10^{1}$ |
| $4 \cdot 10^{0}$ | $8 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
140
008
```
$10^{0}$: $8 + 0 = 8$
$10^{1}$: $0 + 4 = 4$
$10^{2}$: $0 + 1 = 1$
Combine the place-value columns to obtain $148$.
$$ (140 + 8)10^0(1 - -187) \\
= 148(10^0)(1 - -187) \\
= 148(10^0)(1 + 187) $$

## Step 3
$$ 148(10^0)(1 - -187) \\
= 148(10^0)(1 + 187) \\
= 148(10^0)(188) $$

Compute $188 \cdot 148$ by place-value decomposition: form partial products, then add them.
## Step 4

**Partial-product table:**
|                  | $1 \cdot 10^{2}$ | $8 \cdot 10^{1}$  | $8 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- | ----------------- |
| $1 \cdot 10^{2}$ | $1 \cdot 10^{4}$ | $8 \cdot 10^{3}$  | $8 \cdot 10^{2}$  |
| $4 \cdot 10^{1}$ | $4 \cdot 10^{3}$ | $32 \cdot 10^{2}$ | $32 \cdot 10^{1}$ |
| $8 \cdot 10^{0}$ | $8 \cdot 10^{2}$ | $64 \cdot 10^{1}$ | $64 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
10000
08000
04000
00800
03200
00800
00320
00640
00064
```
$10^{0}$: $4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{1}$: $6 + 4 + 2 + 0 + 0 + 0 + 0 + 0 + 0 = 12$, so carry 1 to the next column.
$10^{2}$: $0 + 6 + 3 + 8 + 2 + 8 + 0 + 0 + 0 + 1 = 28$, so carry 2 to the next column.
$10^{3}$: $0 + 0 + 0 + 0 + 3 + 0 + 4 + 8 + 0 + 2 = 17$, so carry 1 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 1 = 2$
Combine the place-value columns to obtain $27824$.
$$ 10000 + 8000 + 4000 + 800 + 3200 + 800 + 320 + 640 + 64 \\
= 27824 $$



---

## Case 29 (seed=17028, difficulty=intermediate, guarantee_solvable=True)

- Problem: $21^9.6$
- Answer: $4.93520537 \times 10^{12}$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

$$ 21^9.6 \\
= 21^9.6 \\
= 4935205366060.78 $$


---

## Case 30 (seed=17029, difficulty=advanced, guarantee_solvable=False)

- Problem: $\frac{1}{B^8}$
- Answer: $4.78865133 \times 10^{-12}$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

Substitute the given values: $B = 26$.
$$ \frac{1}{B^8} \\
= \frac{1}{B^8} \\
= \frac{1}{26^8} \\
= 0.000000000004788651327501 $$


---

## Case 31 (seed=17030, difficulty=beginner, guarantee_solvable=True)

- Problem: $-38(4 - 15 + 32 + 1.6 + 7.9018)$
- Answer: $-1159.076$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
$$ -38(4 - 15 + 32 + 1.6 + 7.9018) \\
= -38(4 - 15 + 32 + 1.6 + 7.9018) \\
= -38(-11 + 32 + 1.6 + 7.9018) $$

## Step 2
$$ -38(4 - 15 + 32 + 1.6 + 7.9018) \\
= -38(-11 + 32 + 1.6 + 7.9018) \\
= -38(21 + 1.6 + 7.9018) $$

## Step 3
$$ -38(-11 + 32 + 1.6 + 7.9018) \\
= -38(21 + 1.6 + 7.9018) \\
= -38(22.6 + 7.9018) $$

Decompose $22.6$ and $7.9018$ into place-value components.
## Step 4
```
20.0000
02.0000
00.6000
07.0000
00.9000
00.0010
00.0008
```
$10^{-4}$: $8 + 0 + 0 + 0 + 0 + 0 + 0 = 8$
$10^{-3}$: $0 + 1 + 0 + 0 + 0 + 0 + 0 = 1$
$10^{-1}$: $0 + 0 + 9 + 0 + 6 + 0 + 0 = 15$, so carry 1 to the next column.
$10^{0}$: $0 + 0 + 0 + 7 + 0 + 2 + 0 + 1 = 10$, so carry 1 to the next column.
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 2 + 1 = 3$
Combine the place-value columns to obtain $30.5018$.
Compute $30.5018 \cdot -38$ by place-value decomposition: form partial products, then add them.
Approximate $30.5018$ as $30.502000000000002$ to control intermediate precision during multiplication.

Rewrite $30.502000000000002$ as an integer-scaled value times $10^{-3}$.
## Step 5
$$ -38(30.502) \\
= \frac{-1159076}{10^3} \\
= \frac{(30000 + 500 + 2)(-30 - 8)}{10^3} $$


**Partial-product table:**
|                   | $3 \cdot 10^{4}$   | $5 \cdot 10^{2}$   | $2 \cdot 10^{0}$   |
| ----------------- | ------------------ | ------------------ | ------------------ |
| $-3 \cdot 10^{1}$ | $-9 \cdot 10^{5}$  | $-15 \cdot 10^{3}$ | $-6 \cdot 10^{1}$  |
| $-8 \cdot 10^{0}$ | $-24 \cdot 10^{4}$ | $-4 \cdot 10^{3}$  | $-16 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-900000
-015000
-240000
-000060
-004000
-000016
```
$10^{0}$: $-6 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{1}$: $-1 + 0 - 6 + 0 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{2}$: $0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{3}$: $0 - 4 + 0 + 0 - 5 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{4}$: $0 + 0 + 0 - 4 - 1 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{5}$: $0 + 0 + 0 - 2 + 0 - 9 - 1 = -12$, so borrow 2 from the next column and write 8 here.
Combine the place-value columns to obtain $-1159076$.
## Step 6
$$ \frac{-900000 - 15000 - 240000 - 60 - 4000 - 16}{10^3} \\
= \frac{-1159076}{10^3} \\
= -1159.076 $$

$$ \frac{-1159076}{10^3} \\
= -1159.076 $$



---

## Case 32 (seed=17031, difficulty=intermediate, guarantee_solvable=False)

- Problem: $32.7c31.3$
- Answer: $-20470.2$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $c = -20$.
$$ 32.7c31.3 \\
= 32.7c31.3 \\
= 32.7(-20(31.3)) $$

Compute $31.3 \cdot -20$ by place-value decomposition: form partial products, then add them.
Rewrite $31.3$ as an integer-scaled value times $10^{-1}$.
Rewrite $-20$ as an integer-scaled value times $10^{1}$.
$$ 32.7(-20(31.3)) \\
= 32.7(313(-2)(10^0)) \\
= 32.7(300 + 10 + 3)(-2) $$


**Partial-product table:**
|                   | $3 \cdot 10^{2}$  | $1 \cdot 10^{1}$  | $3 \cdot 10^{0}$  |
| ----------------- | ----------------- | ----------------- | ----------------- |
| $-2 \cdot 10^{0}$ | $-6 \cdot 10^{2}$ | $-2 \cdot 10^{1}$ | $-6 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-600
-020
-006
```
$10^{0}$: $-6 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{1}$: $0 - 2 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{2}$: $0 + 0 - 6 - 1 = -7$, so borrow 1 from the next column and write 3 here.
Combine the place-value columns to obtain $-626$.
Compute $32.7 \cdot -626$ by place-value decomposition: form partial products, then add them.
Rewrite $32.7$ as an integer-scaled value times $10^{-1}$.
## Step 2
$$ 32.7(-626) \\
= \frac{-204702}{10} \\
= \frac{(300 + 20 + 7)(-600 - 20 - 6)}{10} $$


**Partial-product table:**
|                   | $3 \cdot 10^{2}$   | $2 \cdot 10^{1}$   | $7 \cdot 10^{0}$   |
| ----------------- | ------------------ | ------------------ | ------------------ |
| $-6 \cdot 10^{2}$ | $-18 \cdot 10^{4}$ | $-12 \cdot 10^{3}$ | $-42 \cdot 10^{2}$ |
| $-2 \cdot 10^{1}$ | $-6 \cdot 10^{3}$  | $-4 \cdot 10^{2}$  | $-14 \cdot 10^{1}$ |
| $-6 \cdot 10^{0}$ | $-18 \cdot 10^{2}$ | $-12 \cdot 10^{1}$ | $-42 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-180000
-012000
-006000
-004200
-000400
-001800
-000140
-000120
-000042
```
$10^{0}$: $-2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -2$, so borrow 1 from the next column and write 8 here.
$10^{1}$: $-4 - 2 - 4 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -11$, so borrow 2 from the next column and write 9 here.
$10^{2}$: $0 - 1 - 1 - 8 - 4 - 2 + 0 + 0 + 0 - 2 = -18$, so borrow 2 from the next column and write 2 here.
$10^{3}$: $0 + 0 + 0 - 1 + 0 - 4 - 6 - 2 + 0 - 2 = -15$, so borrow 2 from the next column and write 5 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 8 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 2 = -3$, so borrow 1 from the next column and write 7 here.
Combine the place-value columns to obtain $-204702$.
## Step 3
$$ \frac{-180000 - 12000 - 6000 - 4200 - 400 - 1800 - 140 - 120 - 42}{10} \\
= \frac{-204702}{10} \\
= -20470.2 $$

$$ \frac{-204702}{10} \\
= -20470.2 $$



---

## Case 33 (seed=17032, difficulty=advanced, guarantee_solvable=True)

- Problem: $(21 - 15 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(d(12.4 + 13) + d^3 + 3)$
- Answer: $71595011.6$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
Substitute the given values: $d = -32$.
$$ (21 - 15 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(d(12.4 + 13) + d^3 + 3) \\
= (21 - 15 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(d(12.4 + 13) + d^3 + 3) \\
= (21 - 15 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= (6 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

## Step 2
$$ (21 - 15 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= (6 - 26)(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(\int_{4.5}^{36} \cos{d} \, dd + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

## Step 3
Apply the Fundamental Theorem of Calculus: evaluate the antiderivative at the bounds and subtract, $F(36) - F(4.5)$.

1 to any power is 1.

## Step 4
$$ -20(1\sin{36} - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(1(-0.991778853443116) - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

## Step 5
$$ -20(1(-0.991778853443116) - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - -0.977530117665097 + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

## Step 6
$$ -20(-0.991778853443116 - \sin{4.5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - -0.977530117665097 + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - -0.977530117665097 + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

Compute $-0.977530117665097 \cdot -1$ by place-value decomposition: form partial products, then add them.
Approximate $-0.977530117665097$ as $-0.9775300000000001$ to control intermediate precision during multiplication.

Rewrite $-0.9775300000000001$ as an integer-scaled value times $10^{-5}$.
## Step 7
$$ -20(-0.991778853443116 - -0.97753 + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 - \frac{-97753}{10^5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 + \frac{(-90000 - 7000 - 700 - 50 - 3)(-1)}{10^5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$


**Partial-product table:**
|                   | $-9 \cdot 10^{4}$ | $-7 \cdot 10^{3}$ | $-7 \cdot 10^{2}$ | $-5 \cdot 10^{1}$ | $-3 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $-1 \cdot 10^{0}$ | $9 \cdot 10^{4}$  | $7 \cdot 10^{3}$  | $7 \cdot 10^{2}$  | $5 \cdot 10^{1}$  | $3 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
90000
07000
00700
00050
00003
```
$10^{0}$: $3 + 0 + 0 + 0 + 0 = 3$
$10^{1}$: $0 + 5 + 0 + 0 + 0 = 5$
$10^{2}$: $0 + 0 + 7 + 0 + 0 = 7$
$10^{3}$: $0 + 0 + 0 + 7 + 0 = 7$
$10^{4}$: $0 + 0 + 0 + 0 + 9 = 9$
Combine the place-value columns to obtain $97753$.
## Step 8
$$ -20(-0.991778853443116 + \frac{90000 + 7000 + 700 + 50 + 3}{10^5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 + \frac{97753}{10^5} + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.991778853443116 + 0.97753 + 35 + \frac{d^{2}}{dd^{2}}\sin{d})3(-32(12.4 + 13) + -32^3 + 3) $$

Decompose $-0.9917788534431158$ and $0.9775300000000001$ into place-value components.
## Step 9
```
-0.900000000000000
-0.090000000000000
-0.001000000000000
-0.000700000000000
-0.000070000000000
-0.000008000000000
-0.000000800000000
-0.000000050000000
-0.000000003000000
-0.000000000400000
-0.000000000040000
-0.000000000003000
-0.000000000000100
-0.000000000000010
-0.000000000000006
 0.900000000000000
 0.070000000000000
 0.007000000000000
 0.000500000000000
 0.000030000000000
```
$10^{-15}$: $0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-14}$: $0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-13}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-12}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-11}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{-5}$: $3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-4}$: $0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{-3}$: $0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 - 1 = 5$
$10^{-2}$: $0 + 0 + 0 + 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 + 0 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-1}$: $0 + 0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
Combine the place-value columns to obtain $-0.01424885344311555$.
Differentiate with respect to $d$ (order 2) using the applicable differentiation rules.

Compute $-0.5514266812416906 \cdot -1$ by place-value decomposition: form partial products, then add them.
Approximate $-0.5514266812416906$ as $-0.5514300000000001$ to control intermediate precision during multiplication.

Rewrite $-0.5514300000000001$ as an integer-scaled value times $10^{-5}$.
## Step 10
$$ -20(-0.0142488534431156 + 35 - -0.55143)3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.0142488534431156 + 35 - \frac{-55143}{10^5})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.0142488534431156 + 35 + \frac{(-50000 - 5000 - 100 - 40 - 3)(-1)}{10^5})3(-32(12.4 + 13) + -32^3 + 3) $$


**Partial-product table:**
|                   | $-5 \cdot 10^{4}$ | $-5 \cdot 10^{3}$ | $-1 \cdot 10^{2}$ | $-4 \cdot 10^{1}$ | $-3 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $-1 \cdot 10^{0}$ | $5 \cdot 10^{4}$  | $5 \cdot 10^{3}$  | $1 \cdot 10^{2}$  | $4 \cdot 10^{1}$  | $3 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
50000
05000
00100
00040
00003
```
$10^{0}$: $3 + 0 + 0 + 0 + 0 = 3$
$10^{1}$: $0 + 4 + 0 + 0 + 0 = 4$
$10^{2}$: $0 + 0 + 1 + 0 + 0 = 1$
$10^{3}$: $0 + 0 + 0 + 5 + 0 = 5$
$10^{4}$: $0 + 0 + 0 + 0 + 5 = 5$
Combine the place-value columns to obtain $55143$.
## Step 11
$$ -20(-0.0142488534431156 + 35 + \frac{50000 + 5000 + 100 + 40 + 3}{10^5})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.0142488534431156 + 35 + \frac{55143}{10^5})3(-32(12.4 + 13) + -32^3 + 3) \\
= -20(-0.0142488534431156 + 35 + 0.55143)3(-32(12.4 + 13) + -32^3 + 3) $$

Decompose $35$ and $0.5514300000000001$ into place-value components.
## Step 12
```
30.00000
05.00000
00.50000
00.05000
00.00100
00.00040
00.00003
```
$10^{-5}$: $3 + 0 + 0 + 0 + 0 + 0 + 0 = 3$
$10^{-4}$: $0 + 4 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{-3}$: $0 + 0 + 1 + 0 + 0 + 0 + 0 = 1$
$10^{-2}$: $0 + 0 + 0 + 5 + 0 + 0 + 0 = 5$
$10^{-1}$: $0 + 0 + 0 + 0 + 5 + 0 + 0 = 5$
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 5 + 0 = 5$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 3 = 3$
Combine the place-value columns to obtain $35.55143$.
Decompose $-0.01424885344311555$ and $35.55143$ into place-value components.
## Step 13
```
-00.0100000000000000
-00.0040000000000000
-00.0002000000000000
-00.0000400000000000
-00.0000080000000000
-00.0000008000000000
-00.0000000500000000
-00.0000000030000000
-00.0000000004000000
-00.0000000000400000
-00.0000000000030000
-00.0000000000001000
-00.0000000000000100
-00.0000000000000050
-00.0000000000000006
 30.0000000000000000
 05.0000000000000000
 00.5000000000000000
 00.0500000000000000
 00.0010000000000000
 00.0004000000000000
 00.0000300000000000
```
$10^{-16}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-15}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-14}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-13}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-12}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-11}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{-5}$: $3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-4}$: $0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 - 1 = 1$
$10^{-3}$: $0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 = -3$, so borrow 1 from the next column and write 7 here.
$10^{-2}$: $0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 1 = 3$
$10^{-1}$: $0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{1}$: $0 + 0 + 0 + 0 + 0 + 0 + 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 3$
Combine the place-value columns to obtain $35.53718114655688$.
Compute $35.53718114655688 \cdot 3$ by place-value decomposition: form partial products, then add them.
Approximate $35.53718114655688$ as $35.537$ to control intermediate precision during multiplication.

Rewrite $35.537$ as an integer-scaled value times $10^{-3}$.
## Step 14
$$ -20(35.537(3))(-32(12.4 + 13) + -32^3 + 3) \\
= \frac{-2132220(-32(12.4 + 13) + -32^3 + 3)}{10^3} \\
= \frac{-20(30000 + 5000 + 500 + 30 + 7)(3)(-32(12.4 + 13) + -32^3 + 3)}{10^3} $$


**Partial-product table:**
|                  | $3 \cdot 10^{4}$ | $5 \cdot 10^{3}$  | $5 \cdot 10^{2}$  | $3 \cdot 10^{1}$ | $7 \cdot 10^{0}$  |
| ---------------- | ---------------- | ----------------- | ----------------- | ---------------- | ----------------- |
| $3 \cdot 10^{0}$ | $9 \cdot 10^{4}$ | $15 \cdot 10^{3}$ | $15 \cdot 10^{2}$ | $9 \cdot 10^{1}$ | $21 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
90000
15000
01500
00090
00021
```
$10^{0}$: $1 + 0 + 0 + 0 + 0 = 1$
$10^{1}$: $2 + 9 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 5 + 0 + 0 + 1 = 6$
$10^{3}$: $0 + 0 + 1 + 5 + 0 = 6$
$10^{4}$: $0 + 0 + 0 + 1 + 9 = 10$, so carry 1 to the next column.
$10^{5}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $106611$.
## Step 15
$$ \frac{-20(90000 + 15000 + 1500 + 90 + 21)(-32(12.4 + 13) + -32^3 + 3)}{10^3} \\
= \frac{-2132220(-32(12.4 + 13) + -32^3 + 3)}{10^3} \\
= 106.611(20)(-32(12.4 + 13) + -32^3 + 3)(-1) $$

Decompose $12.4$ and $13$ into place-value components.
## Step 16
```
10.0
02.0
00.4
10.0
03.0
```
$10^{-1}$: $0 + 0 + 4 + 0 + 0 = 4$
$10^{0}$: $3 + 0 + 0 + 2 + 0 = 5$
$10^{1}$: $0 + 1 + 0 + 0 + 1 = 2$
Combine the place-value columns to obtain $25.4$.
Compute $25.4 \cdot -32$ by place-value decomposition: form partial products, then add them.
Rewrite $25.4$ as an integer-scaled value times $10^{-1}$.
## Step 17
$$ 106.611(20)(-812.8 + -32^3 + 3)(-1) \\
= 106.611(20)(\frac{-8128}{10} + -32^3 + 3)(-1) \\
= 106.611(20)(\frac{(200 + 50 + 4)(-30 - 2)}{10} + -32^3 + 3)(-1) $$


**Partial-product table:**
|                   | $2 \cdot 10^{2}$  | $5 \cdot 10^{1}$   | $4 \cdot 10^{0}$   |
| ----------------- | ----------------- | ------------------ | ------------------ |
| $-3 \cdot 10^{1}$ | $-6 \cdot 10^{3}$ | $-15 \cdot 10^{2}$ | $-12 \cdot 10^{1}$ |
| $-2 \cdot 10^{0}$ | $-4 \cdot 10^{2}$ | $-1 \cdot 10^{2}$  | $-8 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
-6000
-1500
-0400
-0120
-0100
-0008
```
$10^{0}$: $-8 + 0 + 0 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 + 0 - 2 + 0 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{2}$: $0 - 1 - 1 - 4 - 5 + 0 - 1 = -12$, so borrow 2 from the next column and write 8 here.
$10^{3}$: $0 + 0 + 0 + 0 - 1 - 6 - 2 = -9$, so borrow 1 from the next column and write 1 here.
Combine the place-value columns to obtain $-8128$.
## Step 18
$$ 106.611(20)(\frac{-6000 - 1500 - 400 - 120 - 100 - 8}{10} + -32^3 + 3)(-1) \\
= 106.611(20)(-\frac{8128}{10} + -32^3 + 3)(-1) \\
= 106.611(20)(-812.8 + -32^3 + 3)(-1) $$

$$ 106.611(20)(-\frac{8128}{10} + -32^3 + 3)(-1) \\
= 106.611(20)(-812.8 + -32^3 + 3)(-1) \\
= 106.611(20)(-812.8 + -32768 + 3)(-1) $$

Compute $-32 \cdot -32$ by place-value decomposition: form partial products, then add them.
$$ 106.611(20)(-812.8 + -32^3 + 3)(-1) \\
= 106.611(20)(-812.8 + -32768 + 3)(-1) \\
= 106.611(20)(-812.8 + (-30 - 2)(-30 - 2)32(-1) + 3)(-1) $$


**Partial-product table:**
|                   | $-3 \cdot 10^{1}$ | $-2 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- |
| $-3 \cdot 10^{1}$ | $9 \cdot 10^{2}$  | $6 \cdot 10^{1}$  |
| $-2 \cdot 10^{0}$ | $6 \cdot 10^{1}$  | $4 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
900
060
060
004
```
$10^{0}$: $4 + 0 + 0 + 0 = 4$
$10^{1}$: $0 + 6 + 6 + 0 = 12$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 0 + 9 + 1 = 10$, so carry 1 to the next column.
$10^{3}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $1024$.
Compute $1024 \cdot -32$ by place-value decomposition: form partial products, then add them.
## Step 19

**Partial-product table:**
|                   | $1 \cdot 10^{3}$  | $2 \cdot 10^{1}$  | $4 \cdot 10^{0}$   |
| ----------------- | ----------------- | ----------------- | ------------------ |
| $-3 \cdot 10^{1}$ | $-3 \cdot 10^{4}$ | $-6 \cdot 10^{2}$ | $-12 \cdot 10^{1}$ |
| $-2 \cdot 10^{0}$ | $-2 \cdot 10^{3}$ | $-4 \cdot 10^{1}$ | $-8 \cdot 10^{0}$  |
**Add these partial values by place value:**
```
-30000
-00600
-02000
-00120
-00040
-00008
```
$10^{0}$: $-8 + 0 + 0 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 - 4 - 2 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{2}$: $0 + 0 - 1 + 0 - 6 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{3}$: $0 + 0 + 0 - 2 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 3 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-32768$.
Decompose $-32768$ and $3$ into place-value components.
## Step 20
```
-30000
-02000
-00700
-00060
-00008
 00003
```
$10^{0}$: $3 - 8 + 0 + 0 + 0 + 0 = -5$, so borrow 1 from the next column and write 5 here.
$10^{1}$: $0 + 0 - 6 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{2}$: $0 + 0 + 0 - 7 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{3}$: $0 + 0 + 0 + 0 - 2 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 3 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-32765$.
Decompose $-812.8000000000001$ and $-32765$ into place-value components.
## Step 21
```
-00800.0
-00010.0
-00002.0
-00000.8
-30000.0
-02000.0
-00700.0
-00060.0
-00005.0
```
$10^{-1}$: $0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{0}$: $-5 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 - 6 + 0 + 0 + 0 + 0 + 0 - 1 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{2}$: $0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 - 8 - 1 = -16$, so borrow 2 from the next column and write 4 here.
$10^{3}$: $0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 + 0 - 2 = -4$, so borrow 1 from the next column and write 6 here.
$10^{4}$: $0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
Combine the place-value columns to obtain $-33577.8$.
Compute $106.611 \cdot -20$ by place-value decomposition: form partial products, then add them.
## Step 22
Approximate $106.611$ as $106.61$ to control intermediate precision during multiplication.

Rewrite $106.61$ as an integer-scaled value times $10^{-2}$.
Rewrite $-20$ as an integer-scaled value times $10^{1}$.
## Step 23
$$ 106.61(20)(-33577.8)(-1) \\
= \frac{715945851.6}{10} \\
= \frac{-33577.8(10000 + 600 + 60 + 1)(-2)}{10} $$


**Partial-product table:**
|                   | $1 \cdot 10^{4}$  | $6 \cdot 10^{2}$   | $6 \cdot 10^{1}$   | $1 \cdot 10^{0}$  |
| ----------------- | ----------------- | ------------------ | ------------------ | ----------------- |
| $-2 \cdot 10^{0}$ | $-2 \cdot 10^{4}$ | $-12 \cdot 10^{2}$ | $-12 \cdot 10^{1}$ | $-2 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-20000
-01200
-00120
-00002
```
$10^{0}$: $-2 + 0 + 0 + 0 = -2$, so borrow 1 from the next column and write 8 here.
$10^{1}$: $0 - 2 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{2}$: $0 - 1 - 2 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{3}$: $0 + 0 - 1 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{4}$: $0 + 0 + 0 - 2 - 1 = -3$, so borrow 1 from the next column and write 7 here.
Combine the place-value columns to obtain $-21322$.
## Step 24
$$ \frac{-33577.8(-20000 - 1200 - 120 - 2)}{10} \\
= \frac{715945851.6}{10} \\
= -2132.2(33577.8)(-1) $$

Compute $-2132.2000000000003 \cdot -33577.8$ by place-value decomposition: form partial products, then add them.
## Step 25
Approximate $-33577.8$ as $-33578.0$ to control intermediate precision during multiplication.

Rewrite $-2132.2000000000003$ as an integer-scaled value times $10^{-1}$.
## Step 26
$$ -2132.2(33578)(-1) \\
= \frac{715950116}{10} \\
= \frac{(-20000 - 1000 - 300 - 20 - 2)(-30000 - 3000 - 500 - 70 - 8)}{10} $$


**Partial-product table:**
|                   | $-2 \cdot 10^{4}$ | $-1 \cdot 10^{3}$ | $-3 \cdot 10^{2}$ | $-2 \cdot 10^{1}$ | $-2 \cdot 10^{0}$ |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $-3 \cdot 10^{4}$ | $6 \cdot 10^{8}$  | $3 \cdot 10^{7}$  | $9 \cdot 10^{6}$  | $6 \cdot 10^{5}$  | $6 \cdot 10^{4}$  |
| $-3 \cdot 10^{3}$ | $6 \cdot 10^{7}$  | $3 \cdot 10^{6}$  | $9 \cdot 10^{5}$  | $6 \cdot 10^{4}$  | $6 \cdot 10^{3}$  |
| $-5 \cdot 10^{2}$ | $1 \cdot 10^{7}$  | $5 \cdot 10^{5}$  | $15 \cdot 10^{4}$ | $1 \cdot 10^{4}$  | $1 \cdot 10^{3}$  |
| $-7 \cdot 10^{1}$ | $14 \cdot 10^{5}$ | $7 \cdot 10^{4}$  | $21 \cdot 10^{3}$ | $14 \cdot 10^{2}$ | $14 \cdot 10^{1}$ |
| $-8 \cdot 10^{0}$ | $16 \cdot 10^{4}$ | $8 \cdot 10^{3}$  | $24 \cdot 10^{2}$ | $16 \cdot 10^{1}$ | $16 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
600000000
030000000
060000000
009000000
003000000
010000000
000600000
000900000
000500000
001400000
000060000
000060000
000150000
000070000
000160000
000006000
000010000
000021000
000008000
000001000
000001400
000002400
000000140
000000160
000000016
```
$10^{0}$: $6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{1}$: $1 + 6 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 11$, so carry 1 to the next column.
$10^{2}$: $0 + 1 + 1 + 4 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{3}$: $0 + 0 + 0 + 2 + 1 + 1 + 8 + 1 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 20$, so carry 2 to the next column.
$10^{4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 + 1 + 0 + 6 + 7 + 5 + 6 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 2 = 35$, so carry 3 to the next column.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 0 + 4 + 5 + 9 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 3 = 29$, so carry 2 to the next column.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 3 + 9 + 0 + 0 + 0 + 2 = 15$, so carry 1 to the next column.
$10^{7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 6 + 3 + 0 + 1 = 11$, so carry 1 to the next column.
$10^{8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 6 + 1 = 7$
Combine the place-value columns to obtain $715950116$.
## Step 27
$$ \frac{600000000 + 30000000 + 60000000 + 9000000 + 3000000 + 10000000 + 600000 + 900000 + 500000 + 1400000 + 60000 + 60000 + 150000 + 70000 + 160000 + 6000 + 10000 + 21000 + 8000 + 1000 + 1400 + 2400 + 140 + 160 + 16}{10} \\
= \frac{715950116}{10} \\
= 71595011.6 $$

$$ \frac{715950116}{10} \\
= 71595011.6 $$



---

## Case 34 (seed=17033, difficulty=beginner, guarantee_solvable=False)

- Problem: $-1(0(-6))10.4809β$
- Answer: $0$
- Solve status: `exact` | reason_code: `-` | approximate: `True`

## Step 1
Substitute the given values: $β = -18$.
$$ -1(0(-6))10.4809β \\
= -1(0(-6))10.4809β \\
= -1(0(-6))10.4809(-18) \\
= -1(0)10.4809(-18) $$

## Step 2
$$ -1(0(-6))10.4809(-18) \\
= -1(0)10.4809(-18) \\
= 0(-1)(10.4809)(-18)(-1) $$

Compute $10.4809 \cdot -18$ by place-value decomposition: form partial products, then add them.
## Step 3
Approximate $10.4809$ as $10.481$ to control intermediate precision during multiplication.

Rewrite $10.481$ as an integer-scaled value times $10^{-3}$.
## Step 4
$$ 0(-1)(10.481)(-18)(-1) \\
= \frac{0}{10^3} \\
= \frac{0}{10^3} $$


**Partial-product table:**
|                   | $1 \cdot 10^{4}$  | $4 \cdot 10^{2}$   | $8 \cdot 10^{1}$   | $1 \cdot 10^{0}$  |
| ----------------- | ----------------- | ------------------ | ------------------ | ----------------- |
| $-1 \cdot 10^{1}$ | $-1 \cdot 10^{5}$ | $-4 \cdot 10^{3}$  | $-8 \cdot 10^{2}$  | $-1 \cdot 10^{1}$ |
| $-8 \cdot 10^{0}$ | $-8 \cdot 10^{4}$ | $-32 \cdot 10^{2}$ | $-64 \cdot 10^{1}$ | $-8 \cdot 10^{0}$ |
**Add these partial values by place value:**
```
-100000
-004000
-080000
-000800
-003200
-000010
-000640
-000008
```
$10^{0}$: $-8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{1}$: $0 - 4 - 1 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{2}$: $0 - 6 + 0 - 2 - 8 + 0 + 0 + 0 - 1 = -17$, so borrow 2 from the next column and write 3 here.
$10^{3}$: $0 + 0 + 0 - 3 + 0 + 0 - 4 + 0 - 2 = -9$, so borrow 1 from the next column and write 1 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 1 = -2$, so borrow 1 from the next column and write 8 here.
Combine the place-value columns to obtain $-188658$.
## Step 5
$$ \frac{0}{10^3} \\
= \frac{0}{10^3} \\
= -188.658(0) $$

$$ \frac{0}{10^3} \\
= -188.658(0) \\
= 0 $$



---

## Case 35 (seed=17034, difficulty=intermediate, guarantee_solvable=True)

- Problem: $(\int_{0}^{5} \cos{X} \, dX)^{c} + \frac{d^{2}}{dX dc}\exp{X}$
- Answer: $-0.958924274663138^{c} + 0$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Apply the Fundamental Theorem of Calculus: evaluate the antiderivative at the bounds and subtract, $F(5) - F(0)$.

1 to any power is 1.

## Step 2
$$ (1\sin{5} - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (1(-0.958924274663138) - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (-0.958924274663138 - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} $$

## Step 3
$$ (1(-0.958924274663138) - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (-0.958924274663138 - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (-0.958924274663138 - 0)^{c} + \frac{d^{2}}{dX dc}\exp{X} $$

## Step 4
$$ (-0.958924274663138 - \sin{0})^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (-0.958924274663138 - 0)^{c} + \frac{d^{2}}{dX dc}\exp{X} \\
= (-0.958924274663138 + 0)^{c} + \frac{d^{2}}{dX dc}\exp{X} $$

Decompose $-0.9589242746631385$ and $0$ into place-value components.
## Step 5
```
-0.900000000000000
-0.050000000000000
-0.008000000000000
-0.000900000000000
-0.000020000000000
-0.000004000000000
-0.000000200000000
-0.000000070000000
-0.000000004000000
-0.000000000600000
-0.000000000060000
-0.000000000003000
-0.000000000000100
-0.000000000000030
-0.000000000000008
 0.000000000000000
```
$10^{-15}$: $0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -8$, so borrow 1 from the next column and write 2 here.
$10^{-14}$: $0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-13}$: $0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{-12}$: $0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{-11}$: $0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{-10}$: $0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{-9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{-7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{-6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{-5}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{-4}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 + 0 + 0 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{-3}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{-2}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{-1}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{0}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
Combine the place-value columns to obtain $-0.9589242746631381$.
Differentiate with respect to $X$, $c$ using the applicable differentiation rules.



---

## Case 36 (seed=17035, difficulty=advanced, guarantee_solvable=False)

- Problem: $x_d(ρ - 9) + 19 + (\frac{d}{dρ}27.4)11.7x_d - 18$
- Answer: $44.2 - 4.8ρ$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $x_d = -4.8$.
$$ x_d(ρ - 9) + 19 + (\frac{d}{dρ}27.4)11.7x_d - 18 \\
= x_d(ρ - 9) + 19 + (\frac{d}{dρ}27.4)11.7x_d - 18 \\
= -4.8(ρ - 9) + 19 + (\frac{d}{dρ}27.4)11.7(-4.8) - 18 \\
= -4.8ρ + 43.2 + 19 + (\frac{d}{dρ}27.4)11.7(-4.8) - 18 $$

## Step 2
Differentiate with respect to $ρ$ using the applicable differentiation rules.

## Step 3
$$ -4.8ρ + 43.2 + 19 + 0(11.7)(-4.8) - 18 \\
= -4.8ρ + 43.2 + 19 + 0 - 18 \\
= -4.8ρ + 43.2 + 19 - 18 $$

## Step 4
$$ -4.8ρ + 43.2 + 19 + 0 - 18 \\
= -4.8ρ + 43.2 + 19 - 18 \\
= 1 - 4.8ρ + 43.2 $$

## Step 5
$$ -4.8ρ + 43.2 + 19 - 18 \\
= 1 - 4.8ρ + 43.2 \\
= 44.2 - 4.8ρ $$



---

## Case 37 (seed=17036, difficulty=beginner, guarantee_solvable=True)

- Problem: $\pow{26, 17}$
- Answer: $1.13382732 \times 10^{24}$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

$$ \pow{26, 17} \\
= \pow{26, 17} \\
= 1133827315385150000000000 $$


---

## Case 38 (seed=17037, difficulty=intermediate, guarantee_solvable=False)

- Problem: $11.3 + -14 + d + d + v + 21 + 26 + 8 + 19 + 19 + 0.5$
- Answer: $147.8$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $d = 15.5$ and $v = 26$.
$$ 11.3 + -14 + d + d + v + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 11.3 + -14 + d + d + v + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 11.3 + -14 + 15.5 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 $$

Decompose $-14$ and $15.5$ into place-value components.
$$ 11.3 + -14 + d + d + v + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 11.3 + -14 + 15.5 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= -10 - 4 + 10 + 5 + 0.5 + 11.3 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 $$

```
-10.0
-04.0
 10.0
 05.0
 00.5
```
$10^{-1}$: $5 + 0 + 0 + 0 + 0 = 5$
$10^{0}$: $0 + 5 + 0 - 4 + 0 = 1$
Combine the place-value columns to obtain $1.5$.
$$ -10 - 4 + 10 + 5 + 0.5 + 11.3 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 1.5 + 11.3 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 47 + 1.5 + 11.3 + 15.5 + 26 + 8 + 19 + 19 + 0.5 $$

## Step 2
$$ 1.5 + 11.3 + 15.5 + 26 + 21 + 26 + 8 + 19 + 19 + 0.5 \\
= 47 + 1.5 + 11.3 + 15.5 + 26 + 8 + 19 + 19 + 0.5 \\
= 73 + 1.5 + 11.3 + 15.5 + 8 + 19 + 19 + 0.5 $$

## Step 3
$$ 47 + 1.5 + 11.3 + 15.5 + 26 + 8 + 19 + 19 + 0.5 \\
= 73 + 1.5 + 11.3 + 15.5 + 8 + 19 + 19 + 0.5 \\
= 27 + 73 + 1.5 + 11.3 + 15.5 + 19 + 0.5 $$

## Step 4
$$ 73 + 1.5 + 11.3 + 15.5 + 8 + 19 + 19 + 0.5 \\
= 27 + 73 + 1.5 + 11.3 + 15.5 + 19 + 0.5 \\
= 46 + 73 + 1.5 + 11.3 + 15.5 + 0.5 $$

Decompose $11.3$ and $1.5$ into place-value components.
## Step 5
```
10.0
01.0
00.3
01.0
00.5
```
$10^{-1}$: $5 + 0 + 3 + 0 + 0 = 8$
$10^{0}$: $0 + 1 + 0 + 1 + 0 = 2$
$10^{1}$: $0 + 0 + 0 + 0 + 1 = 1$
Combine the place-value columns to obtain $12.8$.
Decompose $12.8$ and $15.5$ into place-value components.
## Step 6
```
10.0
02.0
00.8
10.0
05.0
00.5
```
$10^{-1}$: $5 + 0 + 0 + 8 + 0 + 0 = 13$, so carry 1 to the next column.
$10^{0}$: $0 + 5 + 0 + 0 + 2 + 0 + 1 = 8$
$10^{1}$: $0 + 0 + 1 + 0 + 0 + 1 = 2$
Combine the place-value columns to obtain $28.3$.
Decompose $28.3$ and $73$ into place-value components.
## Step 7
```
20.0
08.0
00.3
70.0
03.0
```
$10^{-1}$: $0 + 0 + 3 + 0 + 0 = 3$
$10^{0}$: $3 + 0 + 0 + 8 + 0 = 11$, so carry 1 to the next column.
$10^{1}$: $0 + 7 + 0 + 0 + 2 + 1 = 10$, so carry 1 to the next column.
$10^{2}$: 1 (carry from the previous column)
Combine the place-value columns to obtain $101.3$.
Decompose $101.3$ and $46$ into place-value components.
## Step 8
```
100.0
001.0
000.3
040.0
006.0
```
$10^{-1}$: $0 + 0 + 3 + 0 + 0 = 3$
$10^{0}$: $6 + 0 + 0 + 1 + 0 = 7$
$10^{1}$: $0 + 4 + 0 + 0 + 0 = 4$
$10^{2}$: $0 + 0 + 0 + 0 + 1 = 1$
Combine the place-value columns to obtain $147.3$.
Decompose $147.3$ and $0.5$ into place-value components.
## Step 9
```
100.0
040.0
007.0
000.3
000.5
```
$10^{-1}$: $5 + 3 + 0 + 0 + 0 = 8$
$10^{0}$: $0 + 0 + 7 + 0 + 0 = 7$
$10^{1}$: $0 + 0 + 0 + 4 + 0 = 4$
$10^{2}$: $0 + 0 + 0 + 0 + 1 = 1$
Combine the place-value columns to obtain $147.8$.
$$ 100 + 40 + 7 + 0.3 + 0.5 \\
= 147.8 $$



---

## Case 39 (seed=17038, difficulty=advanced, guarantee_solvable=True)

- Problem: $14(-22^{h})25 + 14^11$
- Answer: $-2.98075162 \times 10^{41}$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

## Step 1
Substitute the given values: $h = 29$.
$$ 14(-22^{h})25 + 14^11 \\
= 14(-22^{h})25 + 14^11 \\
= 14(-22^29)(25) + 14^11 \\
= 14(-851643319086537701956194499721106030592)(25) + 14^11 $$

Compute $25 \cdot 14$ by place-value decomposition: form partial products, then add them.
## Step 2

**Partial-product table:**
|                  | $2 \cdot 10^{1}$ | $5 \cdot 10^{0}$ |
| ---------------- | ---------------- | ---------------- |
| $1 \cdot 10^{1}$ | $2 \cdot 10^{2}$ | $5 \cdot 10^{1}$ |
| $4 \cdot 10^{0}$ | $8 \cdot 10^{1}$ | $2 \cdot 10^{1}$ |
**Add these partial values by place value:**
```
200
050
080
020
```
$10^{1}$: $2 + 8 + 5 + 0 = 15$, so carry 1 to the next column.
$10^{2}$: $0 + 0 + 0 + 2 + 1 = 3$
Combine the place-value columns to obtain $350$.
Compute $350 \cdot -851643319086537701956194499721106030592$ by place-value decomposition: form partial products, then add them.
Rewrite $350$ as an integer-scaled value times $10^{1}$.
## Step 3
$$ 350(851643319086537701956194499721106030592)(-1) + 14^11 \\
= 35(-851643319086537701956194499721106030592)(10^1) + 14^11 \\
= (30 + 5)(-800000000000000000000000000000000000000 - 50000000000000000000000000000000000000 - 1000000000000000000000000000000000000 - 600000000000000000000000000000000000 - 40000000000000000000000000000000000 - 3000000000000000000000000000000000 - 300000000000000000000000000000000 - 10000000000000000000000000000000 - 9000000000000000000000000000000 - 80000000000000000000000000000 - 6000000000000000000000000000 - 500000000000000000000000000 - 30000000000000000000000000 - 7000000000000000000000000 - 700000000000000000000000 - 1000000000000000000000 - 900000000000000000000 - 50000000000000000000 - 6000000000000000000 - 100000000000000000 - 90000000000000000 - 4000000000000000 - 400000000000000 - 90000000000000 - 9000000000000 - 700000000000 - 20000000000 - 1000000000 - 100000000 - 6000000 - 30000 - 500 - 90 - 2)10^1 + 14^11 $$


**Partial-product table:**
|                    | $3 \cdot 10^{1}$    | $5 \cdot 10^{0}$    |
| ------------------ | ------------------- | ------------------- |
| $-8 \cdot 10^{38}$ | $-24 \cdot 10^{39}$ | $-4 \cdot 10^{39}$  |
| $-5 \cdot 10^{37}$ | $-15 \cdot 10^{38}$ | $-25 \cdot 10^{37}$ |
| $-1 \cdot 10^{36}$ | $-3 \cdot 10^{37}$  | $-5 \cdot 10^{36}$  |
| $-6 \cdot 10^{35}$ | $-18 \cdot 10^{36}$ | $-3 \cdot 10^{36}$  |
| $-4 \cdot 10^{34}$ | $-12 \cdot 10^{35}$ | $-2 \cdot 10^{35}$  |
| $-3 \cdot 10^{33}$ | $-9 \cdot 10^{34}$  | $-15 \cdot 10^{33}$ |
| $-3 \cdot 10^{32}$ | $-9 \cdot 10^{33}$  | $-15 \cdot 10^{32}$ |
| $-1 \cdot 10^{31}$ | $-3 \cdot 10^{32}$  | $-5 \cdot 10^{31}$  |
| $-9 \cdot 10^{30}$ | $-27 \cdot 10^{31}$ | $-45 \cdot 10^{30}$ |
| $-8 \cdot 10^{28}$ | $-24 \cdot 10^{29}$ | $-4 \cdot 10^{29}$  |
| $-6 \cdot 10^{27}$ | $-18 \cdot 10^{28}$ | $-3 \cdot 10^{28}$  |
| $-5 \cdot 10^{26}$ | $-15 \cdot 10^{27}$ | $-25 \cdot 10^{26}$ |
| $-3 \cdot 10^{25}$ | $-9 \cdot 10^{26}$  | $-15 \cdot 10^{25}$ |
| $-7 \cdot 10^{24}$ | $-21 \cdot 10^{25}$ | $-35 \cdot 10^{24}$ |
| $-7 \cdot 10^{23}$ | $-21 \cdot 10^{24}$ | $-35 \cdot 10^{23}$ |
| $-1 \cdot 10^{21}$ | $-3 \cdot 10^{22}$  | $-5 \cdot 10^{21}$  |
| $-9 \cdot 10^{20}$ | $-27 \cdot 10^{21}$ | $-45 \cdot 10^{20}$ |
| $-5 \cdot 10^{19}$ | $-15 \cdot 10^{20}$ | $-25 \cdot 10^{19}$ |
| $-6 \cdot 10^{18}$ | $-18 \cdot 10^{19}$ | $-3 \cdot 10^{19}$  |
| $-1 \cdot 10^{17}$ | $-3 \cdot 10^{18}$  | $-5 \cdot 10^{17}$  |
| $-9 \cdot 10^{16}$ | $-27 \cdot 10^{17}$ | $-45 \cdot 10^{16}$ |
| $-4 \cdot 10^{15}$ | $-12 \cdot 10^{16}$ | $-2 \cdot 10^{16}$  |
| $-4 \cdot 10^{14}$ | $-12 \cdot 10^{15}$ | $-2 \cdot 10^{15}$  |
| $-9 \cdot 10^{13}$ | $-27 \cdot 10^{14}$ | $-45 \cdot 10^{13}$ |
| $-9 \cdot 10^{12}$ | $-27 \cdot 10^{13}$ | $-45 \cdot 10^{12}$ |
| $-7 \cdot 10^{11}$ | $-21 \cdot 10^{12}$ | $-35 \cdot 10^{11}$ |
| $-2 \cdot 10^{10}$ | $-6 \cdot 10^{11}$  | $-1 \cdot 10^{11}$  |
| $-1 \cdot 10^{9}$  | $-3 \cdot 10^{10}$  | $-5 \cdot 10^{9}$   |
| $-1 \cdot 10^{8}$  | $-3 \cdot 10^{9}$   | $-5 \cdot 10^{8}$   |
| $-6 \cdot 10^{6}$  | $-18 \cdot 10^{7}$  | $-3 \cdot 10^{7}$   |
| $-3 \cdot 10^{4}$  | $-9 \cdot 10^{5}$   | $-15 \cdot 10^{4}$  |
| $-5 \cdot 10^{2}$  | $-15 \cdot 10^{3}$  | $-25 \cdot 10^{2}$  |
| $-9 \cdot 10^{1}$  | $-27 \cdot 10^{2}$  | $-45 \cdot 10^{1}$  |
| $-2 \cdot 10^{0}$  | $-6 \cdot 10^{1}$   | $-1 \cdot 10^{1}$   |
**Add these partial values by place value:**
```
-24000000000000000000000000000000000000000
-04000000000000000000000000000000000000000
-01500000000000000000000000000000000000000
-00250000000000000000000000000000000000000
-00030000000000000000000000000000000000000
-00005000000000000000000000000000000000000
-00018000000000000000000000000000000000000
-00003000000000000000000000000000000000000
-00001200000000000000000000000000000000000
-00000200000000000000000000000000000000000
-00000090000000000000000000000000000000000
-00000015000000000000000000000000000000000
-00000009000000000000000000000000000000000
-00000001500000000000000000000000000000000
-00000000300000000000000000000000000000000
-00000000050000000000000000000000000000000
-00000000270000000000000000000000000000000
-00000000045000000000000000000000000000000
-00000000002400000000000000000000000000000
-00000000000400000000000000000000000000000
-00000000000180000000000000000000000000000
-00000000000030000000000000000000000000000
-00000000000015000000000000000000000000000
-00000000000002500000000000000000000000000
-00000000000000900000000000000000000000000
-00000000000000150000000000000000000000000
-00000000000000210000000000000000000000000
-00000000000000035000000000000000000000000
-00000000000000021000000000000000000000000
-00000000000000003500000000000000000000000
-00000000000000000030000000000000000000000
-00000000000000000005000000000000000000000
-00000000000000000027000000000000000000000
-00000000000000000004500000000000000000000
-00000000000000000001500000000000000000000
-00000000000000000000250000000000000000000
-00000000000000000000180000000000000000000
-00000000000000000000030000000000000000000
-00000000000000000000003000000000000000000
-00000000000000000000000500000000000000000
-00000000000000000000002700000000000000000
-00000000000000000000000450000000000000000
-00000000000000000000000120000000000000000
-00000000000000000000000020000000000000000
-00000000000000000000000012000000000000000
-00000000000000000000000002000000000000000
-00000000000000000000000002700000000000000
-00000000000000000000000000450000000000000
-00000000000000000000000000270000000000000
-00000000000000000000000000045000000000000
-00000000000000000000000000021000000000000
-00000000000000000000000000003500000000000
-00000000000000000000000000000600000000000
-00000000000000000000000000000100000000000
-00000000000000000000000000000030000000000
-00000000000000000000000000000005000000000
-00000000000000000000000000000003000000000
-00000000000000000000000000000000500000000
-00000000000000000000000000000000180000000
-00000000000000000000000000000000030000000
-00000000000000000000000000000000000900000
-00000000000000000000000000000000000150000
-00000000000000000000000000000000000015000
-00000000000000000000000000000000000002500
-00000000000000000000000000000000000002700
-00000000000000000000000000000000000000450
-00000000000000000000000000000000000000060
-00000000000000000000000000000000000000010
```
$10^{1}$: $-1 - 6 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -12$, so borrow 2 from the next column and write 8 here.
$10^{2}$: $0 + 0 - 4 - 7 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -18$, so borrow 2 from the next column and write 2 here.
$10^{3}$: $0 + 0 + 0 - 2 - 2 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{4}$: $0 + 0 + 0 + 0 + 0 - 1 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -8$, so borrow 1 from the next column and write 2 here.
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 0 - 1 - 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -11$, so borrow 2 from the next column and write 9 here.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -2$, so borrow 1 from the next column and write 8 here.
$10^{7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -12$, so borrow 2 from the next column and write 8 here.
$10^{8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -8$, so borrow 1 from the next column and write 2 here.
$10^{9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{11}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 6 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -13$, so borrow 2 from the next column and write 7 here.
$10^{12}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 1 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{13}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 4 - 7 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -20$, so borrow 2 from the next column and write 0 here.
$10^{14}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 4 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -15$, so borrow 2 from the next column and write 5 here.
$10^{15}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 2 - 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -8$, so borrow 1 from the next column and write 2 here.
$10^{16}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 2 - 2 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -11$, so borrow 2 from the next column and write 9 here.
$10^{17}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 4 - 7 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -19$, so borrow 2 from the next column and write 1 here.
$10^{18}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -7$, so borrow 1 from the next column and write 3 here.
$10^{19}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 8 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -17$, so borrow 2 from the next column and write 3 here.
$10^{20}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 2 - 5 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -15$, so borrow 2 from the next column and write 5 here.
$10^{21}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 4 - 7 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -19$, so borrow 2 from the next column and write 1 here.
$10^{22}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -7$, so borrow 1 from the next column and write 3 here.
$10^{23}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{24}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 - 1 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{25}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 3 - 1 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -12$, so borrow 2 from the next column and write 8 here.
$10^{26}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 1 - 9 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -19$, so borrow 2 from the next column and write 1 here.
$10^{27}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -9$, so borrow 1 from the next column and write 1 here.
$10^{28}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 3 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -13$, so borrow 2 from the next column and write 7 here.
$10^{29}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 4 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{30}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -9$, so borrow 1 from the next column and write 1 here.
$10^{31}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 - 7 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -17$, so borrow 2 from the next column and write 3 here.
$10^{32}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 - 3 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -12$, so borrow 2 from the next column and write 8 here.
$10^{33}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 9 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -17$, so borrow 2 from the next column and write 3 here.
$10^{34}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -12$, so borrow 2 from the next column and write 8 here.
$10^{35}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 = -6$, so borrow 1 from the next column and write 4 here.
$10^{36}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 3 - 8 - 5 + 0 + 0 + 0 + 0 + 0 - 1 = -18$, so borrow 2 from the next column and write 2 here.
$10^{37}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 - 3 - 5 + 0 + 0 + 0 - 2 = -11$, so borrow 2 from the next column and write 9 here.
$10^{38}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 5 + 0 + 0 - 2 = -9$, so borrow 1 from the next column and write 1 here.
$10^{39}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 - 4 - 4 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{40}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 1 = -3$, so borrow 1 from the next column and write 7 here.
Combine the place-value columns to obtain $-29807516168028819568466807490238711070720$.
## Step 4
$$ (-24000000000000000000000000000000000000000 - 4000000000000000000000000000000000000000 - 1500000000000000000000000000000000000000 - 250000000000000000000000000000000000000 - 30000000000000000000000000000000000000 - 5000000000000000000000000000000000000 - 18000000000000000000000000000000000000 - 3000000000000000000000000000000000000 - 1200000000000000000000000000000000000 - 200000000000000000000000000000000000 - 90000000000000000000000000000000000 - 15000000000000000000000000000000000 - 9000000000000000000000000000000000 - 1500000000000000000000000000000000 - 300000000000000000000000000000000 - 50000000000000000000000000000000 - 270000000000000000000000000000000 - 45000000000000000000000000000000 - 2400000000000000000000000000000 - 400000000000000000000000000000 - 180000000000000000000000000000 - 30000000000000000000000000000 - 15000000000000000000000000000 - 2500000000000000000000000000 - 900000000000000000000000000 - 150000000000000000000000000 - 210000000000000000000000000 - 35000000000000000000000000 - 21000000000000000000000000 - 3500000000000000000000000 - 30000000000000000000000 - 5000000000000000000000 - 27000000000000000000000 - 4500000000000000000000 - 1500000000000000000000 - 250000000000000000000 - 180000000000000000000 - 30000000000000000000 - 3000000000000000000 - 500000000000000000 - 2700000000000000000 - 450000000000000000 - 120000000000000000 - 20000000000000000 - 12000000000000000 - 2000000000000000 - 2700000000000000 - 450000000000000 - 270000000000000 - 45000000000000 - 21000000000000 - 3500000000000 - 600000000000 - 100000000000 - 30000000000 - 5000000000 - 3000000000 - 500000000 - 180000000 - 30000000 - 900000 - 150000 - 15000 - 2500 - 2700 - 450 - 60 - 10)10^1 + 14^11 \\
= -29807516168028819568466807490238711070720(10) + 14^11 \\
= -298075161680288195684668074902387110707200 + 14^11 $$

$$ -29807516168028819568466807490238711070720(10) + 14^11 \\
= -298075161680288195684668074902387110707200 + 14^11 \\
= -298075161680288195684668074902387110707200 + 4049565169664 $$

Decompose $-298075161680288195684668074902387110707200$ and $4049565169664$ into place-value components.
## Step 5
```
-200000000000000000000000000000000000000000
-090000000000000000000000000000000000000000
-008000000000000000000000000000000000000000
-000070000000000000000000000000000000000000
-000005000000000000000000000000000000000000
-000000100000000000000000000000000000000000
-000000060000000000000000000000000000000000
-000000001000000000000000000000000000000000
-000000000600000000000000000000000000000000
-000000000080000000000000000000000000000000
-000000000000200000000000000000000000000000
-000000000000080000000000000000000000000000
-000000000000008000000000000000000000000000
-000000000000000100000000000000000000000000
-000000000000000090000000000000000000000000
-000000000000000005000000000000000000000000
-000000000000000000600000000000000000000000
-000000000000000000080000000000000000000000
-000000000000000000004000000000000000000000
-000000000000000000000600000000000000000000
-000000000000000000000060000000000000000000
-000000000000000000000008000000000000000000
-000000000000000000000000070000000000000000
-000000000000000000000000004000000000000000
-000000000000000000000000000900000000000000
-000000000000000000000000000002000000000000
-000000000000000000000000000000300000000000
-000000000000000000000000000000080000000000
-000000000000000000000000000000007000000000
-000000000000000000000000000000000100000000
-000000000000000000000000000000000010000000
-000000000000000000000000000000000000700000
-000000000000000000000000000000000000007000
-000000000000000000000000000000000000000200
 000000000000000000000000000004000000000000
 000000000000000000000000000000040000000000
 000000000000000000000000000000009000000000
 000000000000000000000000000000000500000000
 000000000000000000000000000000000060000000
 000000000000000000000000000000000005000000
 000000000000000000000000000000000000100000
 000000000000000000000000000000000000060000
 000000000000000000000000000000000000009000
 000000000000000000000000000000000000000600
 000000000000000000000000000000000000000060
 000000000000000000000000000000000000000004
```
$10^{0}$: $4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{1}$: $0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{2}$: $0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{3}$: $0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{4}$: $0 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 6$
$10^{5}$: $0 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -6$, so borrow 1 from the next column and write 4 here.
$10^{6}$: $0 + 0 + 0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = 4$
$10^{7}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 5$
$10^{8}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 4$
$10^{9}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2$
$10^{10}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -4$, so borrow 1 from the next column and write 6 here.
$10^{11}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 3 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -4$, so borrow 1 from the next column and write 6 here.
$10^{12}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = 1$
$10^{14}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = -9$, so borrow 1 from the next column and write 1 here.
$10^{15}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{16}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{17}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{18}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{19}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{20}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{21}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 4 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -5$, so borrow 1 from the next column and write 5 here.
$10^{22}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{23}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{24}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{25}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{26}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{27}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{28}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{29}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -3$, so borrow 1 from the next column and write 7 here.
$10^{30}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{31}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{32}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{33}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{34}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 6 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -7$, so borrow 1 from the next column and write 3 here.
$10^{35}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 + 0 + 0 + 0 + 0 + 0 - 1 = -2$, so borrow 1 from the next column and write 8 here.
$10^{36}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 5 + 0 + 0 + 0 + 0 - 1 = -6$, so borrow 1 from the next column and write 4 here.
$10^{37}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 7 + 0 + 0 + 0 - 1 = -8$, so borrow 1 from the next column and write 2 here.
$10^{38}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 1 = -1$, so borrow 1 from the next column and write 9 here.
$10^{39}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 8 + 0 + 0 - 1 = -9$, so borrow 1 from the next column and write 1 here.
$10^{40}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 9 + 0 - 1 = -10$, so borrow 1 from the next column and write 0 here.
$10^{41}$: $0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 - 2 - 1 = -3$, so borrow 1 from the next column and write 7 here.
Combine the place-value columns to obtain $-298075161680288195684668074898337545537536$.
$$ -200000000000000000000000000000000000000000 - 90000000000000000000000000000000000000000 - 8000000000000000000000000000000000000000 - 70000000000000000000000000000000000000 - 5000000000000000000000000000000000000 - 100000000000000000000000000000000000 - 60000000000000000000000000000000000 - 1000000000000000000000000000000000 - 600000000000000000000000000000000 - 80000000000000000000000000000000 - 200000000000000000000000000000 - 80000000000000000000000000000 - 8000000000000000000000000000 - 100000000000000000000000000 - 90000000000000000000000000 - 5000000000000000000000000 - 600000000000000000000000 - 80000000000000000000000 - 4000000000000000000000 - 600000000000000000000 - 60000000000000000000 - 8000000000000000000 - 70000000000000000 - 4000000000000000 - 900000000000000 - 2000000000000 - 300000000000 - 80000000000 - 7000000000 - 100000000 - 10000000 - 700000 - 7000 - 200 + 4000000000000 + 40000000000 + 9000000000 + 500000000 + 60000000 + 5000000 + 100000 + 60000 + 9000 + 600 + 60 + 4 \\
= -298075161680288195684668074898337545537536 $$



---

## Case 40 (seed=17039, difficulty=beginner, guarantee_solvable=False)

- Problem: $-36 + 32$
- Answer: $-4$
- Solve status: `exact` | reason_code: `-` | approximate: `False`

$$ -36 + 32 \\
= -36 + 32 \\
= -4 $$


---
