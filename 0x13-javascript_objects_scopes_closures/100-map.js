#!/usr/bin/node
const entry = require('./100-data').list;

console.log(entry);

let new_list = entry.map((x, index) => x * index);
console.log(new_list);
