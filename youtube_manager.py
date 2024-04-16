import json
import time

file_name = "youtube.txt"

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

def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)

    return

def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    return

def list_all_videos(videos):
    
    if not videos:
        notification_view("No Videos Available")
        time.sleep(1)
        return

    heading_view("Listing all Videos")

    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} || Duration: {video['duration']}")
    
    time.sleep(1)
    return

def add_new_video(videos):
    heading_view("Add new Video")
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")

    new_video = {'name': name, 'duration': duration}

    videos.append(new_video)
    save_data_helper(videos)

    notification_view(f"New video Added: {new_video}")
    time.sleep(1)
    return 

def update_video(videos):
    list_all_videos(videos)

    index = int(input("Select video number to update: ")) - 1

    if not 0 <= index < len(videos):
        notification_view("!!! Invalid option !!!")
        time.sleep(1)
        return

    heading_view("New Video Details")
    
    name = input("Enter name: ")
    duration = input("Enter duration: ")
    new_details = {"name": name, "duration": duration}
    videos[index] = new_details
    save_data_helper(videos)

    notification_view(f"Updated video details: {new_details}")
    time.sleep(1)
    
    return    

def delete_video(videos):
    list_all_videos(videos)

    index = int(input("Select video number to delete: ")) - 1

    if not 0 <= index < len(videos):
        notification_view("!!! Invalid option !!!")
        time.sleep(1)
        return

    del_result = videos.pop(index)
    save_data_helper(videos)

    notification_view(f"Deleted video: {del_result}")
    time.sleep(1)


    return    

def main():
    videos = load_data()
    while True:
        heading_view("Youtube Manager")
        print("1. List all youtube videos")
        print("2. Add new youtube video")
        print("3. Update youtube video details")
        print("4. Delete youtube video")
        print("5. Exit app")

        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Option")

if __name__ == "__main__":
    main()
