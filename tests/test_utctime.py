from unittest import TestCase
from unittest.mock import Mock, patch

from datetime import datetime, timezone, timedelta
import pytz
# この書き方だとpatchできない
# from tzlocal import get_localzone
import tzlocal

from pymisc.utctime import AwareDatetime

_UTC_NAIVE_DATETIME = datetime(2018, 12, 31, 5, 0, 30, 1000)
_UTC_AWARE_DATETIME = datetime(2018, 12, 31, 5, 0, 30, 1000, pytz.utc)
_UTC_DATETIME_STRING = '2018-12-31 05:00:30.001000+00:00'
_CST_ID = 'Asia/Shanghai'
_CST_NAIVE_DATETIME = datetime(2018, 12, 31, 13, 0, 30, 1000)
_CST_STRING = '2018-12-31 13:00:30.001000+08:00'
_CST_ISO_STRING = '2018-12-31T13:00:30.001000+08:00'
_CST_DATETIME_STRING = '2018/12/31 13:00.30'
_JST_ID = 'Asia/Tokyo'
_JST_NAIVE_DATETIME = datetime(2018, 12, 31, 14, 0, 30, 1000)
_JST_STRING = '2018-12-31 14:00:30.001000+09:00'
_JST_ISO_STRING = '2018-12-31T14:00:30.001000+09:00'
_JST_DATETIME_STRING = '2018/12/31 14:00.30'


def timezone_china():
    return pytz.timezone(_CST_ID)


class TestUtctime(TestCase):

    @patch('tzlocal.get_localzone', timezone_china)
    def test_to_local_string(self):
        expect = _CST_DATETIME_STRING
        aware = AwareDatetime(_CST_NAIVE_DATETIME, pytz.timezone(_CST_ID))
        self.assertEqual(expect, str(aware.to_local_string()))

    @patch('tzlocal.get_localzone', timezone_china)
    def test_datetime(self):
        _dt = AwareDatetime(_UTC_NAIVE_DATETIME, pytz.utc)
        expect = _UTC_DATETIME_STRING
        self.assertEqual(expect, str(_dt.datetime))

    @patch('tzlocal.get_localzone', timezone_china)
    def test_local_datetime(self):
        _dt = AwareDatetime(_CST_NAIVE_DATETIME)
        expect = _CST_STRING
        self.assertEqual(expect, str(_dt.local_datetime))
