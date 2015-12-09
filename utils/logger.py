import logging as pylog
import datetime
import functools
"""
	Timezone aware datetimes.

	Requires
	--------
	pytz
	tzlocal
"""

def log(logger, level = None, log_return_val = True):
	_logger = logger
	def wrap(f):
		def wrapped_func(*args, **kwargs):
			starttxt = _format_args('------------------ [', 
						datetime.datetime.now(), 
						'] ------------------',
						'\nCALL TO:',f.__name__,'in',f.__module__,
						'\n**KWARGS:\n\t', kwargs, '\n*ARGS:\n\t', args)
			_logger.log(starttxt)
			return_val = f(*args, **kwargs)
			if log_return_val:
				returntxt = _format_args('RETURNED:\n\t', return_val)
				_logger.log(returntxt)
			endtxt = _format_args("\nDONE AT:\n\t", datetime.datetime.now(), 
						'\n-------------------------------- END', 
						'--------------------------------\n\n')
			_logger.log(endtxt)
			return return_val

		return wrapped_func
	return wrap


def _format_args(*args, **kwargs):
	return ' '.join(['{}'.format(x) for x in args])



class Logger(object):
	"""docstring for logger"""
	
	def __init__(self, filepath, filemode = 'a', level = pylog.DEBUG):
		self.logfile = filepath
		self.loglevel = level
		self.filemode = filemode


	def debug(self, *args, **kwargs):
		self.log(_format_args(*args, **kwargs))


	def info(self, *args, **kwargs):
		self.log(_format_args(*args, **kwargs))


	def echo(self, *args, **kwargs):
		self.log(_format_args(*args, **kwargs))


	def log(self, text, level = None):
		with open(self.logfile , self.filemode) as lf:
			lf.write(text + '\n')


	def warning(self, *args, **kwargs):
		self.log(_format_args(*args, **kwargs))

