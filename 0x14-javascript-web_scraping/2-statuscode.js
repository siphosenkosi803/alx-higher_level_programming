#!/usr/bin/node
const httpRequest = require('request');
const url = process.argv[2];
httpRequest.get(url).on('response', function (httpResponse) {
  console.log(`code: ${httpResponse.statusCode}`);
});
