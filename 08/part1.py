lines = [x.strip("\n").split(" | ") for x in open("input.txt").readlines()]
easy_digits = 0
for pre, post in lines:
    pre = pre.split(" ")
    post = post.split(" ")
    for segments in post:
        if len(segments) in [2, 3, 4, 7]:
            easy_digits += 1

print(easy_digits)
