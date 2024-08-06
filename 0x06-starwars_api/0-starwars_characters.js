#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
request(
  `https://swapi-api.alx-tools.com/api/films/${arg}`,
  (err, res, body) => {
    if (err) {
      return;
    }
    const urls = JSON.parse(body).characters;
    const names = urls.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, json) => {
          if (err) {
            reject(new Error());
          } else {
            resolve(JSON.parse(json).name);
          }
        });
      });
    });
    Promise.all(names).then((res) => {
      for (const name of res) {
        console.log(name);
      }
    });
  }
);
