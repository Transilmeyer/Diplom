#Павлов Олег 6-я когорта — Финальный проект. Инженер по тестированию плюс
import Sender_stand_requests
import Data
import requests

def track_order():
    track = Sender_stand_requests.new_order()
    return track.json()["track"]

def test_order():
    track = track_order()
    get_response = Sender_stand_requests.order_info(track)
    assert get_response.status_code == 200