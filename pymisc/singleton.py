# https://media.accel-brain.com/python3-singleton/
# http://www.denzow.me/entry/2018/01/28/171416
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

# TODO: マルチスレッド対応
#from threading import Lock


# https://media.accel-brain.com/python3-singleton/
class Singleton(type):
    _instance = {}
#    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        # if cls not in cls._instance:
        #     with cls._lock:
        #         if cls not in cls._instance:
        #             cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


# http://www.denzow.me/entry/2018/01/28/171416
'''
class Singleton:

    _unique_instance = None
    _lock = Lock()  # クラスロック

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            with cls._lock:
                if not cls._unique_instance:
                    cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance
'''

# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
'''
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


'''

