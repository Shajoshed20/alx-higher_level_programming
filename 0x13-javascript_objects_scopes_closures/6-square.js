#!/usr/bin/node
/**
 * A Square class that defines a square and inherits from Square of 5-square.js
*/
const fSquare = require('./5-square');

module.exports = class Square extends fSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let col = '';
        for (let j = 0; j < this.width; j++) {
          col += 'C';
        }
        console.log(col);
      }
    }
  }
};
