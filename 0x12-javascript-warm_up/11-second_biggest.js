#!/usr/bin/node
// Script to search the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const num = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
