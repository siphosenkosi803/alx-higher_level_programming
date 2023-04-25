#!/usr/bin/node
const req = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

req(API_URL + movieId, (error, response, body) => {
  if (!error) {
    const movieCharacters = JSON.parse(body).characters;
    for (const characterUrl of movieCharacters) {
      req(characterUrl, (error, response, body) => {
        if (!error) {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    }
  }
});
