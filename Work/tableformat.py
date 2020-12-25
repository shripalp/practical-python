#tableformat.py

class tableformatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()


    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class texttableformatter(tableformatter):

    '''
    Output data in plain-text format.
    '''
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
        
    def row(self, rowdata):   
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

    
class csvtableformatter(tableformatter):
        
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        print(','.join(rowdata))

class htmltableformatter(tableformatter):

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class formaterror(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = texttableformatter()
    elif fmt == 'csv':
        formatter = csvtableformatter()
    elif fmt == 'html':
        formatter = htmltableformatter()
    else:
        raise formaterror(f'Unknown table format %s' %fmt)
    return formatter

def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)




    

    

