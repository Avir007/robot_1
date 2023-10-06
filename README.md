## Robot_1

### Approach to Problem

* **Identify the needs**
* We basically need to implement 3 things:
  1. When to not move (Breaching condition)
  2. When to move with direction (move function)
  3. Iterate through str

### Responsibilities of Each Function

1. **Breaching Function:** This function checks whether our coordinates lie inside the given grid.
2. **Move Function:** This function helps to move the cursor according to the given direction by one unit.
3. **Main:** Inside the main function, we iterate over each letter of the word, check for movement and breaking conditions, and update accordingly.
