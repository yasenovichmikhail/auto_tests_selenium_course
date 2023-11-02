def build_query_string(params):
    return '&'.join([f"{key}={value}" for key, value in sorted(params.items())])