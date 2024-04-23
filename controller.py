import json
import time

def heading_view(title):
    sym = "x "
    length = 70

    print("\n")
    print(sym * length)
    print(sym)
    print(f"{sym} {title}")
    print(sym)
    print(sym * length)
    print("\n")
    
    return

def notification_view(title):
    sym = "*"
    length = 70
    
    print("\n")
    print(sym * length)
    print(sym)
    print(f"{sym} {title}")
    print(sym)
    print(sym * length)
    print("\n")
    
    return

def list_all_videos(db):

    videos = db.get_data("videos")

    if not videos:
        notification_view("No Videos Available")
        time.sleep(1)
        return

    heading_view("Listing all Videos")
    for video in videos:
        print(f"Id: {video[0]} || Name: {video[1]} || Duration: {video[2]}")
    
    time.sleep(1)
    return videos

def add_new_video(db):
    heading_view("Add new Video")
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    new_video = {'name': name, 'duration': duration}

    db.insert_data("videos", new_video)

    notification_view(f"New video Added: {new_video}")
    time.sleep(1)
    return 

def update_video(db):
    videos = list_all_videos(db)
    index = int(input("Select video Id to update: "))
    is_data_available = db.get_data("videos", id = index)

    if not is_data_available:
        notification_view("!!! Invalid option !!!")
        time.sleep(1)
        return

    heading_view("New Video Details")
    
    name = input("Enter name: ")
    duration = input("Enter duration: ")

    fields = ("name", "duration")
    new_data = (name, duration, index)

    db.update_data("videos", fields, new_data)

    new_details = {"name": name, "duration": duration}
    notification_view(f"Updated video details: {new_details}")
    
    time.sleep(1)
    
    return    

def delete_video(db):
    videos = list_all_videos(db)
    index = int(input("Select video Id to delete: "))
    
    is_data_available = db.get_data("videos", id = index)

    if not is_data_available:
        notification_view("!!! Invalid option !!!")
        time.sleep(1)
        return

    db.delete_data("videos", index)

    del_video = is_data_available

    notification_view(f"Deleted video: {del_video}")
    time.sleep(1)


    return    


