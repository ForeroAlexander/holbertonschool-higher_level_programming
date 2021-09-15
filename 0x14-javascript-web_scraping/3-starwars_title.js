#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request.get(url, function (error, response, body) {
  error = 0;
  response = '';
  const data = JSON.parse(body);
  console.log(data.title);
});
