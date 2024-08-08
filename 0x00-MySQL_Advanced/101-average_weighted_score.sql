-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Change the delimiter to // for procedure definition
DELIMITER //

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary variables to hold computed values
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE cur CURSOR FOR 
        SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Open the cursor
    OPEN cur;
    
    -- Loop through all users
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the weighted sum and total weight for the current user
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
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

-- Reset the delimiter
DELIMITER ;
