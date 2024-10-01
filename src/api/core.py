import pycountry
import re
from redishandler import intersection_iso_input


def handler(iso, input_list):
    if input_list == []:
        raise Exception("Country list provided empty")

    pattern = r"\b([a-zA-Z]{2,3})\b"

    if not re.match(pattern, iso):
        raise Exception("ISO format is invalid")

    # ISO 3166-1 alpha-2 and ISO 3166-1 alpha-3 support, ISO 3166-1 numeric is rubbish
    if len(iso) == 3:
        country_details = pycountry.countries.get(alpha_3=iso)
    else:
        country_details = pycountry.countries.get(alpha_2=iso)

    if not country_details:
        raise Exception("Country does not exist")

    iso = country_details.alpha_3
        

    iso = iso.upper()

    res=intersection_iso_input(iso, input_list)

    # if we really insisted on mantaining the order.. uncomment following line:
    # res = [ elem for elem in input_list if elem in res ]

    return (
        {
            "iso": iso.lower(),
            "match_count": len(res), 
            "matches": list(res)
        }
    )
