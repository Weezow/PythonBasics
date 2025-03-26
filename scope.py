ball = 3

def string_check(input):
    var = 1
    if input == "apple":
        return "basket"
    if input == "bananas":
        var = 3
    if input == "cherry":
        ball = 5
    return var

print(string_check("cherry"))