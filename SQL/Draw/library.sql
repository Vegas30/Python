CREATE TABLE `Books` (
    `id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ таблицы книг',
    `title` VARCHAR(255) DEFAULT "Без названия" COMMENT 'Название книги',
    `author` VARCHAR(128) DEFAULT "Без автора" COMMENT 'Автор книги',
    `publish_year` YEAR NOT NULL COMMENT 'Год публикации книги',
    `price` DECIMAL(10, 2) NOT NULL COMMENT 'Цена книги',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания записи',
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время последнего обновления записи',
    PRIMARY KEY (`id`),
    UNIQUE (`title`, `author`, `publish_year`) COMMENT 'Уникальное ограничение для предотвращения дублирования книг'
);

CREATE TABLE `Clients` (
    `id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ таблицы клиентов',
    `client_name` VARCHAR(255) NOT NULL COMMENT 'Имя клиента',
    `address` TEXT NOT NULL COMMENT 'Адрес клиента',
    `phone_number` VARCHAR(15) NOT NULL COMMENT 'Номер телефона клиента',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания записи',
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время последнего обновления записи',
    PRIMARY KEY (`id`),
    UNIQUE (`phone_number`) COMMENT 'Уникальное ограничение для предотвращения дублирования номеров телефонов'
);

CREATE TABLE `Orders` (
    `id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ таблицы заказов',
    `order_date` DATE NOT NULL COMMENT 'Дата оформления заказа',
    `client_id` INTEGER NOT NULL COMMENT 'ID клиента, оформившего заказ',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания записи',
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время последнего обновления записи',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`client_id`) REFERENCES `Clients`(`id`)
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `Sales` (
    `id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ таблицы продаж',
    `quantity` INTEGER NOT NULL CHECK (`quantity` > 0) COMMENT 'Количество проданных книг (должно быть больше 0)',
    `book_price` DECIMAL(10, 2) NOT NULL COMMENT 'Цена книги на момент продажи',
    `total_price` DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * book_price) STORED COMMENT 'Общая стоимость продажи (рассчитывается автоматически)',
    `order_id` INTEGER NOT NULL COMMENT 'ID связанного заказа',
    `book_id` INTEGER NOT NULL COMMENT 'ID проданной книги',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания записи',
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время последнего обновления записи',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`order_id`) REFERENCES `Orders`(`id`)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`book_id`) REFERENCES `Books`(`id`)
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `Genres` (
    `id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'Первичный ключ таблицы жанров',
    `name` VARCHAR(255) NOT NULL COMMENT 'Название жанра',
    PRIMARY KEY (`id`)
);

CREATE TABLE `BookGenre` (
    `book_id` INTEGER NOT NULL COMMENT 'ID книги',
    `genre_id` INTEGER NOT NULL COMMENT 'ID жанра',
    PRIMARY KEY (`book_id`, `genre_id`) COMMENT 'Составной первичный ключ для предотвращения дублирования связей',
    FOREIGN KEY (`book_id`) REFERENCES `Books`(`id`)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`genre_id`) REFERENCES `Genres`(`id`)
    ON UPDATE CASCADE ON DELETE CASCADE
);
