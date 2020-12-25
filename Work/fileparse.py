# fileparse.py
#
# Exercise 3.3

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    import csv
    
    
    indices =[]
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []
    
    if select: #if option is available
        indices = [headers.index(colname) for colname in select] #creat a list indices which has index of selected columns from headers
        headers = select
        
        #if types is specified


    records = [] # create empty list of records
    for rowno, row in enumerate(rows, 1):
        if not row: #skip row with no data
            continue
            #filter the row if specific columns were selected

        if select:
            row = [ row[index] for index in indices ]
            #apply types formatting
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue
        if headers:
            try:
                record = dict(zip(headers, row)) #ceate a dictionary with keys: value
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue
        else:
            record = (row[0], row[1])
        records.append(record)
    return records




