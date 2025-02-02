-- SHOW ENGINE InnoDB STATUS;
BEGIN;
SELECT * from tests;
COMMIT;
-- BEGIN;

-- SAVEPOINT my_savepoint_0;

-- UPDATE tests SET ball = ball - 80 WHERE idTest = 33; 

-- SAVEPOINT my_savepoint_1;

-- UPDATE tests AS t SET t.proiden = 'Нет' WHERE IDTest = 33;

-- SAVEPOINT MY_savepoint_2;

-- ROLLBACK TO SAVEPOINT MY_savepoint_0;

SHOW ENGINE InnoDB STATUS;

