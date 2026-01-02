import os
import sys
import pymysql

# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Manual settings import to avoid Django setup issues
from backend import settings

db_settings = settings.DATABASES['default']

print(f"Checking MySQL connection...")
print(f"Host: {db_settings['HOST']}")
print(f"User: {db_settings['USER']}")
print(f"Database: {db_settings['NAME']}")

try:
    # Connect without database first
    connection = pymysql.connect(
        host=db_settings['HOST'],
        user=db_settings['USER'],
        password=db_settings['PASSWORD'],
        port=int(db_settings['PORT']) if db_settings['PORT'] else 3306,
        charset='utf8mb4'
    )
    print("\n✅ Connection to MySQL Server: SUCCESS")
    
    try:
        with connection.cursor() as cursor:
            db_name = db_settings['NAME']
            print(f"Attempting to create database '{db_name}'...")
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"✅ Database '{db_name}' ready.")
    finally:
        connection.close()

except pymysql.err.OperationalError as e:
    code, msg = e.args
    if code == 1045:
        print("\n❌ ACCESS DENIED")
        print("The password for user 'root' is incorrect.")
        print("👉 ACTION REQUIRED: Open 'backend/backend/settings.py' and update the 'PASSWORD' field with your actual MySQL password.")
    else:
        print(f"\n❌ Connection Error: {e}")

except Exception as e:
    print(f"\n❌ Unexpected Error: {e}")
