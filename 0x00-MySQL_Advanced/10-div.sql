-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    
    -- Check if the second number (b) is zero
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    
    RETURN result;
END //

DELIMITER ;
