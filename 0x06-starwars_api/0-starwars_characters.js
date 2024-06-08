#!/usr/bin/node

const request = require('request');
const util = require('util');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
const requestPromise = util.promisify(request);

async function fetchCharacters() {
  try {
    const response = await requestPromise(apiUrl);
    const filmData = JSON.parse(response.body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const charResponse = await requestPromise(characterUrl);
      const characterData = JSON.parse(charResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

fetchCharacters();
