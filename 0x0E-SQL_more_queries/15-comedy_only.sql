-- lists all comedy shows in the database hbtn_0d_tvshows
-- lists all rows of a database corresponding to a column value
SELECT tittle
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY tittle
ORDER BY tittle ASC;

