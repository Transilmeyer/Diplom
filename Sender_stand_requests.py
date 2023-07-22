import Configuration
import Data
import requests

def new_order():
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_ORDER_PATH,
           json=Data.order_body)

def order_info(track):
    return requests.get(Configuration.URL_SERVICE + Configuration.ORDER_INFO,
           params={"t":track} )