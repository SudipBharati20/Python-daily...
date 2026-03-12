import time

while True:
    current_time = time.strftime("%H:%M:%S")  # Hour:Minute:Second
    print("\rCurrent Time:", current_time, end="")
    time.sleep(1)  # wait 1 second