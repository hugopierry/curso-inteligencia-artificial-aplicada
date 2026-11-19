from unittest import result

import pandas as pd

print("="*80)
print("Tabela 'pedidos'\n")

pedidos = pd.read_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\pedidos.ods", engine="odf")
print(pedidos)

print("="*80)

print("Tabela 'clientes'\n")
clientes = pd.read_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\clientes.ods", engine="odf")
print(clientes)

print("="*80)
print("\nUsando merge para concatenar dados: ")
# print(pedidos.dtypes)

resultado = pd.merge(clientes, pedidos, on ="id_cliente", how="outer", indicator=True)
print(resultado)

print("="*80)
print("\nEliminando valore nulos 'NaN':\n")
print("\nInformando todas as linhas com valore nulos")
print(resultado[resultado["_merge"] !="both"])

print("\nEliminando valore nulos 'NaN':\n")
resultado = resultado.dropna()
print(resultado)

resultado = resultado.drop(columns="_merge")
resultado.to_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\Clientes_pedidos_tratados.ods", index= False, engine="odf")

print("\nPlanilha tratada e salva com sucesso!")

print("="*80)
input("\n\nPressione ENTER para sair do programa")