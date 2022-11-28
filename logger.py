import _thread
import time

LOG_FILE_NAME = "log.log"

LOG_FILE_LOCK = _thread.allocate_lock()
LOG_FILE_LENGTH = 10000


def log(message):
    log_string = f"{time.time()}: {message}"
    print(log_string)
    with LOG_FILE_LOCK:
        try:
            with open(LOG_FILE_NAME, "r") as log_file:
                contents = log_file.read(LOG_FILE_LENGTH * 2)
        except OSError:
            contents = ""
        contents = contents + "\n" + log_string
        with open(LOG_FILE_NAME, "w") as log_file:
            log_file.write(contents[-LOG_FILE_LENGTH:])


def reset_log():
    with LOG_FILE_LOCK:
        with open(LOG_FILE_NAME, "w") as log_file:
            log_file.write(f"{time.time()}: Log Reset")
