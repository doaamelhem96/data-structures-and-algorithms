

1. Initial array: `[8, 4, 23, 42, 16, 15]`

2. Split the array into two halves:
   - Left side: `[8, 4, 23]`
   - Right side: `[42, 16, 15]`

3. Recursive call to sort the left side:
   - Left side: `[8]`
   - Right side: `[4, 23]`
   - Merge the sorted left and right sides: `[4, 8, 23]`

4. Recursive call to sort the right side:
   - Left side: `[42]`
   - Right side: `[16, 15]`
   - Recursive call to sort the right side:
     - Left side: `[16]`
     - Right side: `[15]`
     - Merge the sorted left and right sides: `[15, 16]`
   - Merge the sorted left and right sides: `[15, 16, 42]`

5. Merge the sorted left and right sides of the original array:
   - Left side: `[4, 8, 23]`
   - Right side: `[15, 16, 42]`
   - Merge the sorted left and right sides: `[4, 8, 15, 16, 23, 42]`

The final sorted array is `[4, 8, 15, 16, 23, 42]`.

efficiency :
time >> o(nlog(n))
space >> O(n)