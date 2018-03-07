post = {}
print("ジャンルを入力してください:")
post["genre"] = input()

print("タイトルを入力してください:")
post["title"] = input()

print("レビューを入力してください:")
post["review"] = input()
line = "---------------------------"

print("ジャンル : " + post["genre"])
print(line)
print("タイトル : " + post["title"])
print(line)
print("感想 :")
print(post["review"])
print(line)
