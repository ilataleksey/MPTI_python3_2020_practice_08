'''
Упражнение №2: числа Фибоначчи

Напишите программу, вычисляющую n-ное число Фибоначчи. Используйте рекурсивные вызовы функций.
'''

def main():

	FIBO_NUMBER = 7

	def fibo_number(n):
		'''
		Calculate Fibonacci number
		'''

		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return fibo_number(n-2) + fibo_number(n-1)


	result = fibo_number(FIBO_NUMBER)
	print('Число фибоначчи для последовательности из', FIBO_NUMBER, '=', result)

if __name__ == '__main__':
	main()
