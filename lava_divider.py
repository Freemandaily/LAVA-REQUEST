# This program uses subprocessto give command and open the main script 
# It starts the script for Request blockchain Data using (lava RPC-ENDPOINT)

import time,os
import subprocess

start = True
while start:
    for number in range(7):
        subprocess.Popen(['python3','main.py',f'LAVA_{number}'])
        time.sleep(2)
    print('WAITING FOR THE NEXT 20 MINUTE BEFORE SENDING AGAIN')
    sys.exit()
    #time.sleep(1800)
