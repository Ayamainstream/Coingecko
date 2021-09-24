import sys
sys.path.insert(0, '/Users/ayaze/Projects/Assignment1/src')
from coingecko import collect

N = int(input("Type N numbers of cryptocurrency markets: "))
result = collect(N)