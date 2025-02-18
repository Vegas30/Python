-- UPDATE articles
-- SET search_vector = to_tsvector('russian', title ||' '|| content);

-- CREATE INDEX idx_search_vector ON articles USING GIN(search_vector);

-- SELECT title, content
-- FROM articles
-- WHERE search_vector @@ to_tsquery('russian', 'PostgreSQL | индекс');

-- SELECT *, ts_rank_cd(search_vector, to_tsquery('russian', 'PostgreSQL'))
-- FROM articles
-- ORDER BY ts_rank_cd(search_vector, to_tsquery('russian', 'PostrgreSQL'))
-- DESC;

CREATE FUNCTION update_search_vector() RETURNS TRIGGER AS $$
BEGIN
 NEW.search_vector=to_tsvector('russian', NEW.title||' '||NEW.content);
 RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER articles_search_update
BEFORE INSERT OR UPDATE ON articles
FOR EACH ROW
EXECUTE FUNCTION update_search_vector();

INSERT INTO articles (title, content) VALUES
('PostgreSQL для начинающих', 'PostgreSQL — это мощная объектно-реляционная СУБД с открытым исходным кодом, используемая для хранения и обработки данных.');
