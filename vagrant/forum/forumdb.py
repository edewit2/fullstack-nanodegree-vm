#
# Database access functions for the web forum.
# 

import psycopg2
import bleach

## Database connection
DBNAME = "forum"

## Get posts from database.
def GetAllPosts():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = ({'content': str(bleach.clean(str(row[1]))), 'time': str(bleach.clean(str(row[0])))}
             for row in c.fetchall())
  db.close()
  return posts

## Add a post to the database.
def AddPost(content):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (content,))
  db.commit()
  db.close()
