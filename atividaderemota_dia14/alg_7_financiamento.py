salario = (input("Digite o valor salário:"))
salariobr = float(salario.replace(',','.'))
valor_financiamento = (input("Digite o valor do financiamento pretendido:"))
valor_financiamentobr = float(valor_financiamento.replace(',','.'))

if float(valor_financiamentobr) <= salariobr*5:
    print("Financiamento concedido, obrigado por nos consultar.")
else:
    print("Financiamente negado, obrigado por nos consultar.")
