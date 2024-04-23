import sqlite3
from controller import *
from db.SqliteDB import SqliteDB

def db_init():
    conn = sqlite3.connect("db/vid_man.db")
    db = SqliteDB(conn)
    return db

def main():
    db = db_init()

    while True:
        heading_view("Video Manager")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update video details")
        print("4. Delete video")
        print("5. Exit app")

        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(db)
            case '2':
                add_new_video(db)
            case '3':
                update_video(db)
            case '4':
                delete_video(db)
            case '5':
                break
            case _:
                print("Invalid Option")
    db.close()

if __name__ == "__main__":
    main()