#!/usr/bin/node
const request = require('request');
const _apiUrl_ = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(apiUrl, function (err, response, body) {
  if (!err) {
    const charactersList = JSON.parse(body).characters;
    printCharacters(charactersList, 0);
  }
});

function printCharacters(charactersList, index) {
  request(charactersList[index], function (err, response, body) {
    if (!err) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      if (index + 1 < charactersList.length) {
        printCharacters(charactersList, index + 1);
      }
    }
  });
}
