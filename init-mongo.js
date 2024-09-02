db = db.getSiblingDB('Lottery'); // Use the 'Lottery' database

// Create collections
db.createCollection('Lottery');
db.createCollection('Ballot');
db.createCollection('User');
db.createCollection('Winner');
