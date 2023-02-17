-- lists all shows containes in the database hbtn_tvshows
-- lists all rows in a database
SELECT tv_shows.tittle, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.tittle ASC, tv_show_genres.genre_id ASC;

