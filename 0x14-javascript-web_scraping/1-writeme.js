#!/usr/bin/node
const fs = require('fs');

const filePathArg = process.argv[2];
const fileContentArg = process.argv[3];

fs.writeFile(filePathArg, fileContentArg, 'utf8', (writeErr) => {
  if (writeErr) {
    console.error(writeErr);
    return;
  }
});
