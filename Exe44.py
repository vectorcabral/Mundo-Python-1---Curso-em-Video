'''
Elabore um programa que calcule o valor a ser pago de um produto consederando seu preço normal e condição de pagamento:
-> à vista no dinheiro/pix:
    10% de desconto
-> à vista no débito
    05% de desconto
-> em até 2x no cartão
    preço normal
-> 3xx ou mais no cartão: 20% de juros
'''
valor_compra = float(input('Digite o valor da sua compra: '))
print(f'O valor da sua compra foi de R$ {valor_compra}')


print('Esolha o métdo de pagamento: \n'
      'Digite [1] para pagamento à vista no DINHEIRO ou PIX\n'
      'Digite [2] para pagamento à vista no DÉBITO\n'
      'Digite [3] para parcelar em 2x sem juros\n'
      'Digite [4] para parcelar em 3x ou mais')
pagamento = int(input('Digite a opção:  '))
if pagamento == 1:
    print(
        f'A opção escolhida foi à vista no DINHEIRO/PIX, o valor da compra foi de R$ {valor_compra},com 10% de desconto o valor é final {(valor_compra-(valor_compra*0.1)):.2f}')
elif pagamento == 2:
    print(
        f'A opção escolhida foi à vista no DÉBITO, o valor da compra foi de R$ {valor_compra}, com 05% de desconto o valor final é de {(valor_compra-(valor_compra*0.05)):.2f}')
elif pagamento == 3:
    print(
        f'A opção escolhida foi PARCELALEMNTO EM 2x SEM JUROS, o valor da compra foi de R$ {valor_compra} com parcelas de {(valor_compra/2):.2f}')
if pagamento == 4:
    parcelas = int(input('Digite em quantas vezes deseja parcelar: '))
    print(
        f'A opção escohida foi PARCELAMENTO com 20% de juros, o valor da compra foi de R$ {valor_compra} com parcelas de R$ {((valor_compra*1.2)/parcelas):.2f}')
else:
    print('Opção inválida')
