from flask import request
import connection


def main():
    return like_increase(request.form["param"])


def like_increase(id):
    new_value = 0
    datas = connection.read_from_file()
    for data in datas:
        if data['id'] == id:
            new_value = int(data['post_likes']) + 1
            data['post_likes'] =str(new_value)
            connection.update_file(data)
    return str(new_value)


# def like_decrease(id):
#     datas = connection.read_from_file()
#     for data in datas:
#         if data['id'] == id:
#             int(data['post_likes']) - 1
#
#
# def like_reset(id):
#     datas = connection.read_from_file()
#     for data in datas:
#         if data['id'] == id:
#             (data['post_likes']) = 0
