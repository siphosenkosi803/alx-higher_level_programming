#!/usr/bin/node

const httpRequest = require('request');
const url = process.argv[2];

httpRequest(url, function (error, httpResponse, body) {
  if (error) {
    console.log(error);
  } else if (httpResponse.statusCode === 200) {
    const completedTasksByUser = {};
    const tasks = JSON.parse(body);
    for (const index in tasks) {
      const task = tasks[index];
      if (task.completed === true) {
        if (completedTasksByUser[task.userId] === undefined) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    }
    console.log(completedTasksByUser);
  } else {
    console.log('Error. StatuS: ' + httpResponse.statusCode);
  }
});
