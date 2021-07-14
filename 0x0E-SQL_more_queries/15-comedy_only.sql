-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT m.title 
FROM tv_shows m
JOIN tv_show_genres sg
	ON sg.show_id = m.id
JOIN tv_genres g
	ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY m.title;
