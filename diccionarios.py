## Nombres de parallel ##
P = {
    "EXT": "Extracción",
    "TRF": "Transformación",
    "LOD": "Cargue",
    "CHC": "Cambios",
    "FRMW": "Framework",
    "PRPAL": "Principal"
}
## Tipo Artefacto
T = {
    "JOB": "Parallel",
    "SEQ": "Secuencia"
}
## Nombre secuencias
S = {
    "JOB": "Parallel",
    "SEQ": "Secuencia"
}
## Nombre de links
L = {
    "Lnk": "Nombre links"
}
## Nombre de stages
G = {
    "AGG" : "Aggregator",
    "CDC" : "Change Capture",
    "CAC" : "Change Apply",
    "COP" : "Copy",
    "FIL" : "Filter",
    "FTP" : "FTP",
    "FUN" : "Funnel",
    "LKP" : "LookUp",
    "MER" : "Merge",
    "MOD" : "Modify",
    "PIV" : "Pivot",
    "RMD" : "Remove Duplicates",
    "SCD" : "Slowly Changing Dimension",
    "SRT" : "Sort",
    "SKG" : "Surrogate Key Generator",
    "SWT" : "Switch",
    "CONT" : "Container",
    "ORA" : "Oracle Connector",
    "DB2" : "DB2 Connector",
    "ODBC" : "ODBC Connector",
    "SQL" : "SQL Server Enterprise",
    "SYB" : "Sybase",
    "SP" : "Store Procedure",
    "TER" : "Teradata",
    "COG": "Column Generator",
    "ROG": "Row Generator",
    "DS" : "Data Set",
    "SF" : "Sequential File",
    "LFS": "Lookup File Set",
    "HF": "Hash File",
    "IPC": "Inter Process",
    "LNP": "Link Partitioner",
    "LNC": "Link Collector",
    "DTR": "Data Rule",
    "INV": "Investigate",
    "STD": "Standardize",
    "TRF": "Transformer",
    "ISD_Input": "Information Services Input",
    "ISD_Output": "Information Services Output",
    "HD": "Hierarchical Data",
    "PEEK": "Peek",
    "STL": "Start Loop Activity",
    "ENL": "End Loop Activity",
    "EXH": "Exception Handler",
    "CMD": "Execute Command",
    "NEC": "Nested Condition",
    "NOA": "Notification Activity",
    "RTN": "Routine Activity",
    "SEQ": "Sequencer",
    "TEA": "Terminator Activity",
    "UVA": "User Variables Activity",
    "WFF": "Wait For File Activity"
}
def get_p():
    return P
def get_t():
    return T
def get_s():
    return S
def get_l():
    return L
def get_g():
    return G