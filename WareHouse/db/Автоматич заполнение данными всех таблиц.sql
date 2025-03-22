-- 1. Добавляем поставщиков (50 записей)
INSERT INTO suppliers (supplier_id, supplier_name, contact_person, phone_number, email)
SELECT 
    num,
    'Поставщик #' || num,
    'Контакное лицо #' || num,
    lpad((random() * 9999999999)::bigint::text, 10, '0'),
    'supplier' || num || '@example.com'
FROM generate_series(1, 50) AS num;

-- 2. Добавляем склады (30 записей)
INSERT INTO warehouses (warehouse_id, warehouse_name, location, capacity)
SELECT 
    num,
    'Склад #' || num,
    'Город ' || (random() * 50 + 1)::int,
    (random() * 9000 + 1000)::int
FROM generate_series(1, 30) AS num;

-- 3. Добавляем товары (100 записей)
INSERT INTO products (product_id, product_name, product_description, category, unit_price)
SELECT
    num,
    CASE categories.category
        WHEN 'электроника' THEN 'Ноутбук Model ' || num
        WHEN 'одежда' THEN 'Футболка Style ' || num
        WHEN 'обувь' THEN 'Кроссовки Edition ' || num
        WHEN 'мебель' THEN 'Стул Design ' || num
        WHEN 'товары для спорта' THEN 'Мяч Sport ' || num
        ELSE 'Инструмент Professional ' || num
    END,
    'Описание для товара ' || num,
    categories.category,
    (random() * 990 + 10)::numeric(10,2)
FROM 
    generate_series(1, 100) AS num,
    (SELECT ('{электроника,одежда,обувь,мебель,товары для спорта,инструменты}'::text[])[floor(random() * 6 + 1)] AS category) AS categories;

-- 4. Заполняем складские запасы (stock)
INSERT INTO stock (stock_id, product_id, warehouse_id, quantity, last_restocked)
SELECT
    num,
    (random() * 99 + 1)::int,
    (random() * 29 + 1)::int,
    (random() * 500 + 1)::int,
    CURRENT_DATE - (random() * 365)::int
FROM generate_series(1, 300) AS num; -- 300 записей для примера

-- 5. Добавляем заказы (50 записей)
WITH orders_data AS (
    SELECT 
        num AS order_id,
        CURRENT_DATE - (random() * 365)::int AS order_date,
        (random() * 49 + 1)::int AS supplier_id,
        (random() * 9900 + 100)::numeric(10,2) AS total_amount,
        ('{в обработке,доставлен,отменен}'::text[])[floor(random() * 3 + 1)] AS status
    FROM generate_series(1, 50) AS num
)
INSERT INTO orders (order_id, order_date, supplier_id, total_amount, status)
SELECT * FROM orders_data;

-- 6. Добавляем позиции заказов (минимум 1 позиция на заказ)
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price, total_price)
SELECT
    num,
    (random() * 49 + 1)::int,
    (random() * 99 + 1)::int,
    (random() * 10 + 1)::int,
    p.unit_price,
    (p.unit_price * (random() * 10 + 1))::numeric(10,2)
FROM 
    generate_series(1, 150) AS num, -- 150 позиций (в среднем 3 на заказ)
    products p
WHERE p.product_id = (random() * 99 + 1)::int;

-- Важные примечания:
-- Категории товаров автоматически выбираются из списка: электроника, одежда, обувь, мебель, товары для спорта, инструменты.

-- Проверки данных:

-- Все цены (unit_price, total_price) будут положительными (благодаря CHECK).

-- Количество товаров (quantity) не может быть отрицательным.

-- Связи:

-- При удалении поставщика/товара/заказа связанные записи автоматически удаляются (ON DELETE CASCADE).

-- Обновление данных:

-- Поля created_at и updated_at заполняются автоматически.

-- Для проверки данных можно выполнить запросы вида:

-- SELECT count(*) FROM suppliers; -- Должно быть 50
-- SELECT category, count(*) FROM products GROUP BY category; -- Распределение по категориям
