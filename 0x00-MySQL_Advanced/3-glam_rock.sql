-- Task: List all bands with Glam rock as their main style, ranked by their longevity.

-- Select band names and their calculated lifespan, filtering for Glam rock and ordering by lifespan in descending order
SELECT band_name, 
       CASE 
           WHEN split IS NULL THEN 2022 - formed 
           ELSE split - formed 
       END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
