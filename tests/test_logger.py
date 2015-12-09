from utils.logger import log, Logger
from . import logfilepath


LOG_FILE = 'logger.log'

logger = Logger(filepath = logfilepath(LOG_FILE))

def get_logger():
	return logger	


# def test_simple_log_texts():
# 	text = '\nThis is a log text in a test.'
# 	logger.debug(text, 'Just DEBUGIN!!!')
# 	logger.echo(text, 'Just ECHOING!!!')
# 	logger.info(text, 'Just INFOS!!!')
# 	logger.warning(text, 'Just VARNING!!!')
# 	done = True
# 	assert done == True

@log(logger)
def decorated_func(a, y = 0, z = 10):	
	logger.echo('Method This should be Wrapped')

	return a + (y * z) 


def test_log_decorator():
	l = decorated_func(50, y = 5)
	assert l == 100

# def debug(a, b, x = False, y = None, z = 10):
# 	pylog.debug(_format_args(**kwargs, *args))


# def info(a, b, x = False, y = None, z = 10):
# 	pylog.info(_format_args(**kwargs, *args))


# def echo(a, b, x = False, y = None, z = 10):
# 	pylog.info(_format_args(**kwargs, *args))


# def warning(a, b, x = False, y = None, z = 10):
# 	pylog.warning(_format_args(*args))
