#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  const dict = {};
  for (const userd of json) {
    const saveId = userd.userId;
    if (userd.completed) {
      if (dict[saveId]) {
        dict[saveId]++;
      } else {
        dict[saveId] = 1;
      }
    }
  }
  console.log(dict);
});
