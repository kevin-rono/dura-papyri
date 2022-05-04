CREATE DATABASE IF NOT EXISTS dura_papyri;
SHOW DATABASES;
USE dura_papyri;
CREATE TABLE IF NOT EXISTS information (
    `doc_id` INT NOT NULL auto_increment PRIMARY KEY,
    `ID` INT NOT NULL,
    `Publication` VARCHAR(256) NOT NULL,
    `Relation` VARCHAR(128) NOT NULL,
    `Language` VARCHAR(128) NOT NULL,
    `Date` VARCHAR(128) NOT NULL,
    `Provenance` VARCHAR(256) NOT NULL,
    `Findspot` VARCHAR(256) NOT NULL,
    `Season` VARCHAR(128) NOT NULL,
    `Wikidata_ID` VARCHAR(128) NOT NULL,
    `content` VARCHAR(128) NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `subject` VARCHAR(128) NOT NULL,
    `start` INT NOT NULL,
    `end` INT NOT NULL,
    `image_url` VARCHAR(500) NOT NULL,
    `image` LONGBLOB NOT NULL,
    `material` VARCHAR(128) NOT NULL,
    `origin` VARCHAR(128) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=utf8;
DESCRIBE information;

-- DROP DATABASE dura_papyri;