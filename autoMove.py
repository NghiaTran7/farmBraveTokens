import pyautogui, time

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
    time.sleep(5)
    print('WE farming for you')



if __name__ == '__main__':
    #printPosition()
    autoMove()