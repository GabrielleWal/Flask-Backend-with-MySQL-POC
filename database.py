import mysql.connector
import os
import bcrypt

class Database:

  def __init__(self) -> None:
    config = {
      'user': os.getenv('DB_USER'),
      'password': os.getenv('DB_PASSWORD'),
      'host': os.getenv('DB_HOST'),
      'database': os.getenv('DB_NAME')
    }
    self.cnx = mysql.connector.connect(**config)
    self.cursor = self.cnx.cursor()

    def __encrypt(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email, password):
        password_hash = self.__encrypt(password)
        try:
          self.cursor.execute('INSERT INTO user (email, password) VALUES (%s, %s)', (email, password_hash))
          self.cnx.commit()
          return 'Account registered'
        except mysql.connector.Error as error:
          return error.msg

  def login_user(self, email, pswd):
    try:
      self.cursor.execute('SELECT id, password FROM user WHERE email = (%s)', [email])
      user = self.cursor.fetchone()
      if (user is None):
        return ('User not found')
      id, password = user
      if (not bcrypt.checkpw(pswd.encode(), password.encode())):
        return ('wrong password')
      else:
        return 'User Logged in with'
    except mysql.connector.Error as error:
      return error.msg