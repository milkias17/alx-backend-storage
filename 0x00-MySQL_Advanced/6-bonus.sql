-- Creating Procedures

DELIMITER //
CREATE PROCEDURE `AddBonus` (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
DECLARE try1, p_id INT;
SET try1 = (SELECT project_name IN (SELECT name FROM projects));
IF try1 = 0 THEN
	INSERT INTO projects(name) VALUES(project_name);
END IF;
SET p_id = (SELECT id FROM projects WHERE name = project_name);
INSERT INTO corrections(user_id, project_id, score) VALUE(user_id, p_id, score);
END //
DELIMITER ;