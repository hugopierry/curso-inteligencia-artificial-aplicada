
import pandas as pd

print("="*80)
print("Tabela 'pedidos'\n")


pedidos = pd.read_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\pedidos.ods", engine="odf")
# Caminho absoluto para localizar o arquivo (Absolute Path)
print(pedidos)

print("="*80)

print("Tabela 'clientes'\n")
clientes = pd.read_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\clientes.ods", engine="odf")
print(clientes)

print("="*80)
print("\nUsando merge para relacionar dados: ")
# print(pedidos.dtypes)

resultado = pd.merge(clientes, pedidos, on ="id_cliente", how="outer", indicator=True)
# Combinar ou relacionar DataFrames
print(resultado)

print("="*80)

print("\nIdentificando registros sem correspondência:")
print(resultado[resultado["_merge"] !="both"])
# Filtra e apresenta os registros que não tiveram correspondência
# entre os dois DataFrames após o merge do Pandas.

# Foi utilizado essa função, para identificar esses registros específicos para serem 
# removidos 

print("\nEliminando valore nulos 'NaN':\n")
resultado = resultado.dropna()
# Removendo registros com valores ausentes
print(resultado)

resultado = resultado.drop(columns="_merge")
resultado.to_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\Clientes_pedidos_tratados.ods", index= False, engine="odf")
# # Utilizado o caminho absoluto (Absolute Path) para salvar
# o arquivo tratado no diretório do projeto.

print("\nPlanilha tratada e salva com sucesso!")
# mensagem de confirmação de alterações realizadas e salvas com sucesso!
print("="*80)
input("\n\nPressione ENTER para sair do programa")
# input que aguarda ENTER para finalizar o processo e não fechar o terminal automaticamente