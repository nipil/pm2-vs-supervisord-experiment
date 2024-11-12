#!/bin/bash

import time
import os
import random
import logging

def work():
    logging.info(f'PID {os.getpid()}: Processing item')

def wait():
    n = random.randint(0,4)
    logging.debug(f'PID {os.getpid()}: Sleeping for {n} seconds')
    time.sleep(n)

def loop():
    while True:
        work()
        wait()

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
    logging.info(f'PID {os.getpid()}: Starting.')
    random.seed(time.time())
    try:
        loop()
    except KeyboardInterrupt:
        logging.warning(f'PID {os.getpid()}: User requested exit...')

if __name__ == '__main__':
    main()
