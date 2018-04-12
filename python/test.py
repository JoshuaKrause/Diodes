class Widget():

    def __init__(self, function_x):
        self.function_x = function_x


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(add(1,2))
print(sub(2,1))

widget = Widget(add)

print(widget.function_x(2,2))