#!/usr/bin/node
// Script to print a square

const string = 'X';
const args = process.argv;
const size = Number(args[2]);

if (!isNaN(size)) {
  for (let index = 0; index < size; index++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += string;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
