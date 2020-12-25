# report.py
#
# Exercise 2.4


from fileparse import parse_csv
import stock
import tableformat
from portfolio import Portfolio

def make_report_data(portfolio, prices):
    
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
            
    return rows


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))
        




def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        #list of stock class
    portfolio = [ stock.stock(d['name'], d['shares'], d['price']) for d in portdicts]

    return Portfolio(portfolio)


    
def print_report(report, formatter):

    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)



    
def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report_data(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)

    

    print_report(report, formatter)
    return 

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfolio, prices format')
    
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)

















