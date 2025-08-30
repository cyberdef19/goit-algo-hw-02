from queue import Queue

from application_queue.generate_request import generate_request
from application_queue.process_request import process_request
import time
import keyboard


def start_app():
    application_queue = Queue()
    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("Програму завершено натиском на кнопку esc")
                break

            generate_request(application_queue)
            process_request(application_queue)
            time.sleep(1)

    except KeyboardInterrupt as ex:
        print("Програму завершено!")