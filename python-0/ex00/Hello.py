ft_list = ["Hello","tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

temp_tuple = list(ft_tuple)
temp_tuple[1] = "Spain!"
ft_tuple = tuple(temp_tuple)

ft_set.remove("tutu!")
ft_set.add("Barcelona!")

ft_dict["Hello"] = "42Barcelona!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)