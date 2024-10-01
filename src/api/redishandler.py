from redis import Redis


password = "KiwiLetsGo"
redis = Redis(host='redis', port=6379, db=0,
              password=f"{password}", decode_responses=True)


def get_set_from_redis(key):
    """returns set of vals corresponding to key"""
    return redis.smembers(key)


def add_set_to_redis(key, vals):
    """adds set of values under specific key into redis"""
    redis.sadd(key, *vals)

# using set operation integrated in redis to "filter" input list
def intersection_iso_input(key, vals):
    """this fuction returns the intersection of {set(vals), set saved under key param}"""
    add_set_to_redis("TO_COMPARE", vals)
    res = redis.sinter("TO_COMPARE", key)
    redis.delete("TO_COMPARE")
    return res
