import pycountry
import country_list

from redishandler import add_set_to_redis
# SUPPORTS ALMOST ALL LANGUAGES
def ini_load():
    """loads up all country acronyms on app startup to redis"""
    for country in pycountry.countries:
        iso_2 = country.alpha_2
        iso_acronyms_set = set()

        for lang in country_list.available_languages():
            names_in_lang = dict(country_list.countries_for_language(lang))
            if (to_add := names_in_lang.get(iso_2)) != None:
                iso_acronyms_set.add(to_add)

        add_set_to_redis(country.alpha_3, iso_acronyms_set)

#TODO: use logger
