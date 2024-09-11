# week03_07.py

test = "I am a BOY."

print(test.count("a"))
print(test.count("A"))

print(test.find("a"))
print(test.find("q"))
print(test.find("am"))
print(test.find("qm"))

print(test.index("a"))
# print(test.index("q"))
print(test.index("am"))
if "qm" in test:
    print(test.index("qm"))


print(test.upper()) # 대문자
print(test.lower()) # 소문자
print(test.title()) # 단어 첫 글자 대문자
print(test.capitalize()) # 문장 첫 글자 대문자
print("/".join(test)) # /를 문자열의 모든 요소에 끼워넣기..


test ="  JMT University  "
print(test)
print("|" + test.strip() + "|")
print("|" + test.lstrip() + "|")
print("|" + test.rstrip() + "|")
print(test)
# strip 공백 제거
# 문자열은 불변이다.


print(test.replace("University", "High School"))

print(test.split())
print(test.split("i"))
