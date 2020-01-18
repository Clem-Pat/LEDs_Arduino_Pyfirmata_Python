import pyfirmata
import time

board=pyfirmata.Arduino('COM5')

board.digital[2].write(0)
board.digital[3].write(0)
board.digital[4].write(0)

while True:
    board.digital[2].write(1)
    time.sleep(1)
    board.digital[2].write(0)
    board.digital[3].write(1)
    time.sleep(1)
    board.digital[3].write(0)
    board.digital[4].write(1)
    time.sleep(1)
    board.digital[4].write(0)
