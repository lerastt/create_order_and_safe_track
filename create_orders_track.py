import data
import sender_stand_request

# создание нового заказа и сохранить номер трека заказа
def test_response_status_code():
    create_order_response = sender_stand_request.post_create_order(data.order_body)
    track = create_order_response.json()["track"]
    get_info_about_order_by_track_response = sender_stand_request.get_info_about_order_by_track(track)
    assert get_info_about_order_by_track_response.status_code == 200
