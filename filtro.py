import pandas as pd

# Le o arquivo
df_csv = pd.read_csv("arquivo.csv")

# Remove as quebras de linha
df_csv.replace('\n',' ', regex=True, inplace=True)

# Seleciona as linhas que serão removidas por MOTIVO_FINALIZACAO
linhas_para_remover = ["FINALIZADO SEM DESPACHO","FINALIZADO NA DELEGACIA DE POLÍCIA","FINALIZADO SEM ATENDIMENTO APÓS DESPACHO"]

df_filtrado = df_csv[~df_csv["MOTIVO_FINALIZACAO"].isin(linhas_para_remover)]
df_finalizado_delegacia = df_csv[df_csv["MOTIVO_FINALIZACAO"] == "FINALIZADO NA DELEGACIA DE POLÍCIA"]

# Seleciona as colunas que serão removidas do CSV final
colunas_para_remover = ["NO_AGENCIA", "NO_REGIAO_ATUACAO", "DT_REGISTRO_INCIDENTE", "SG_UF", "NO_MUNICIPIO", "NO_RODOVIA","NR_KM", "TX_TRECHO", "TIPO_LOCAL", "SITUACAO"]

df_filtrado = df_filtrado.drop(columns=colunas_para_remover)
df_finalizado_delegacia = df_finalizado_delegacia.drop(columns=colunas_para_remover)

# Salva os CSV's em UTF-8 e remove as linhas do índice
df_filtrado.to_csv("filtrado.csv", encoding="utf-8", index=False)
df_finalizado_delegacia.to_csv("finalizadoDelegacia.csv", encoding="utf-8", index=False)