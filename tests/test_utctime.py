from unittest import TestCase

from datetime import datetime, timezone, timedelta
import pytz
from tzlocal import get_localzone

from pymisc.utctime import utc_to_local, local_to_utc


class TestUtctime(TestCase):

    def test_native_to_utc(self):
        dt_local = datetime(2018, 12, 31, 5, 0, 30, 1000)
        dt_local = get_localzone().localize(dt_local.replace(tzinfo=None))
        expect = '2018-12-31 05:00:30.001000+00:00'
        self.assertEqual(expect, str(local_to_utc(dt_local)))

    def test_utc_to_native(self):
        dt_utc = datetime(2018, 12, 31, 5, 0, 30, 1000, tzinfo=timezone.utc)
        expect = '2018-12-31 05:00:30.001000+09:00'
        self.assertEqual(expect, str(utc_to_local(dt_utc)))

