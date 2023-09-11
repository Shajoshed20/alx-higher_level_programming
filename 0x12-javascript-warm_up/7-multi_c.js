#!/usr/bin/node
// Script to prints x times “C is fun”

const string = 'C is fun';
const args = process.argv;
const conv = Number(args[2]);

if (!isNaN(conv)) {
  for (let index = 0; index < conv; index++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
