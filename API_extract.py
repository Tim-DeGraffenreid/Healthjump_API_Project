import requests_cache
import json
from helper_functions import *

#Cache for API extraction
requests_cache.install_cache('healthjump_cache', backend='sqlite', expire_after=180)
print("Extracting data from Healthjump API...")

#Extract demographic data from Healthjump sandbox
response = call_API()
#Format and sort by first name extracted data
formatted = format_data(response)

#Print extracted data to screen
print(formatted)
#Write extracted data to demographicData.json file
write_to_file("demographicData.json", formatted)

input("Press enter to exit...")






