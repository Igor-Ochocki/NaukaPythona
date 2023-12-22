# 18. Zdefiniuj funkcję reverse_str() do odwracania stringu.
to_reverse = "ljkhlsdf kjaskldfjjklhasd kl;jasdf jk.asdjk asdjk"
# temp = l
# i = j , i + temp j+l  => jl


def reverse_str(text):
    temp = ""
    for i in text:
        temp = i + temp
    text = temp
    return text


to_reverse = reverse_str(to_reverse)
print(to_reverse)
