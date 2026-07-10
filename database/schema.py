from database.connection import get_connection

def create_urls_table():    
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS urls (
            short_url TEXT PRIMARY KEY,
            original_url TEXT NOT NULL,
            expires_at DATETIME,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
    )

    conn.commit()
    conn.close()
    return True