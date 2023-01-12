--  computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE `ComputeAverageWeightedScoreForUser` (IN user_id INT)
BEGIN
DECLARE total_W, final_W INT;
SET total_W = ((SELECT SUM(`weight`) FROM projects));
SET final_W = (SELECT SUM(projects.weight * corrections.score) FROM projects
INNER JOIN corrections ON corrections.project_id = projects.id AND corrections.user_id = user_id);
UPDATE users SET users.average_score = final_W / total_W WHERE users.id = user_id;
END //
DELIMITER ;
