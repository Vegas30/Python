CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    search_vector TSVECTOR
);

INSERT INTO articles (title, content) VALUES
('PostgreSQL для начинающих', 'PostgreSQL — это мощная объектно-реляционная СУБД с открытым исходным кодом, используемая для хранения и обработки данных.'),
('Основы работы с SQL', 'SQL (Structured Query Language) — это язык программирования для работы с реляционными базами данных. Основы SQL включают запросы SELECT, INSERT, UPDATE, DELETE.'),
('Что такое индексирование?', 'Индексирование в PostgreSQL ускоряет поиск данных в таблицах, позволяя уменьшить время выполнения запросов.'),
('Рекурсивные запросы в PostgreSQL', 'Рекурсивные запросы полезны для работы с иерархическими данными и могут быть реализованы с помощью CTE (Common Table Expressions).');