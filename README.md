# Divide the elements of array

A program to split a 1-dimensional array (list) into two separate arrays (halves).

## 📝 Description

This program takes a single 1-dimensional array of integers and divides it into two new arrays. The split is made at the midpoint of the original array. If the original array has an odd number of elements, the extra element is included in the first new array.

-----

## 🎯 Problem Statement

### Input:

  * A single 1-dimensional array (list) of integers.

### Output:

  * The first half of the array on one line.
  * The second half of the array on a second line.
  * An error message if the validation rules are not met.

### Rules:

1.  **Validation 1 (Type):** The input list must contain *only* integers. If any non-integer element (like a string) is found, output: "Cannot determine, as there is a list."
2.  **Validation 2 (Size):** The input list must contain a minimum of 2 elements. If the list has 0 or 1 element, output: "Cannot determine, the minimum size of the array must be 2."
3.  **Splitting (Even):** If the array has an even number of elements, it is split into two equal halves.
4.  **Splitting (Odd):** If the array has an odd number of elements, the middle element is included in the *first* half. (e.g., a size 5 array is split into 3 and 2 elements).

-----

## 💡 Examples

### Example 1 (Even Size)

**Input:**

```
[10, 20, 30, 40, 50, 60]
```

**Output:**

```
[10, 20, 30]
[40, 50, 60]
```

**Explanation:** The 6-element array is split into two 3-element arrays.

### Example 2 (Odd Size)

**Input:**

```
[10, 5, 1]
```

**Output:**

```
[10, 5]
[1]
```

**Explanation:** The 3-element array is split into a 2-element array and a 1-element array. The first half gets the extra element.

### Example 3 (Sample 3)

**Input:**

```
[10, 10]
```

**Output:**

```
[10]
[10]
```

**Explanation:** The 2-element array is split into two 1-element arrays.

### Example 4 (Type Validation)

**Input:**

```
[10, "a", 2]
```

**Output:**

```
Cannot determine, as there is a list.
```

**Explanation:** The list contains a non-integer (a string "a").

### Example 5 (Size Validation)

**Input:**

```
[10]
```

**Output:**

```
Cannot determine, the minimum size of the array must be 2.
```

**Explanation:** The list does not meet the minimum size requirement of 2 elements.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/array-splitter.git
    cd array-splitter
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter the array in list format (e.g., `[1, 4, 5, 6]`) when prompted to see the result.
