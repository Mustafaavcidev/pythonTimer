import time


def countdown_timer(seconds):
    while seconds > 0:
        print(f"remaining time : {seconds} second")
        time.sleep(1)
        seconds -= 1
    print(f"remaining time : {seconds} second... time expired")


countdown_timer(10)
