-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to // for procedure definition
DELIMITER //

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    -- Variable to hold the average score
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the given user
    SET avg_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = user_id
    );

    -- Update the average_score field in the users table
    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = user_id;
END //

-- Reset the delimiter
DELIMITER ;
