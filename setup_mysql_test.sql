-- Script to prepare a MySQL server for the project

-- create a database
CREATE DATABASE if not exists hbnb_test_db;

-- create a new user
CREATE USER if not exists 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on the database hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.*  TO 'hbnb_test'@'localhost';

-- grant select privilege on the database performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.*  TO 'hbnb_test'@'localhost';
