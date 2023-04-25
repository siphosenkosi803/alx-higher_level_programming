#!/usr/bin/node
const fileSystem = require('fs');
const httpRequest = require('request');
const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];
httpRequest(sourceURL).pipe(fileSystem.createWriteStream(destinationFilePath));
