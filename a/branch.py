import warnings
# from memory_profiler import profile

import requests
import web



# ddd

warnings.filterwarnings("ignore")

urls = (
    "/ai/v1/load_time_elasticity", "load_time_elasticity"
)

app = web.application(urls, globals())
#_author:"zqs"
#date:2023/11/7