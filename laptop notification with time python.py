import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Alert!!!!",
            message="Take a break! it has been an hour!",
            timeout=5
        )
        time.sleep(60) # how many second after that it will remind again
        
import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Alert!!!!",
            message="Take a break! it has been an hour!",
            timeout=5
        )
        time.sleep(50) # how many second after that it will remind again
