import pandas as pd
import xml.etree.ElementTree as ET

# Wczytanie danych z pliku Excel
df = pd.read_excel('DANE_IMPORTER_PK.xlsx')

# Tworzenie korzenia dokumentu XML
root = ET.Element('DATAEX')

# Tworzenie elementu COMMAND dla tworzenia nowego zamówienia
command_import_order = ET.SubElement(root, 'COMMAND', {'Name': 'Import', 'TblRef': 'SALEORDERS'})
ET.SubElement(command_import_order, 'FIELD', {'FldRef': 'OrdRef', 'FldValue': 'zz_11FB-ZAMOWIENIE', 'FldType': '20'})


# Iteracja przez wiersze danych
for index, row in df.iterrows():
    # Pobranie wartości OrdRef z bieżącego wiersza danych
    ord_ref_value = row['OrdRef']

    # Tworzenie elementu COMMAND dla przeniesienia do zamówienia
    command_import_line = ET.SubElement(root, 'COMMAND', {'Name': 'Import', 'TblRef': 'SALEORDERLINES'})
    ET.SubElement(command_import_line, 'FIELD', {'FldRef': 'OrdRef', 'FldValue': ord_ref_value, 'FldType': '20'})
    ET.SubElement(command_import_line, 'FIELD', {'FldRef': 'ArtRef', 'FldValue': row['ArtRef'], 'FldType': '20'})
    ET.SubElement(command_import_line, 'FIELD', {'FldRef': 'LineNum', 'FldValue': str(row['LineNum']), 'FldType': '20'})
    ET.SubElement(command_import_line, 'FIELD', {'FldRef': 'Quantity', 'FldValue': str(row['Quantity']), 'FldType': '20'})

# Tworzenie tekstu XML
xml_str = ET.tostring(root, encoding='unicode')

# Zapis tekstu XML do pliku
with open('output.xml', 'w') as file:
    file.write(xml_str)
