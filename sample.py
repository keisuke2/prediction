    #DBの呼び出し
    import MySQLdb

    if __name__ == "__main__":

      connector = MySQLdb.connect(host="10.0.1.75", db="jobhunt", user="jobhunt", passwd="jobhuntpasswd", charset="utf8")
      cursor = connector.cursor()

      sql = "select name from users"
      #sql2 = "INSERT INTO users (id, name) VALUES (5,3)"
      #sql2 ="INSERT INTO jobhunt.users (id, name) VALUES (2,2)"
      cursor.execute(sql)
      records = cursor.fetchall()
      for record in records:
          print (record[0])
      cursor.close()
      connector.close()
      #tst
      print('インサート完了')
