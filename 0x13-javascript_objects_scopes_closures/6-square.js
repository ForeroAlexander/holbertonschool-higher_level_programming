#!/usr/bin/node
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    let char = 'X';
    if (c !== undefined) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.height));
    }
  }
};
