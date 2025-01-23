CREATE TABLE `Books` (
	`idBooks` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ',
	`title` VARCHAR(255) DEFAULT "Без названия",
	`autor` VARCHAR(128) DEFAULT "Без автора",
	`publish_year` YEAR NOT NULL,
	`price` DECIMAL NOT NULL,
	`created_at` TIMESTAMP,
	`updated_at` TIMESTAMP,
	PRIMARY KEY(`idBooks`)
);


CREATE TABLE `Clients` (
	`id_Client` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`client_name` VARCHAR(255) NOT NULL,
	`address` TEXT(65535) NOT NULL,
	`phone_number` VARCHAR(255) NOT NULL,
	`created_at` TIMESTAMP,
	`updated_at` TIMESTAMP,
	PRIMARY KEY(`id_Client`)
);


CREATE TABLE `Order` (
	`id_order` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`order_date` DATE NOT NULL,
	`client_id` INTEGER,
	`created_at` TIMESTAMP,
	`updated_at` TIMESTAMP,
	PRIMARY KEY(`id_order`)
);


CREATE TABLE `Sales` (
	`id_sale` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`quantity` INTEGER NOT NULL,
	`book_price` DECIMAL NOT NULL,
	`total_price` DECIMAL NOT NULL,
	`book_id` INTEGER NOT NULL,
	`order_id` INTEGER NOT NULL,
	`created_at` TIMESTAMP,
	`updated_at` TIMESTAMP,
	PRIMARY KEY(`id_sale`)
);


CREATE TABLE `Genre` (
	`id_genre` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name_genre` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id_genre`)
);


CREATE TABLE `BookGenre` (
	`Book_id` INTEGER NOT NULL,
	`Genre_id` INTEGER NOT NULL,
	PRIMARY KEY(`Book_id`, `Genre_id`)
);


ALTER TABLE `BookGenre`
ADD FOREIGN KEY(`Book_id`) REFERENCES `Books`(`idBooks`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `BookGenre`
ADD FOREIGN KEY(`Genre_id`) REFERENCES `Genre`(`id_genre`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `Sales`
ADD FOREIGN KEY(`order_id`) REFERENCES `Order`(`id_order`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `Sales`
ADD FOREIGN KEY(`book_id`) REFERENCES `Books`(`idBooks`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `Clients`
ADD FOREIGN KEY(`id_Client`) REFERENCES `Order`(`client_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;