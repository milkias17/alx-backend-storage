-- if the second number is equal to 0

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE
  FUNCTION SafeDiv (a INT, b INT)
  RETURNS FLOAT
  READS SQL DATA
  DETERMINISTIC
  BEGIN
    IF b = 0
    THEN
      RETURN 0;
    ELSE
      RETURN a/b;
    END IF;
  END //
DELIMITER ;