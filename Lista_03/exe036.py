house_value = int (input('O valor da casa ? '))

salary_buyer = float (input('Salário do comprador ? '))

years = int (input('Quantos anos a ser pago ? '))

monthly_installment = house_value/(years * 12)

if monthly_installment < 0.3 * salary_buyer:
  print('Empréstimo foi um sucesso!')
else: 
  print('Empréstimo negado!')