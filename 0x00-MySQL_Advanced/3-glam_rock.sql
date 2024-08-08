-- Drop the view if it exists
DROP VIEW IF EXISTS glam_rock_bands;

-- Create a view to list all bands with Glam rock as their main style, ranked by longevity
CREATE VIEW glam_rock_bands AS
SELECT 
    band_name,
    (2022 - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    main_style = 'Glam rock'
ORDER BY 
    lifespan DESC;

-- Select from the view to see the results
SELECT * FROM glam_rock_bands;
