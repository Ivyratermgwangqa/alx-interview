# 0x06. Star Wars API

## Description

This project is designed to interact with the Star Wars API to fetch and display information about Star Wars characters based on the movie ID provided as a command-line argument. The script prints all characters of a specified Star Wars movie, displaying one character name per line in the same order as the "characters" list in the /films/ endpoint.

## Requirements

- All files should be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
- Code should be semistandard compliant (rules of Standard + semicolons on top).
- You are not allowed to use `var`; use `const` or `let` instead.

## Setup

### Install Node.js

```sh
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install `semistandard`

```sh
sudo npm install semistandard --global
```

### Install `request` module

```sh
sudo npm install request --global
```

### Set `NODE_PATH`

```sh
export NODE_PATH=/usr/lib/node_modules
```

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/alx-interview.git
   cd alx-interview/0x06-starwars_api
   ```

2. Create the `0-starwars_characters.js` script:
   ```sh
   touch 0-starwars_characters.js
   chmod +x 0-starwars_characters.js
   ```

3. Add the following code to `0-starwars_characters.js`:

   ```js
   #!/usr/bin/node

   const request = require('request');

   const movieId = process.argv[2];
   if (!movieId) {
     console.error('Please provide a Movie ID');
     process.exit(1);
   }

   const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

   request(apiUrl, (error, response, body) => {
     if (error) {
       console.error(error);
       return;
     }

     if (response.statusCode !== 200) {
       console.error(`Failed to fetch data: ${response.statusCode}`);
       return;
     }

     const filmData = JSON.parse(body);
     const characters = filmData.characters;

     characters.forEach(characterUrl => {
       request(characterUrl, (charError, charResponse, charBody) => {
         if (charError) {
           console.error(charError);
           return;
         }

         if (charResponse.statusCode === 200) {
           const characterData = JSON.parse(charBody);
           console.log(characterData.name);
         }
       });
     });
   });
   ```

4. Run the script with a Movie ID as an argument:
   ```sh
   ./0-starwars_characters.js <movie_id>
   ```

   Example:
   ```sh
   ./0-starwars_characters.js 3
   ```

## Example Output

```sh
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
$
```

## Concepts Learned

- Making HTTP requests in Node.js using the `request` module.
- Interacting with RESTful APIs.
- Handling asynchronous operations with callbacks.
- Parsing and manipulating JSON data.
- Using command-line arguments in Node.js.

## Author

This project was completed by [Lerato Mgwangqa](https://github.com/ivyratermgwangqa).

## License

This project is licensed under the Alx Curriculum.
```
