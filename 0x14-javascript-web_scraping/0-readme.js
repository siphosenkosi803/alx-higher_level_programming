#!/usr/bin/node
const _f_s_ = require('fs');
const _read_f = process.argv[2];

_f_s_.readFile(_read_f, 'utf8', (error, _f_Content_) => {
  if (error) {
    console.error(error);
  } else {
    console.log(_f_Content_);
  }
});

