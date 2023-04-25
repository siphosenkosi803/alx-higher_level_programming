#!/usr/bin/node
const fileSystem = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];
fileSystem.writeFile(fileName, fileContent, err => {
  if (err) console.log(err);
});
