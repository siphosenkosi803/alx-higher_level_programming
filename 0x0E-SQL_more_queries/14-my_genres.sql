-- uses the hbtn_0d_tvshoes database to list all genres of the show dexter
-- uses a database to list all rows in a table corresponding to another
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genre ON tv_genres.id = tv_ahow_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.tittle = 'Dexter'
GROUP BY name
ORDER BY name ASC;

