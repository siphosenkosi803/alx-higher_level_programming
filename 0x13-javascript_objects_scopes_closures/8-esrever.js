#!/usr/bin/node
// returns the reversed version of a list without using reverse built-in
exports.esrever = function (list) {
  const reversedList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversedList.push(list[index]);
  }
  return reversedList;
};

