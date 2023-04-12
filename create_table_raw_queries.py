import sqlite3

conn = sqlite3.connect('instance/meter_data.db', check_same_thread=False)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS meters
             (id INTEGER PRIMARY KEY, label TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS meter_data
             (id INTEGER PRIMARY KEY, meter_id INTEGER, timestamp TEXT, value INTEGER,
              FOREIGN KEY(meter_id) REFERENCES meters(id))''')
conn.commit()




# c.execute("INSERT INTO meters (label) VALUES ('Meter 1')")
# c.execute("INSERT INTO meters (label) VALUES ('Meter 2')")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (1, '2022-01-01 12:00:00', 100)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (1, '2022-01-02 12:00:00', 200)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (2, '2022-01-01 12:00:00', 300)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (2, '2022-01-02 12:00:00', 400)")
# conn.commit()
