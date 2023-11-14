import argparse
import time

parser = argparse.ArgumentParser()
message = "Use -m flag and double quote (\" \") around your message to customize it"
sleepTime = 0.001
parser.add_argument("-m", "--message", action="store", help="Message to be printed", default=message)
parser.add_argument("-s", "--sleeptime", action="store", help="Time between two message printing", default=sleepTime,
                    type=float)
parser.add_argument("-r", "--refresh", action="store_true", help="Should the program refresh the printing")

args = parser.parse_args()

sleepTime = args.sleeptime
message = args.message
shouldRefresh = args.refresh

for key, letter in enumerate(message):
    for pickedLetter in range(ord("!"), ord("z")):
        time.sleep(sleepTime)
        pickedLetter = chr(pickedLetter)
        if shouldRefresh:
            print(message[:key]+pickedLetter, end='\r')
        else:
            print(message[:key] + pickedLetter)
        if pickedLetter == letter:
            break
        elif pickedLetter == " ":
            break
