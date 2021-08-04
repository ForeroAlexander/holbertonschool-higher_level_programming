#!/usr/bin/node

// returns the reversed version of a list

exports.esrever = function (list) {
  const array = [];
  list.forEach(item => array.unshift(item));
  return (array);
};
