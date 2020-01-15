import sqlite3

def passengerData():
    con=sqlite3.connect("passenger.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS passenger(id INTEGER PRIMARY KEY,Pno text,Pname text,PAddress text,Pmobile text,Bno text,Rname text)")
    con.commit()
    con.close()

def addPas(Pno,Pname,PAddress,Pmobile,Bno,Rname):
    con=sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO passenger VALUES(NULL,?,?,?,?,?,?)",(Pno,Pname,PAddress,Pmobile,Bno,Rname))
    con.commit()
    con.close()

def viewDat():
    con=sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM passenger")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteDat(id):
    con=sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM passenger WHERE id=?", (id,))
    con.commit()
    con.close()

def searchDat(Pno="",Pname="",PAddress="",Pmobile="",Bno="",Rname=""):
    con=sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM passenger WHERE Pno=? OR Pname=? OR PAddress=? OR Pmobile=? OR Bno=? OR Rname=?",(Pno,Pname,PAddress,Pmobile,Bno,Rname))
    rows=cur.fetchall()
    con.close()
    return rows

def datUpdate(id,Pno="",Pname="",PAddress="",Pmobile="",Bno="",Rname=""):
    con=sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("UPDATE passenger SET Pno=?, Pname=?, PAddress=?, Pmobile=?, Bno=?, Rname=? WHERE id=?",(Pno,Pname,PAddress,Pmobile,Bno,Rname,id))
    con.commit()
    con.close()
