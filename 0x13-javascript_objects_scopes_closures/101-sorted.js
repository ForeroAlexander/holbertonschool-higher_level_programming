#!/usr/bin/node
/* SCript that imports a dictionary of ocurrences by user id and computes a
 * dictionary of user ids by ocurrence */

const dict = require('./101-data').dict;
const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newDict[value] === undefined) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}
console.log(newDict);
