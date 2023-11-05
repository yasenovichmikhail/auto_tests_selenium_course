def merge(values):      # values - это список словарей
    result = {}
    for d in values:
        for key in d:
            result.setdefault(key, set()).add(d[key])
    return result