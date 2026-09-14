email = "hong.gildong@example.com"
pos = email.find("@")


print(pos)
print(email[:pos], email[pos + 1:])

id = email.split("@")[0]
domain = email.split("@")[1]


print(id, domain)
print(id.upper(), domain.split(".")[0])