import webbrowser
import sys

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0

def input_math():
    global ERROR_COUNT
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1":
                open_video()
                break
            elif user_input.lower() == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1
    except Exception as e:
        print(f"An error occurred: {e}")
        ERROR_COUNT -= 1

def open_video():
    webbrowser.open(VIDEO_URL)
    print("Rickroll incoming...")

if __name__ == "__main__":
    input_math()