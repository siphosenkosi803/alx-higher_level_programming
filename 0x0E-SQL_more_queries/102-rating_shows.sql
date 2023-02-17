-- lists al shows from hbt_0d_tvshows_rate by their rating
-- lists all roes of a table by the sum of a linked row
SELECT tittle, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tittle
ORDER BY rating DESC;

