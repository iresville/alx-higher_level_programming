-- list number by score
-- the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
SELECT score COUNT(*) AS NUMBER FROM second_table GROUP BY score ORDER BY score DESC;
