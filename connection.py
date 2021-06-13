import csv
import datetime as time
import shutil


def read_from_file():
    posts = []
    with open("datas/posts.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            posts.append(row)
        return posts


def current_time():
    return time.datetime.now()


def new_id():
    new_id = 0
    elems = read_from_file()
    for elem in elems:
        if new_id <= int(elem['id']):
            new_id = int(elem['id'])
    return new_id + 1


def write_to_file(post_datas):
    with open('datas/posts.csv', 'a', newline='') as post_file:
        writer = csv.writer(post_file)
        writer.writerow(post_datas)


def update_file(updated_datas):
    question_row = [str(updated_datas['id']), str(updated_datas['post_title']), updated_datas['post_content'],
                    updated_datas['post_date'], updated_datas['post_likes']]
    delete_question(updated_datas['id'])
    write_to_file(question_row)


def delete_question(id):
    with open('datas/posts.csv', 'r') as inp, open('datas/edit.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != id:
                writer.writerow(row)

    shutil.move('datas/edit.csv', "datas/posts.csv")
