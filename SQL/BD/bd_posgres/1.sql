-- select * from pg_database;
-- SELECT datname FROM pg_database;
-- CREATE SCHEMA schema_name;
-- SHOW search_path;

-- CREATE TABLE IF NOT EXISTS clients (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(25) NOT NULL,
-- 	type VARCHAR(50) CHECK ( type IN ('individual','business')),
-- 	contact_info JSONB
-- );
-- -- DROP TABLE clients CASCADE;

-- CREATE TABLE IF NOT EXISTS services(
-- 	id SERIAL PRIMARY KEY,
-- 	name varchar(255) not null,
-- 	category VARCHAR(255),
-- 	price decimal(10,2) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS transactions(
-- 	id SERIAL PRIMARY KEY,
-- 	client_id INT REFERENCES clients(id),
-- 	service_id INT REFERENCES services(id),
-- 	transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	amount DECIMAL(10,2) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS employees (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(255) NOT NULL,
-- 	role VARCHAR(255),
-- 	contact_info JSONB
-- );

CREATE OR REPLACE FUNCTION calculate_amount_total(cl_id INT, start_date TIMESTAMP, end_date TIMESTAMP)
RETURNS DECIMAL AS $$
DECLARE
	total DECIMAL(10,2);
BEGIN
	SELECT SUM(amount) INTO total
	FROM transactions
	WHERE client_id = cl_id	AND transaction_date BETWEEN start_date AND end_date;

	RETURN total;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM calculate_amount_total(1, '2024-02-01 10:30:00', '2024-02-11 15:50:00');
