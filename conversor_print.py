import openpyxl

#carregando o arquivo
book = openpyxl.load_workbook('planilhadecompras.xlsx')
#slecionando uma página
frutas_page = book['Frutas']
#imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
	for cell in rows:
		print(cell.value)