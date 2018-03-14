print("レビュー数:0")
print("[0]レビューを書く")
print("[1]レビューを読む")
print("[2]アプリを終了する")
user_input = int(input())
# インデントは2つでもいい
# 通常は4つのインデントを使用する
def post_review():
    post = {}
    print("ジャンルを入力してください:")
    post["genre"] = input()
    print("タイトルを入力してください:")
    post["title"] = input()
    print("レビューを入力してください:")
    post["review"] = input()
    line = "\n---------------------------"

    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 : " + post["review"] + line)

def read_review():
    pass

def end_program():
    pass

def exception():
    print("入力された値は無効な値です")

if user_input == 0:
    post_review()
elif user_input == 1:
    read_review()
elif user_input == 2:
    end_program()
else:
    exception()
