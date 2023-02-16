-- Grant privileges in my sql server
-- Create a user user_0d_1@localhost
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
		IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privilleges to user_0d_1@localhost
GRANT ALL PRIVILEGES
		ON *.*
		TO 'user_0d_1'@'localhost';

