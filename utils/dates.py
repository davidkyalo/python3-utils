import datetime
import time
from pytz import timezone

home_timezone = 'Africa/Nairobi'

def localized(zone_name, dtm = None):
	if not dtm:
		dtm = datetime.datetime.now()

	zone = timezone(zone_name)
	return zone.localize(dtm)


def home_time(dtm = None):
	athome = localized(home_timezone, dtm)
	return athome

def time_as_home(dtm):
	return time_as_zone(home_timezone, dtm)


def time_as_zone(zone_name, dtm = None):
	if zone_name == home_timezone:
		return home_time(dtm)

	if not dtm:
		dtm = home_time()

	return dtm.astimezone(timezone(zone_name))



def str_datetime(f = '%c', ts = None):
    if not ts:
        ts = time.time()
    norm_format = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).strftime(f)


def int_time():
    return int(time.time())



def timetostr(dtm, f = None):
	if not dtm:
		return ' - '
	if not f:
		f = '%H:%M:%S'
	return dtm.strftime(f)


def datetostr(dtm, f = None):
	if not dtm:
		return ' - '
	if not f:
		f = '%d, %b %Y'
	return dtm.strftime(f)

def datetimetostr(dtm, f = None):
	if not dtm:
		return ' - '
	if not f:
		f = '%Y-%m-%d %H:%M:%S'
	return dtm.strftime(f)