-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT m.title "title", g.id "genre_id" FROM tv_shows m, tv_genres g, tv_show_genres sg WHERE sg.genre_id = g.id AND sg.show_id = m.id ORDER BY m.title, g.id;
