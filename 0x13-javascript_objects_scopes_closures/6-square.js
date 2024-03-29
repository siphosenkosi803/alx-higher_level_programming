#!/usr/bin/node
// class that defines a square and inherits from Square
const Ssquare = require('./5-square');

class Square extends Ssquare {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

