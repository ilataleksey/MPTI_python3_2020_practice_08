'''
Упражнение №3: кривая Коха

Нарисуйте кривую Коха. Процесс её построения выглядит следующим образом: берём единичный отрезок, разделяем на три равные части и заменяем средний интервал равносторонним треугольником без этого сегмента. В результате образуется ломаная, состоящая из четырёх звеньев длины 1/3. На следующем шаге повторяем операцию для каждого из четырёх получившихся звеньев и т. д… Предельная кривая и есть кривая Коха.
'''


def main():
    import turtle

    DEPTH = 3  # глубина рекурсии - кол-во фракталов
    length = 500 * (1 + DEPTH)  # исходная длинна прямой при DEPTH = 0

    # задаем скорость черепахи
    turtle.speed(0)

    # сдвигаем черепаху влево на половину длины
    # turtle.ht()
    # turtle.penup()
    # turtle.back(length / (2 * DEPTH))
    # turtle.pendown()
    # turtle.st()

    def draw(l, d):
        '''
        Draw Doha's curve
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

    draw(length, DEPTH)


if __name__ == '__main__':
    main()
