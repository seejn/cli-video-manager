from controller import *

def main():
    videos = load_data()
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