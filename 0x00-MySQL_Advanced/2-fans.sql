-- Task: Rank the country origins of bands by the total number of (non-unique) fans, ordered by the number of fans.

-- Select the origin and total number of fans, then order by the number of fans in descending order
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
