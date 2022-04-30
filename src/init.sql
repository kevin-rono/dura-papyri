CREATE DATABASE IF NOT EXISTS dura_papyri;
SHOW DATABASES;
USE dura_papyri;
CREATE TABLE IF NOT EXISTS information (
    `id` INT NOT NULL auto_increment PRIMARY KEY,
    `tm_id` INT NOT NULL,
    `wikidata_id` VARCHAR(128) NOT NULL,
    `content` VARCHAR(128) NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `subject` VARCHAR(128) NOT NULL,
    `date` VARCHAR(128) NOT NULL,
    `image_url` VARCHAR(500) NOT NULL,
    `material` VARCHAR(128) NOT NULL,
    `origin` VARCHAR(128) NOT NULL,
    `language` VARCHAR(128) NOT NULL,
    `findspot` VARCHAR(500) NOT NULL,
    `time_of_excavation` VARCHAR(128) NOT NULL,
    `image` LONGBLOB NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8;
DESCRIBE information;