#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
