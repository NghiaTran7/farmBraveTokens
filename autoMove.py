from datetime import datetime, timedelta
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
    print('WE are hard at work, farming for you! Sit back, relax, and watch the BAT coins roll in!!!!')
    start = time.time()
    #time.sleep(1)
    end = time.time()
    ending = end-start
    ending2 = str(round(ending, 2))
    #print ('Duration of script: ' + str(ending2) + " seconds")

#function to refresh amazon browser every 2 minutes 30 seconds
def autoRefresh():
    pyautogui.typewrite(['f5'])
    print ('We refreshed your browser to trick them into giving us more ads!! MUAHAHAHAHA!!!!')
    time.sleep(30)

def autoClick():
    pyautogui.click(button='left')
    print ('We clicked left!')
    time.sleep(3)


#schedules to run the automove
def timeBot():

    while True:
        autoMove()
        autoClick()
        autoRefresh()


        dt = datetime.now() + timedelta(hours=0)
        dt = dt.replace(minute=0)

        while datetime.now() < dt:
            time.sleep(.5)


if __name__ == '__main__':
    #printPosition()
    #autoMove()
    timeBot()
    pyautogui.FAILSAFE = False