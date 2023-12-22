text = "ljkhlsdf kjaskldfjjklhasd kl;jasdf jk.asdjk asdjk"
# temp = l
# i = j , i + temp j+l  => jl
temp = ""
for i in text:
    temp = i + temp
text = temp
print(text)