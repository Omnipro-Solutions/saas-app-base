from functools import reduce

DEFAULT_RECORD_LIMIT = 10000


def nested(data: dict, keys: str, default=None):
    """
    Receives a dictionary and a list of keys, and returns the value associated with the keys in order,
    searching the dictionary to any depth, not including lists. in order, searching the dictionary to
    any depth, not including lists. If the key is not found, it returns the default value.
    """
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), data)
