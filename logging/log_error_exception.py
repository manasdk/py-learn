import logging

logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

def do_exceptional_work():
    raise Exception('Doctor Who!') 

def main():
    try:
        do_exceptional_work()
    except Exception as e:
        logger.info('====== Exeption block with instance. ======')
        logger.error('using log.error %s', e)
        logger.exception('using log.exception %s', e)
    try:
        do_exceptional_work()
    except:
        logger.info('====== Exception block without instance. ======')
        logger.error('using log.error')
        logger.exception('using log.exception')

if __name__ == '__main__':
    main()
