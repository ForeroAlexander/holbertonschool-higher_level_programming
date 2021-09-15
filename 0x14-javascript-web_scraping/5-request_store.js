#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const filename = process.argv[3];
const url = process.argv[2];
request(url, function (error, response, body) {
  error = 0;
  response = '';
  fs.writeFile(filename, body.toString(), (error) => {
    if (error) {
      console.log(error);
    }
  });
});
