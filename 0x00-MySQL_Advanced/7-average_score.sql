-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = user_id
    );
    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = user_id;
END //
DELIMITER ;
