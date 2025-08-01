objects = ["Stone", "Brain", "House", "mouse", "watch"]

for i, object in  enumerate(objects, start= 1):
    print (f"{i}. {object}")

test = [
    [ 2, 4, 5],
    [ 2, 3, 4],
    [ 5, 6, 3]
]

for i, tests in enumerate(test , 1):
    for i, num in enumerate(tests,1):
        print (f"{i}.   {num} ")

