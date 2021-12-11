'''
Упражнение №4: кривая Коха

Три копии кривой Коха, построенные (остриями наружу) на сторонах правильного треугольника, образуют замкнутую кривую бесконечной длины, называемую снежинкой Коха. Нарисуйте ee.
'''


def main():
    import turtle
    turtle.hideturtle()

    DEPTH = 4  # глубина рекурсии - кол-во фракталов
    length = 6000  # исходная длинна прямой

    # задаем скорость черепахи
    turtle.speed(0)

    # сдвигаем черепаху влево на половину длины
    turtle.penup()
    if DEPTH == 0:
        divisor = 1
    else:
        divisor = 3 * DEPTH
    turtle.setposition(- (length / (2 * divisor)), 0)
    turtle.pendown()


    def draw(l, d):
        '''
        Draw Doh's snowflake
        l - length
        d - depth
        :return: none
        '''

        if d == 0:
            turtle.forward(l)
            return

        element_length = l / (3 * d)

        draw(element_length, d - 1)
        turtle.left(60)
        draw(element_length, d - 1)
        turtle.right(120)
        draw(element_length, d - 1)
        turtle.left(60)
        draw(element_length, d - 1)

    turtle.left(60)
    for i in range(3):
        draw(length, DEPTH)
        turtle.right(120)

    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main()
