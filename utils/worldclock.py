"""

	Timezone aware datetimes.

	Requires
	--------
	pytz
	tzlocal

"""
import datetime
import time
import pytz
import tzlocal
#from pytz import timezone, all_timezones

from utils.logger import log, Logger
from . import logfilepath


LOG_FILE = 'logger.log'

logger = Logger(filepath = logfilepath(LOG_FILE))



class WorldClock(object):
	"""docstring for WorldClock"""
	
	def __init__(self, localzone = None, syszone = None):
		if syszone:
			self.systz = self.timezone(syszone)
		else:
			self.systz = tzlocal.get_localzone()


		if localzone:
			self.localtz = self.timezone(localzone)
		else:
			self.localtz = self.systz

	
	@classmethod
	def timezone(self, tz):
		""" Creates and returns pytz timezone given the timezone name """
		if isinstance(tz, datetime.tzinfo):
			return tz
		else:
			return pytz.timezone(tz)

	@classmethod
	def localize(self, tz, dtm):
		""" Localize a datetime object to the given timezone """
		timezone = self.timezone(tz)
		return timezone.localize(dtm)

	def aslocal(self, dtm):
		""" Returns the current local datetime given the datetime of another timezone """
		return dtm.astimezone(self.localtz)

	def tolocal(self, dtm):
		""" Localize a datetime object to the local timezone """
		return self.localize(self.localtz, dtm)

	def localnow(self):
		""" Get the current local datetime.now() """
		return self.localize(self.localtz, datetime.datetime.now())

	def as_sys(self, dtm):
		""" Returns the current system datetime given the datetime of another timezone """
		return dtm.astimezone(self.systz)

	def tosys(self, dtm):
		""" Localize a datetime object to the system timezone """
		return self.localize(self.systz, dtm)

	def sysnow(self):
		""" Get the current system datetime.now() """
		return self.localize(self.systz, datetime.datetime.now())


	def now(self, tz = None):
		""" Get the datetime now() of a given timezone. Or localnow() if tz = None """
		if tz == None:
			return self.localnow()
		return self.astz(tz, self.localnow())


	def astz(self, tz, dtm):
		""" 
		Returns the datetime of the timezone given the datetime of another timezone 
		"""
		timezone = self.timezone(tz)
		if timezone == self.localttz:
			return self.aslocal(dtm)
		elif timezone == self.systz:
			return self.as_sys(dtm)

		return dtm.astimezone(timezone)
	
	def totz(self, tz, dtm = None):
		""" 
		Localize a datetime object to the given timezone
		"""
		if dtm == None:
			dtm = datetime.datetime.now()

		return self.localize(tz, dtm)-