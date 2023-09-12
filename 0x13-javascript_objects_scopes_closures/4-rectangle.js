#!/usr/bin/node
// A Rectangle class that defines a rectangle (update of task 3)

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let col = '';
      for (let j = 0; j < this.width; j++) {
        col += 'X';
      }
      console.log(col);
    }
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
