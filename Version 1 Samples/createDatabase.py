import sqlite3

conn = sqlite3.connect('ReviewStore.db')
c = conn.cursor()


def createDB():
    c.execute('CREATE TABLE userReviews (pid TEXT, score REAL, review TEXT)')
