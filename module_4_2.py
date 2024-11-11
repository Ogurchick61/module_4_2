def test_function():


    def inner_function():
        inner = 'Я в области видимости функции test_function'
        print(inner)
        return
    inner_function()
test_function()

#inner_function()# Error функция не может работать вне заданой функции

def inner_function(text):
    print(text)
inner_function('Иначе можно сделать так!!!')

















