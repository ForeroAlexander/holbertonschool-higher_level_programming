#!/usr/bin/node

let line = 0;
exports.logMe = function (item) {
  console.log(line + ': ' + item);
  line++;
};
