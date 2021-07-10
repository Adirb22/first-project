import sqlite3

con = sqlite3.connect('credentials.db')
cur = con.cursor()


#delete table
dropTableStatement = "DROP TABLE users"

#cur.execute(dropTableStatement)
# Create table
#cur.execute('''CREATE TABLE users (username text, password text)''')

# Insert a row of data

# Save (commit) the changes
#con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()





con.commit()

