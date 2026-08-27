# Challenges Week 3

The challenges are intended for students who finish the weekly practice before the laboratory session ends and want to continue practicing the concepts covered during the week.

## 🎯 Objective

The main objective of these challenges is to provide additional practice while reinforcing the concepts covered during the current laboratory session.

The challenges are organized from easier to more difficult. Students are encouraged to choose a challenge according to their current level.

### Difficulty levels
| Level	| Description |
|--------|-------------|
|🟢 Beginner	| A small extension of the concepts covered in the regular practice.|
🟡 Intermediate	| Requires more planning and problem decomposition.|
🟠 Advanced	| Combines several operations and requires careful organization.|
🔴 Challenge	| A more complex problem intended for students looking for an additional challenge.|

## 🟢 Challenge 1 – Time Conversion

Write a complete Python program that asks the user for a number of seconds and determines the equivalent amount of hours, minutes, and seconds.

The program must display the result using the following units:

- Hours
- Minutes
- Seconds

#### Example

```
Input:
3672

Output:
Hours: 1
Minutes: 1
Seconds: 12
```
#### Requirements
- Use variables to store the values and intermediate results.
- Use integer division (//) and modulo (%).
- Do not use if, for, or while.
- Do not use functions to perform the conversion.
- Store intermediate calculations in auxiliary variables.

#### Test Case
```
Input:
7384

Output:
Hours: 2
Minutes: 3
Seconds: 4
```
## 🟡 Challenge 2 – Bill Decomposition

Write a complete Python program that asks the user for an integer amount of money and determines how many bills of each denomination are needed to represent that amount.

The available denominations are:

- $500
- $200
- $100
- $50
- $20

The program must use the maximum possible number of bills of each denomination before moving to the next denomination.

#### Example

```
Input:
1870

Output:
500: 3
200: 1
100: 1
50: 1
20: 1
Remaining: 0

```
If the amount cannot be represented exactly:

```
Input:
1865

Output:
500: 3
200: 1
100: 1
50: 1
20: 0
Remaining: 15
```

#### Requirements
- Use integer division (//) and modulo (%).
- Do not use conditional statements.
- Do not use loops.
- Do not use lists.
- Use variables to store intermediate results.
- Solve the problem using only variables and arithmetic operations.

## 🟠 Challenge 3 – Shopping Calculator

Write a complete Python program that asks the user for:

- The price of a product.
- The quantity of products purchased.
- The tax percentage.

The program must calculate and display:

- Subtotal.
- Tax amount.
- Total purchase cost.
- Average price per product.

#### Formulas

The subtotal is:

$\text{subtotal} = \text{price} \times \text{quantity}$

The tax amount is:

$\text{tax} = \text{subtotal} \times \text{tax\_percentage} / 100$

The total is:

$\text{total} = \text{subtotal} + \text{tax}$

The average price per product is:

$\text{average} = \text{total} / \text{quantity}$

#### Example

```
Input:
250
4
16

Output:
Subtotal: 1000.000
Tax: 160.000
Total: 1160.000
Average: 290.000
```

#### Requirements
- Use variables for all input values.
- Store intermediate calculations in auxiliary variables.
- Do not use conditional statements.
- Do not use loops.
- Do not use functions.
- Perform all calculations using arithmetic expressions.

## 🔴 Challenge 4 – Motion Calculator

Write a complete Python program that calculates the final position and final velocity of an object moving with constant acceleration.

The user must provide:

- Initial position **x0**
- Initial velocity **v0**
- Acceleration **a**
- Time **t**

The program must calculate the final position using:

$x = x0 + v0 × t + 1/2 × a × t²$

and the final velocity using:

$v = v0 + a × t$

The program must also calculate the distance traveled by the object.

#### Example

```
Input:
x0: 10
v0: 5
a: 2
t: 3

Output:
Final position: 34.000
Final velocity: 11.000
Distance traveled: 24.000
```

#### Requirements
- Use variables x0, v0, a, and t.
- Use auxiliary variables for intermediate calculations.
- Declare any constants that are necessary.
- Do not use conditional statements.
- Do not use loops.
- Do not use functions.
- The program must work with values provided by the user.

## 📚 Recommended Order

If you are not sure which challenge to choose, follow this order:

Regular Practice
      ↓
Challenge 1
      ↓
Challenge 2
      ↓
Challenge 3
      ↓
Challenge 4

You do not need to complete every challenge. Choose a challenge that is appropriate for your current level.

If you complete one challenge and still have time, move on to the next level.

## 💡 Recommendations

Before writing your program:

- Read the entire problem carefully.
- Identify the input values.
- Identify the required outputs.
- Determine which operations are necessary.
- Identify the intermediate results that should be stored.
- Write your solution step by step.
- Test your program using the provided test cases.
- Try additional values to make sure your program works correctly.

Remember that the goal is not only to make the program work, but also to understand how the problem can be translated into a sequence of operations.
