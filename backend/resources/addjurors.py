"""

Script intended to add jurors from an excel file

"""

import pandas as pd


df = pd.read_excel('jurados.xlsx')



df['CIUDAD'][df['CIUDAD'] == "MEDELLIN"] = 'Medellín'
df['CIUDAD'][df['CIUDAD'] == "BUCARAMANGA"] = 'Bucaramanga'



jurors = []
# dado que el índice comienza en cero, le agregamos 1
# como ya tenemos 1, y además un jurado, el indíce comenzará desde 2
for index,row in df.iterrows():
    juror = {}

    juror["name"] = row["NOMBRE"]
    juror["email"] = row["email"]
    juror["upb_id"] = row['ID']
    juror["password"] = str(row['ID'])
    juror['seccional'] = row['CIUDAD']
    juror["isAdmin"] = 'false'
    juror["participants"] = []
    juror["row_id"] = index+2

    jurors.append(juror)


print(jurors)
