"""
Python公式ドキュメントより抜粋
https://www.soudegesu.com/python/python-datetime/

aware オブジェクト
aware オブジェクトは他の aware オブジェクトとの相対関係を把握出来るように、
タイムゾーンや夏時間の情報のような、アルゴリズム的で政治的な適用可能な
時間調節に関する知識を持っています。 aware オブジェクトは解釈の余地のない
特定の実時刻を表現するのに利用されます。

naive オブジェクト
naive オブジェクトには他の日付時刻オブジェクトとの相対関係を把握するのに
足る情報が含まれません。 あるプログラム内の数字がメートルを表わしているのか、
マイルなのか、それとも質量なのかがプログラムによって異なるように、
naive オブジェクトが協定世界時 (UTC) なのか、現地時間なのか、それとも
他のタイムゾーンなのかはそのプログラムに依存します。 Naive オブジェクトは
いくつかの現実的な側面を無視してしまうというコストを無視すれば、簡単に
理解でき、うまく利用することができます。
"""
from datetime import datetime
import pytz
# この書き方だとpatchできない
# from tzlocal import get_localzone
import tzlocal

"""
タイムゾーン
https://jp.cybozu.help/general/ja/admin/list_systemadmin/list_system_time/timezone.html
"""

"""
出典
https://narito.ninja/blog/detail/81/
https://www.soudegesu.com/python/python-datetime/
https://note.nkmk.me/python-datetime-isoformat-fromisoformat/
https://qiita.com/shota243/items/91660ece72b5e84c3adb
"""

"""
キーワード
ISO8601, RFC3339
"""


class AwareDatetime:
    def __init__(self, naive_time, tz=None):
        """
        指定されたローカル時間からUTCやローカル文字列など生成する。

        :param naive_time: naive時間。tzが設定されていても無視する。
        :param tz: タイムゾーン。省略された場合はPCに設定されているタイムゾーン。
        """
        self._tz = tz
        if self._tz is None:
            self._tz = tzlocal.get_localzone()
        _dt = datetime(
            year=naive_time.year,
            month=naive_time.month,
            day=naive_time.day,
            hour=naive_time.hour,
            minute=naive_time.minute,
            second=naive_time.second,
            microsecond=naive_time.microsecond)
        if self._tz is not pytz.utc:
            self._utc = self._tz.localize(_dt).astimezone(pytz.utc)
        else:
            # 内部ではUTCで保持する
            self._utc = pytz.utc.localize(_dt)

    @property
    def datetime(self):
        return self._utc

    @property
    def local_datetime(self):
        return self._utc.astimezone(tzlocal.get_localzone())

    def to_local_string(self, form='%Y/%m/%d %H:%M.%S'):
        return self._utc.astimezone(tzlocal.get_localzone()).strftime(form)

    def to_iso_string(self):
        return self._utc.isoformat()

    def to_local_iso_string(self):
        return self._utc.astimezone(tzlocal.get_localzone()).isoformat()
        # _naive = self._utc.astimezone(tzlocal.get_localzone()).replace(tzinfo=None)
        # return self._tz.normalize(self._tz.localize(_naive)).isoformat()

    def __str__(self):
        return self._utc


if __name__ == '__main__':
    _now = datetime.now()
    print(_now)
    print(_now.tzinfo)
    print("localize UTC: {}".format(pytz.utc.localize(_now)))
    print("localize JST: {}".format(tzlocal.get_localzone().localize(_now)))
    print("replace: {}".format(_now.replace(tzinfo=tzlocal.get_localzone())))   # +9:19
    print("")
    aware = AwareDatetime(_now)
    print("datetime: {}".format(aware.datetime))
    print("local_datetime: {}".format(aware.local_datetime))
    print("to_local_string: {}".format(aware.to_local_string()))
    print("to_iso_string: {}".format(aware.to_iso_string()))
    print("to_local_iso_string: {}".format(aware.to_local_iso_string()))
    print("")
    aware = AwareDatetime(_now, tzlocal.get_localzone())
    print("datetime: {}".format(aware.datetime))
    print("local_datetime: {}".format(aware.local_datetime))
    print("to_local_string: {}".format(aware.to_local_string()))
    print("to_iso_string: {}".format(aware.to_iso_string()))
    print("to_local_iso_string: {}".format(aware.to_local_iso_string()))
    print("")
    aware = AwareDatetime(_now, pytz.utc)
    print("datetime: {}".format(aware.datetime))
    print("local_datetime: {}".format(aware.local_datetime))
    print("to_local_string: {}".format(aware.to_local_string()))
    print("to_iso_string: {}".format(aware.to_iso_string()))
    print("to_local_iso_string: {}".format(aware.to_local_iso_string()))
