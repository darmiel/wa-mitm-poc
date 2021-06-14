import sqlite3
import time
from obj import PresenceInfo

create_table_presences = '''create table if not exists wa_presence (
	id integer
		constraint wa_presence_pk
			primary key autoincrement,
	update_time integer(12) not null,
	phone_number TEXT not null,
	presence text not null
);'''


def add_presence(info: PresenceInfo):
    con = sqlite3.connect('data.db')

    cur = con.cursor()
    cur.execute(create_table_presences)
    cur.execute(f'''
    INSERT INTO wa_presence 
    (update_time, phone_number, presence) VALUES 
    ({int(time.time())}, '{info.get_number()}', '{info.type}');
    ''')

    con.commit()
    con.close()
