#!/usr/bin/node
// 
const _f_s_ = require('fs');
_f_s_.writeFile(process.argv[2], process.argv[3], 'utf8', function (error) {
  if (err) {
    console.log(error);
  }
}
);
