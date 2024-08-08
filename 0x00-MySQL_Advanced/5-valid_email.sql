-- Create a trigger that resets valid_email if the email is changed
DELIMITER //

CREATE TRIGGER before_update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being changed
    IF NEW.email <> OLD.email THEN
        -- Reset valid_email to 0 if the email is changed
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
