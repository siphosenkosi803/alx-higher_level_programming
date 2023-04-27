#!/usr/bin/node
const httpRequest = require('request');
const episodeNumber = process.argv[2];
const apiURL = 'https://swapi-api.hbtn.io/api/films/';
httpRequest(apiURL + episodeNumber, function (error, httpResponse, body) {
  if (error) {
    console.log(error);
  } else if (httpResponse.statusCode === 200) {
    const responseBody = JSON.parse(body);
    console.log(responseBody.title);
  } else {
    console.log('Error code: ' + httpResponse.statusCode);
  }
});
