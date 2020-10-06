from math import cos, sin, tan, radians

angulo = radians(float((input('Digite o ângulo: '))))

print('O cosseno do ângulo é: {:.2f}\nO seno do ângulo é: {:.2f}\nA tangente do ângulo é: {:.2f}\n'.format(cos(angulo),sin(angulo),tan(angulo)))
