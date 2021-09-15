#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charId = 18;
request(url, function (error, response, body) {
  response = '';
  error = 0;
  let count = 0;
  const result = JSON.parse(body).results;
  for (const film of result) {
    for (const character of film.characters) {
      if (character.includes(charId)) {
        count++;
      }
    }
  }
  console.log(count);
});
