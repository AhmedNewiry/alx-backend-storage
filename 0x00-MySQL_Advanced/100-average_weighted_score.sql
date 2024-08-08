-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Change the delimiter to // for procedure definition
DELIMITER //

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;

    -- Calculate the weighted sum and total weight
    SET weighted_sum = (
        SELECT SUM(C.score * P.weight)
        FROM corrections C
        JOIN projects P ON C.project_id = P.id
        WHERE C.user_id = user_id
    );

    SET total_weight = (
        SELECT SUM(P.weight)
        FROM corrections C
        JOIN projects P ON C.project_id = P.id
        WHERE C.user_id = user_id
    );

    -- Calculate and update the average weighted score
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = weighted_sum / total_weight
        WHERE id = user_id;
    ELSE
        -- If total_weight is 0, set average_score to 0
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END //

-- Reset the delimiter
DELIMITER ;
