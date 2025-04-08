import sqlite3

def set_user(username, email, password):
    with sqlite3.connect("data") as con:
        cur = con.cursor()
        try:
            inornot = cur.execute(f"SELECT username FROM users WHERE username='{username}'").fetchall()
            if len(inornot) == 0:
                cur.execute(
                    f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')")
                return True
            else:
                return False

        except Exception as e:
            print(e)
            print('set_user')