#!/usr/bin/node
// Script that prints the addition of 2 integers

function add (a, b) {
  return (a + b);
}
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
const result = add(first, second);

console.log(result);
