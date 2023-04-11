//  1. Write a program to get the largest number from a list.
function largestNumber(numbers) {
  let largest = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      largest = numbers[i];
    }
  }
  return largest;
}

// Example usage
let numbers = [3, 7, 1, 9, 5, 4];
console.log(largestNumber(numbers));