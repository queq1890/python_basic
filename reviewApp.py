# pythonではリストオブジェクトと呼ぶ
posts = []
line = "\n---------------------------"

def post_review():
  # pythonでは辞書オブジェクトと呼ぶ
    post = {}
    print("ジャンルを入力してください:")
    post["genre"] = input()
    print("タイトルを入力してください:")
    post["title"] = input()
    print("レビューを入力してください:")
    post["review"] = input()

    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 : " + post["review"] + line)

    posts.append(post)

def read_review():
    for (num, post) in enumerate(posts):
        print("[" + str(num) + "] :" + post["genre"] + "のレビュー")

    print("見たいレビューの番号を入力してください")
    review_input = int(input())
    post = posts[review_input]

    print("## ジャンル : " + post["genre"] + line)
    print("## タイトル : " + post["title"] + line)
    print("## 感想 : \n" + post["review"] + line)

def end_program():
    exit()

def exception():
    print("入力された値は無効な値です")

while True:
    print("レビュー数:" + str(len(posts)))
    print("[0]レビューを書く")
    print("[1]レビューを読む")
    print("[2]アプリを終了する")
    user_input = int(input())

    if user_input == 0:
        post_review()
    elif user_input == 1:
        read_review()
    elif user_input == 2:
        end_program()
    else:
        exception()
