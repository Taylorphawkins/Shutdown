#Alarm Clock


import datetime
import time
from subprocess import Popen, PIPE
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class my_timer():

    def __init__(self):
        super().__init__()
        logging.basicConfig(level=logging.INFO)

        
    def popup(self):
        script = 'tell the current application to display dialog "It worked!!" & return & "The script worked. Thats good. A lot more needs to be done, but this is a good start!" buttons {"Close"} default button 1 with icon 1'
        p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(script)
        return stdout
    

    def wait_for_time(self, set_time):
        while True:
            Time = datetime.datetime.now()
            now_time = Time.strftime("%H:%M")
            logger.info(now_time + Time.strftime(":%S"))
            if now_time == set_time:
                logger.info("yes")
                self.popup()
                break
            else:
                time.sleep(10)
                continue


    def snooze(self):
        pass
    

    def shut_down(self):
        if alert is True:
            script = 'tell application "System Events" shut down, end tell'



if __name__ == "__main__":
    set_time = input("what time would you like for me to alert you?: ")
    timer = my_timer()
    timer.wait_for_time(set_time)



