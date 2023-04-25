#!/usr/bin/node
const _req_ = require('request');
_req_ (process.argv[2], function (_err, _resp_, body) {
  if (error) throw error;
  console.log('code:', _resp_.statusCode);
});
