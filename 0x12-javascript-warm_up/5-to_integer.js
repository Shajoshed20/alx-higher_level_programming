#!/usr/bin/node
// Script that prints My number: <first argument converted in integer>

const args = process.argv;
const conv = Number(args[2]);

if (!isNaN(conv)) {
  console.log(`My number: ${conv}`);
} else {
  console.log('Not a number');
}
