from flask import Flask, render_template, request
import connection, ajax

app = Flask(__name__)
post = "./datas/posts.csv"


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def list_of_posts():
    posts = connection.read_from_file()
    return render_template("index.html", posts=posts)


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == 'POST':
        post_id = connection.new_id()
        post_title = request.form['title_input']
        post_content = request.form['content_textarea']
        post_date = connection.current_time().strftime("%Y-%m-%d %H:%M:%S")
        post_likes = 0
        all_datas = [str(post_id), str(post_title), str(post_content), str(post_date), str(post_likes)]
        connection.write_to_file(all_datas)
    return render_template("new_post.html")


@app.route("/<post_id>", methods=["GET"])
def show_current_post(post_id, post_title="", post_content="", post_date="", post_likes=""):
    posts = connection.read_from_file()
    for elem in posts:
        if str(post_id) == elem['id']:
            post_title = elem['post_title']
            post_content = elem['post_content']
            post_date = elem['post_date']
            post_likes = elem['post_likes']
    return render_template('current_post.html', post_id=post_id, post_title=post_title, post_content=post_content, post_date=post_date, post_likes=post_likes)


@app.route("/ajax", methods=["POST"])
def ajax_def():
    return ajax.main()


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
