# pcost.py
#
# Exercise 1.27

from stock import stock
from report import read_portfolio

def portfolio_cost(record):

    portfolio = read_portfolio(record)
    return portfolio.total_cost
    


def main(args):
    
    if len(args) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfolio')
    
    filename = args[1]
    
    print('total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)












