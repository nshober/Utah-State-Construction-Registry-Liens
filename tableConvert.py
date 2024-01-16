'''
	Description:
    	Python script to convert html table element from Utah State Contruction Registry to 
        an excel file so it can be uploaded to Domo for a report. Use the htmlTable.txt file
        to paste the html table element and save before running.
        
    Created By: 
    	Nico Shober (2023-09-08)
    
    Modified By:
		Nico Shober (2023-10-25)
		Description: Read from local text file instead of header file
    
	Modified By:
		name (YYYY-MM-dd)
		Description:
'''


from bs4 import BeautifulSoup
import pandas as pd

with open("htmlTable.txt", "r", encoding="utf-8") as file:
    htmlTable = file.read()

soup = BeautifulSoup(htmlTable, 'html.parser')
tableRows = soup.findAll('tr')

noticeType = []
filingDate = []
countyParcel = []
address = []
contractor = []
contractedBy = []
owner = []
filer = []

for row in tableRows[1:]:
    cells = row.find_all('td')
    noticeType.append(cells[1].get_text())
    filingDate.append(cells[2].get_text())
    countyParcel.append(cells[3].get_text())
    address.append(cells[4].get_text())
    contractor.append(cells[5].get_text())
    contractedBy.append(cells[6].get_text())
    owner.append(cells[7].get_text())
    filer.append(cells[8].get_text())


data = {'noticeType': noticeType,'filingDate': filingDate, 'countyParcel': countyParcel, 'address': address,'contractor': contractor, 'contractedBy': contractedBy,'owner': owner, 'filer': filer}
df = pd.DataFrame(data)
#print(df.head(5))

outputFilename = 'output.xlsx'
df.to_excel(outputFilename, index=False, sheet_name='mainSheet', engine='openpyxl')