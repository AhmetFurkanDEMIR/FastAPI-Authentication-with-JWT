from app.db.db import db

cursor, conn = db()

def addPost(user_id, post_tittle, post_create_date, post_content):

    try:
        cursor.execute("INSERT INTO TBL_Posts(UserID, PostTitle, PostCreateDate, PostContent) Values(%s, %s, %s, %s);", (user_id, post_tittle, post_create_date, post_content,))
        conn.commit()
    except:

        return 0

    return 1

def getAllPost():

    try:

        cursor.execute(
                    'SELECT * FROM TBL_Posts')
        posts = cursor.fetchall()

    except:

        return 0

    return posts


def getIdPost(id):

    try:

        cursor.execute(
                    'SELECT * FROM TBL_Posts where PostID=%s',(id,))
        post = cursor.fetchone()

    except:

        return -99

    return post
    
def deleteIdPost(id):

    try:
        cursor.execute("DELETE FROM TBL_Posts WHERE PostID=%s", (id,))
        conn.commit()
    except:

        return 0

    return 1

def updatePost(user_id, post_id, post_tittle, post_content):

    try:
        cursor.execute("UPDATE TBL_Posts SET PostTitle=%s, PostContent=%s WHERE PostID=%s AND UserID=%s", (post_tittle, post_content, post_id, user_id,))
        conn.commit()
    except:

        return 0

    return 1