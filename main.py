import subprocess
import datetime
import os

from dotenv import load_dotenv

load_dotenv()

# Configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
BACKUP_DIR = os.getenv('BACKUP_DIR')

if not DB_HOST:
    raise ValueError("No database host set")

if not DB_PORT:
    raise ValueError("No database port set")

if not DB_USER:
    raise ValueError("No database user set")

if not DB_PASSWORD:
    raise ValueError("No database password set")

if not DB_NAME:
    raise ValueError("No database name set")

if not BACKUP_DIR:
    raise ValueError("No backup directory set")

# if backup directory does not exist, create it
if not os.path.exists(BACKUP_DIR):
    raise ValueError("Backup directory does not exist")

def export_db():
    # Ensure backup directory exists
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # Timestamp for the backup file
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"{DB_NAME}_backup_{timestamp}.sql"
    backup_filepath = os.path.join(BACKUP_DIR, backup_filename)

    # Construct the mysqldump command
    dump_command = [
        'mysqldump',
        f'--host={DB_HOST}',
        f'--port={DB_PORT}',
        f'--user={DB_USER}',
        f'--password={DB_PASSWORD}',
        DB_NAME
    ]

    try:
        with open(backup_filepath, 'w') as backup_file:
            # Execute the mysqldump command
            subprocess.check_call(dump_command, stdout=backup_file)
        print(f"Database exported successfully to {backup_filepath}")
    except subprocess.CalledProcessError as e:
        print(f"Error exporting database: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    export_db()