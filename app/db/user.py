from app.db.db import db
from passlib.hash import sha256_crypt

cursor, conn = db()

def createUser(user_full_name, user_email, user_password):

    try:
        user_password = sha256_crypt.encrypt(user_password)
        cursor.execute("INSERT INTO TBL_Users(UserFullName, UserEmail, UserPassword) Values(%s, %s, %s);", (user_full_name, user_email, user_password,))
        conn.commit()
    except:

        return 0

    return 1

def checkUser(login_email, login_password):

    cursor.execute(
                'SELECT UserPassword FROM TBL_Users WHERE UserEmail=%s', (login_email,))
    user = cursor.fetchone()

    try:
        if sha256_crypt.verify(login_password, user[0]) != True:

            return 0

        else:

            return 1

    except:

        return 0
