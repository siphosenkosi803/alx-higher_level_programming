#!/usr/bin/node
const httpRequest = require('request');
const url = process.argv[2];
httpRequest(url, function (error, httpResponse, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    console.log(movies.reduce((count, movie) => {
      return movie.characters.find((characterUrl) => characterUrl.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
