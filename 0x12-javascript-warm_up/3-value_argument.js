#!/usr/bin/node
// Script that prints the first argument passed to it

let x = process.argv;

if (x[2] !== undefined) {
  console.log(x[2]);
} else {
  console.log('No argument');
}
