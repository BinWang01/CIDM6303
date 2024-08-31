# Bin Wang

import sqlite3

db_name = "chinook.db"
with sqlite3.connect(db_name) as conn:
    sql_command = '''
                    SELECT 
                            T.Name
                            , T.Composer
                            , T.UnitPrice
                            FROM tracks T
                            INNER JOIN playlist_track PT
                            ON T.TrackId = PT.TrackId
                            WHERE PT.PlaylistId = 12
                  '''
    cursor = conn.execute(sql_command)
    for row in cursor:
        print(f"Title: {row[0]}. Composer: {row[1]}. Unit Price: {row[2]}.")
