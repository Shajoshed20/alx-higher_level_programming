#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
