[![Build Status](https://travis-ci.org/phasetwenty/generator2.svg?branch=master)](https://travis-ci.org/phasetwenty/generator2)

A web application for generating random elements for use in role-playing games.

See [the introductory docs](docs/INTRO.md) for more information.

# Development

## First time setup: API

I recommend you setup a virtualenv for development. Be sure to first install dependencies:

    generator2 $ pip install -r requirements_dev.txt

This will also install some bootstrapping scripts, including `getprops` and `initializedb`.

When running for the first time, run `initializedb`:

    generator2 $ initializedb

This will setup your database and save the file to `db.sqlite3`, a path defined in `src/server/dev.ini`.

## First time setup: Web

Run the script that generates initial props and save them:

    generator2 $ getprops > initialprops.json

This filename is hardcoded, set in `webpack.config.babel.js`.

## Running the app

First, start the API using the dev server:

    generator2 $ pserve src/server/dev.ini

Then start the webpack dev server:

    generator2 $ npm run wds

When the bundle is ready, you're all set! Just visit http://localhost:8081