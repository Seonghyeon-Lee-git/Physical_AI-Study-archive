jumin = "990101-1234567"
card = "1234-5678-9012-3456"


jumin_h = jumin.replace(jumin[-6:],"*" * 6)
card_h_len = len(card) - 4
card_h = card.replace(card[:card_h_len], "*" * card_h_len)


print(jumin_h)
print(len(jumin_h))
print(card_h)