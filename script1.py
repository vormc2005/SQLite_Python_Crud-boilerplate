import sqlite3


def create_table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS data(item TEXT, quantity integer, prices REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)", (item, quantity, price))
    con.commit()
    con.close()


# insert("Beer", 50, 5.5)


def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    con.close()
    return rows


def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE item=?", (item,))
    con.commit()
    con.close()


# delete('wine')

def update(quantity, price, item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute('UPDATE data SET quantity=?, prices=? WHERE item=?', (quantity, price, item))
    con.commit()
    con.close()


update(20, 10.5, 'Beer')

print(view())
