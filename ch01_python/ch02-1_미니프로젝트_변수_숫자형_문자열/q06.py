s = "  Life is too short, You need Python  "


s_len = len(s)
s = s.strip()
print(s_len, len(s))


s_count_o = s.count("o")
print(s_count_o)


print(s.find("short"), s.find("Java"))
print(s.replace("Python", "Java"))
print(s.split())
print(len(s.split()))