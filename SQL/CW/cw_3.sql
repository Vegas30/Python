
-- SELECT b.title, b.author, b.publish_year
-- FROM books AS b
-- JOIN bookgenre ON id = book_id
-- JOIN genres ON genre_id = genres.id
-- WHERE genres.name = "Historical Fiction";

-- SELECT client_name, address, phone_number, clients.created_at, order_date
-- FROM clients
-- JOIN orders ON clients.id = client_id
-- WHERE order_date BETWEEN '2024-06-03' AND '2025-01-01';

-- SELECT books.title, books.author, SUM(sales.quantity) AS total_sold
-- FROM books
-- JOIN sales ON books.id = book_id
-- GROUP BY books.title, books.author
-- HAVING total_sold > 3;

-- SELECT title, author, price 
-- FROM books
-- WHERE price > (SELECT AVG(price) FROM books); ???