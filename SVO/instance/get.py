import sqlite3


def get_password(email):
    try:
        with sqlite3.connect("data") as con:
            cur = con.cursor()
            f1 = cur.execute(f"SELECT password FROM users WHERE username='{email}'").fetchall()
            f2 = cur.execute(f"SELECT password FROM users WHERE email='{email}'").fetchall()
            if f1:
                return f1[0][0]
            elif f2:
                return f2[0][0]
            else:
                return None
    except Exception as s:
        print(s)
        print('get_user')
        return False
