#!/usr/bin/node

const fetch = require('node-fetch');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

async function fetchCharacters() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const filmData = await response.json();
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const charResponse = await fetch(characterUrl);
      if (!charResponse.ok) {
        throw new Error(`HTTP error! status: ${charResponse.status}`);
      }
      const characterData = await charResponse.json();
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

fetchCharacters();
