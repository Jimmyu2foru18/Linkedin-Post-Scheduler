import mysql.connector
from config.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from utils.logger import setup_logger

logger = setup_logger()

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_next_post(self):
        query = """
        SELECT * FROM posts 
        WHERE status = 'Pending' 
        ORDER BY created_at ASC 
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def delete_post(self, post_id):
        query = "DELETE FROM posts WHERE id = %s"
        self.cursor.execute(query, (post_id,))
        self.connection.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'connection'):
            self.connection.close() 