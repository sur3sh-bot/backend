// server.js

const express = require('express');   // import Express
const app = express();                // create an app

app.use(express.json());              // tell Express to understand JSON

// A simple "hello world" route
app.get('/', (req, res) => {
  res.send('Notes API is running!');
});

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});