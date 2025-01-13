import pandas as pd

# Le o arquivo
df_excel = pd.read_excel("relatorio.xlsx")

# Remove as quebras de linha
df_excel.replace('\n', ' ', regex=True, inplace=True)
df_excel['NATUREZA'] = df_excel['NATUREZA'].str.upper()
df_excel['DT_REGISTRO_OCORRENCIA'] = pd.to_datetime(df_excel['DT_REGISTRO_OCORRENCIA'], errors='coerce')
df_excel['DT_REGISTRO_OCORRENCIA'] = df_excel['DT_REGISTRO_OCORRENCIA'].dt.strftime('%d/%m/%Y')

# Seleciona as linhas que serão removidas por MOTIVO_FINALIZACAO
linhas_para_remover = ["FINALIZADO SEM DESPACHO", "FINALIZADO NA DELEGACIA DE POLÍCIA", "FINALIZADO SEM ATENDIMENTO APÓS DESPACHO"]
df_filtrado = df_excel[~df_excel["MOTIVO_FINALIZACAO"].isin(linhas_para_remover)]
df_finalizado_delegacia = df_excel[df_excel["MOTIVO_FINALIZACAO"] == "FINALIZADO NA DELEGACIA DE POLÍCIA"]

# Seleciona as colunas que serão removidas do CSV final
colunas_para_remover = ["ID_INCIDENTE", "NO_REGIAO_ATUACAO", "DT_REGISTRO_INCIDENTE", "DT_DESIGNACAO_OPERADOR", "SG_UF", "NO_MUNICIPIO", "NO_RODOVIA", "NR_KM", "TX_TRECHO", "TIPO_LOCALIZACAO", "PRIORIDADE", "ED_BAIRRO", "ED_LOGRADOURO", "ED_NUMERO", "ED_COMPLEMENTO", "ED_PONTO_REFERENCIA", "SITUACAO"]
df_filtrado = df_filtrado.drop(columns=colunas_para_remover)
df_finalizado_delegacia = df_finalizado_delegacia.drop(columns=colunas_para_remover)

# Cria o arquivo alimentabanco.csv com as colunas desejadas
df_alimenta_banco = df_excel[['DT_REGISTRO_OCORRENCIA', 'NATUREZA']].copy()

# Define 'Categoria' e 'Subcategoria' com os mesmos valores de 'NATUREZA'
df_alimenta_banco['Categoria'] = df_alimenta_banco['NATUREZA']
df_alimenta_banco['Subcategoria'] = df_alimenta_banco['NATUREZA']

# Renomeia a coluna 'DT_REGISTRO_OCORRENCIA' para 'Data'
df_alimenta_banco.rename(columns={'DT_REGISTRO_OCORRENCIA': 'Data'}, inplace=True)

# Salva o novo CSV
df_alimenta_banco[['Data', 'Categoria', 'Subcategoria']].to_csv("alimentabanco.csv", encoding="utf-8", index=False)

# Salva os CSV's em UTF-8 e remove as linhas do índice
df_filtrado.to_csv("filtrado.csv", encoding="utf-8", index=False)
df_finalizado_delegacia.to_csv("finalizadoDelegacia.csv", encoding="utf-8", index=False)
