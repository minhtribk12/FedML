from communicate import send
import time
while True:
    send('./acc_loss/','weight_U0_0_1.txt', '10.100.3.54', 4455)
    time.sleep(2)

    