-- Task: Create a 'users' table with an auto-incrementing primary key, unique email, and optional name field.
-- The script ensures the table is created only if it doesn't already exist.

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,  -- Primary key with auto-incrementing integer values
    email VARCHAR(255) NOT NULL UNIQUE,  -- Unique and non-null email address
    name VARCHAR(255),  -- Optional name field
    PRIMARY KEY (id)  -- Define the primary key on the 'id' column
);
