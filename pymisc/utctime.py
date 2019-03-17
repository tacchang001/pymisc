from datetime import datetime
from pytz import timezone, utc
from tzlocal import get_localzone

_NATIVE_TIMEZONE = get_localzone()


def naive_to_utc(native_datetime):
    return get_localzone().localize(native_datetime).astimezone(utc)


def local_to_utc(local_datetime):
    return local_datetime.replace(tzinfo=utc)


def utc_to_local(utc_datetime):
    return _NATIVE_TIMEZONE.localize(utc_datetime.replace(tzinfo=None))
