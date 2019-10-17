import pyautogui, time
from datetime import datetime, timedelta

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
    pyautogui.moveTo(3485, 1934, duration=0.25)
    pyautogui.click(button='left')
    print('WE farming for you')
    time.sleep(260)

#schedules to run the automove every 12 miuntes
def timeBot():

    while True:
        autoMove()

        dt = datetime.now() + timedelta(hours=0.5)
        dt = dt.replace(minute=5)

        while datetime.now() < dt:
            time.sleep(.5)


if __name__ == '__main__':
    #printPosition
    #autoMove()
    timeBot()