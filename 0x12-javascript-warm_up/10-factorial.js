#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (a) {
    if (isNaN(a)) {
        return (1);
    } else if (a === 0) {
        return (1);
    } else {
        return (a * factorial(a - 1));
    }
}

const args = parseInt(process.argv[2]);
const result = factorial(args);

console.log(result);
