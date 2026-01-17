-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server

-- create the `hbtn_0d_usa` database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

--  select the `hbtn_0d_usa` database
USE `hbtn_0d_usa`;

-- create the `states` table
CREATE TABLE IF NOT EXISTS `states` (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));
