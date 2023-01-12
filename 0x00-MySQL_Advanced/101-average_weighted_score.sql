--  computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE `ComputeAverageWeightedScoreForUsers` ()
BEGIN
DECLARE total_W, final_W, check_C INT;
DECLARE check_A INT DEFAULT 1;
SET total_W = ((SELECT SUM(`weight`) FROM projects));
SET check_C = (SELECT COUNT(id) FROM users);

WHILE check_A < check_C + 1 DO
    SET final_W = (SELECT SUM(projects.weight * corrections.score) FROM projects
    INNER JOIN corrections ON corrections.project_id = projects.id AND corrections.user_id = check_A);
    UPDATE users SET users.average_score = final_W / total_W WHERE users.id = check_A;
    SET check_A = check_A + 1;
    END WHILE;
END //
DELIMITER ;