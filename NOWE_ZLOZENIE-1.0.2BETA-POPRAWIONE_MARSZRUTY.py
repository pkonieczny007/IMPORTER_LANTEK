import pandas as pd
import xml.etree.ElementTree as ET

# Wczytaj dane z pliku Excel
df = pd.read_excel('DANE_NOWE_ZLOZENIE.xlsx')

# Utwórz korzeń XML
root = ET.Element('DATAEX')

# Przetwórz każdy wiersz danych
for index, row in df.iterrows():
    # Tworzenie komendy Import dla elementu złożenia
    assembly_command = ET.SubElement(root, 'COMMAND', Name='Import', TblRef='PR_PPRR_00000100')

    # Konwertuj wartości liczbowe na ciągi znaków
    assembly_id = str(row['ASSEMBLY_ID'])
    assembly_name = str(row['ASSEMBLY_NAME'])
    pquant = str(row['PQUANT'])

    # Ustalanie wartości pól dla elementu złożenia
    ET.SubElement(assembly_command, 'FIELD', FldRef='PrdRef', FldValue=assembly_id, FldType='20')
    ET.SubElement(assembly_command, 'FIELD', FldRef='PrdName', FldValue=assembly_name, FldType='20')
    ET.SubElement(assembly_command, 'FIELD', FldRef='Assembly', FldValue=pquant, FldType='100')
    ET.SubElement(assembly_command, 'FIELD', FldRef='PCATEGORY', FldValue='2', FldType='100')
    ET.SubElement(assembly_command, 'FIELD', FldRef='ForSale', FldValue='1', FldType='30')

    # Tworzenie komend Import dla operacji złożenia
    for i in range(3):
        operation_command = ET.SubElement(root, 'COMMAND', Name='Import', TblRef='PRODUCT OPERATIONS')

        # Ustalanie wartości pól dla operacji złożenia
        ET.SubElement(operation_command, 'FIELD', FldRef='PrdRef', FldValue=assembly_id, FldType='20')
        ET.SubElement(operation_command, 'FIELD', FldRef='OOrder', FldValue=str(i + 1), FldType='100')
        ET.SubElement(operation_command, 'FIELD', FldRef='PrevOpr', FldValue=str(i), FldType='100')

        # Ustalanie wartości pól dla konkretnej operacji
        if i == 0:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Spawalnia', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Spawanie', FldType='20')
        elif i == 1:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Ocynkownia', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Ocynk', FldType='20')
        elif i == 2:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Centrum kompletacji', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Kompletacja', FldType='20')

    # Tworzenie komend Import dla elementów z bazy do złożenia
    element_command = ET.SubElement(root, 'COMMAND', Name='Import', TblRef='PR_SSTT_00000100')

    # Ustalanie wartości pól dla elementów z bazy do złożenia
    ET.SubElement(element_command, 'FIELD', FldRef='PrdRefOrg', FldValue=assembly_id, FldType='20')
    ET.SubElement(element_command, 'FIELD', FldRef='PrdRefDst', FldValue=row['DXF_ID'], FldType='20')
    ET.SubElement(element_command, 'FIELD', FldRef='PQUANT', FldValue=pquant, FldType='100')

    # Tworzenie komend Import dla operacji złożenia dla elementu
    for i in range(3):
        operation_command = ET.SubElement(root, 'COMMAND', Name='Import', TblRef='PRODUCT OPERATIONS')

        # Ustalanie wartości pól dla operacji złożenia dla elementu
        ET.SubElement(operation_command, 'FIELD', FldRef='PrdRef', FldValue=row['DXF_ID'], FldType='20')
        ET.SubElement(operation_command, 'FIELD', FldRef='OOrder', FldValue=str(i + 1), FldType='100')
        ET.SubElement(operation_command, 'FIELD', FldRef='PrevOpr', FldValue=str(i), FldType='100')

        # Ustalanie wartości pól dla konkretnej operacji
        if i == 0:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Spawalnia', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Spawanie', FldType='20')
        elif i == 1:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Ocynkownia', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Ocynk', FldType='20')
        elif i == 2:
            ET.SubElement(operation_command, 'FIELD', FldRef='WrkRef', FldValue='Centrum kompletacji', FldType='20')
            ET.SubElement(operation_command, 'FIELD', FldRef='OprRef', FldValue='Kompletacja', FldType='20')

# Utwórz drzewo XML
tree = ET.ElementTree(root)

# Zapisz drzewo XML do pliku
tree.write('wyjscie.xml', encoding='utf-8', xml_declaration=True)
