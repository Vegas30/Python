-- CREATE TABLE flowers (
-- 	flower_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL, 
-- 	price NUMERIC(8, 2) CHECK (price > 0),
-- 	quantity INTEGER CHECK (quantity >= 0),
-- 	image_path VARCHAR(255),
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE clients (
-- 	client_id SERIAL PRIMARY KEY,
-- 	full_name VARCHAR(100) NOT NULL, 
-- 	phone VARCHAR(20) UNIQUE,
-- 	email VARCHAR(100) UNIQUE,
-- 	registration_date DATE DEFAULT CURRENT_DATE
-- );

-- CREATE TABLE orders (
-- 	order_id SERIAL PRIMARY KEY,
-- 	client_id INTEGER REFERENCES clients(client_id)
-- 	ON DELETE CASCADE,
-- 	status VARCHAR(20) CHECK (status IN 
-- 	('Новый', 'В обработке', 'Выполнен', 'Отменен')),
-- 	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE order_items(
-- 	item_id SERIAL PRIMARY KEY,
-- 	order_id INTEGER REFERENCES orders(order_id)
-- 	ON DELETE CASCADE,
-- 	flower_id INTEGER REFERENCES flowers(flower_id)
-- 	ON DELETE CASCADE,
-- 	quantity INTEGER CHECK (quantity > 0)
-- );

-- -- Цветы
-- INSERT INTO flowers (name, price, quantity, image_path) VALUES
-- ('Роза', 15.99, 50, '/images/rose.jpg'),
-- ('Тюльпан', 8.50, 100, '/images/tulip.jpg'),
-- ('Лилии', 12.30, 30, '/images/lily.jpg'),
-- ('Герберы', 10.00, 45, '/images/gerbera.jpg'),
-- ('Орхидеи', 25.75, 20, '/images/orchid.jpg'),
-- ('Пионы', 18.40, 35, '/images/peony.jpg'),
-- ('Гвоздики', 7.90, 60, '/images/carnation.jpg'),
-- ('Хризантемы', 9.99, 55, '/images/chrysanthemum.jpg'),
-- ('Ирисы', 11.20, 40, '/images/iris.jpg'),
-- ('Гиацинты', 13.45, 25, '/images/hyacinth.jpg');

-- -- Клиенты
-- INSERT INTO clients (full_name, phone, email) VALUES
-- ('Иван Петров', '+79161234567', 'ivan@mail.com'),
-- ('Мария Сидорова', '+79035556677', 'maria@mail.com'),
-- ('Алексей Иванов', '+79219876543', 'alex@mail.com'),
-- ('Ольга Кузнецова', '+79167778899', 'olga@mail.com'),
-- ('Дмитрий Смирнов', '+79034443322', 'dmitry@mail.com'),
-- ('Анна Воробьева', '+79169998877', 'anna@mail.com'),
-- ('Сергей Козлов', '+79031112233', 'sergey@mail.com'),
-- ('Елена Новикова', '+79163334455', 'elena@mail.com'),
-- ('Павел Морозов', '+79037776655', 'pavel@mail.com'),
-- ('Татьяна Павлова', '+79160001122', 'tatyana@mail.com');

-- -- Заказы
-- INSERT INTO orders (client_id, status) VALUES
-- (1, 'Новый'),
-- (2, 'Выполнен'),
-- (3, 'Выполнен'),
-- (4, 'В обработке'),
-- (5, 'Отменен'),
-- (6, 'Отменен'),
-- (7, 'Новый'),
-- (8, 'Новый'),
-- (9, 'Новый'),
-- (10, 'Новый');

-- -- Состав заказа
-- INSERT INTO order_items (order_id, flower_id, quantity) VALUES
-- (1, 1, 5),
-- (1, 2, 10),
-- (2, 3, 3),
-- (3, 4, 7),
-- (4, 5, 2),
-- (5, 6, 4),
-- (6, 7, 8),
-- (7, 8, 6),
-- (8, 9, 1),
-- (9, 10, 9);
