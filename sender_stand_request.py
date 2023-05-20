import requests
import configuration
import data

def post_create_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


def get_info_about_order_by_track(track):
    params = {
        't': track,
    }
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                        params=params)
