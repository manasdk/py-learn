2014-06-13 10:38:03,569 - test_logger - INFO - ====== Exeption block with instance. ======
2014-06-13 10:38:03,569 - test_logger - ERROR - using log.error Doctor Who!
2014-06-13 10:38:03,569 - test_logger - ERROR - using log.exception Doctor Who!
Traceback (most recent call last):
  File "log_error_exception.py", line 19, in main
    do_exceptional_work()
  File "log_error_exception.py", line 15, in do_exceptional_work
    raise Exception('Doctor Who!')
Exception: Doctor Who!
2014-06-13 10:38:03,569 - test_logger - INFO - ====== Exception block without instance. ======
2014-06-13 10:38:03,569 - test_logger - ERROR - using log.error
2014-06-13 10:38:03,569 - test_logger - ERROR - using log.exception
Traceback (most recent call last):
  File "log_error_exception.py", line 25, in main
    do_exceptional_work()
  File "log_error_exception.py", line 15, in do_exceptional_work
    raise Exception('Doctor Who!')
Exception: Doctor Who!

