from app.db.session import check_database_connection

if __name__ == "__main__":
    check_database_connection()
    print("Lakebase connection successful!")
