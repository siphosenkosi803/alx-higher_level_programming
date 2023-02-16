-- Create database and user in MYSQL server
-- Create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
-- Creates user user_0d_2@localhost
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
		IDENTIFIED BY 'user_0d_2_pwd';
-- Grant privileges to the user
GRANT SELECT
	ON 'hbtn_0d_2'.*
	TO 'user_0d_2'@'localhost';

