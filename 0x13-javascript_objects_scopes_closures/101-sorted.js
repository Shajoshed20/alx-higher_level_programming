#!/usr/bin/node

const entry = require('./101-data').dict;

const newDict = {};

for (const key in entry) {
  if (newDict[entry[key]] === undefined) {
    newDict[entry[key]] = [key];
  } else {
    newDict[entry[key]].push(key);
  }
}

console.log(newDict);
