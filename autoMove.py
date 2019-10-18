from datetime import datetime, timedelta
import schedule
import pyautogui
import time

#helper function that prints x,y coordinate of my display in order to close brave ad display(farming BAT coins)

def printPosition():
    #the code below prints the x,y coordinates
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionString, end='')
            print('\b' * len(positionString), end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone.')




def autoMove():
    #hoovers mouse over certain parameters for pixels, and then clicks on it.
    #4 minute intervals
    pyautogui.moveTo(3485, 1934, duration=0.25)
    pyautogui.click(button='left')
    print('WE farming for you')
    start = time.time()
    print("Start time: " + str(start))
    end = time.time()
    time.sleep(240)
    end = time.time()
    ending = end-start
    ending2 = str(round(ending, 2))
    print ('Ending time: ' + str(ending2))

#schedules to run the automove
def timeBot():

    while True:
        autoMove()

        dt = datetime.now() + timedelta(hours=0)
        dt = dt.replace(minute=0)

        while datetime.now() < dt:
            time.sleep(.5)


if __name__ == '__main__':
    #printPosition
    #autoMove()
    timeBot()