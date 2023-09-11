#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”

const x = process.argv;

if (x !== undefined) {
  console.log(x[2] + ' is ' + x[4]);
}
