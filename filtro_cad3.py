import pandas as pd

# Le o arquivo
df_csv = pd.read_csv("relatorioCAD3.csv")

# Remove as quebras de linha
df_csv.replace('\n',' ', regex=True, inplace=True)

# Seleciona as linhas que serão removidas por categoriaFinalizacaoValor
linhas_para_remover = ["FSD","FDP","FSA","-"]

df_filtrado = df_csv[~df_csv["categoriaFinalizacaoValor"].isin(linhas_para_remover)]
df_finalizado_delegacia = df_csv[df_csv["categoriaFinalizacaoValor"] == "FDP"]

# Seleciona as colunas que serão removidas do CSV final
colunas_para_manter = ["categoriaFinalizacaoValor","dataHoraRegistro", "naturezasFinais"]

df_filtrado = df_filtrado[colunas_para_manter]
df_finalizado_delegacia = df_finalizado_delegacia[colunas_para_manter]

# Salva os CSV's em UTF-8 e remove as linhas do índice
df_filtrado.to_csv("filtradoCAD3.csv", encoding="utf-8", index=False)
df_finalizado_delegacia.to_csv("finalizadoDelegaciaCAD3.csv", encoding="utf-8", index=False)