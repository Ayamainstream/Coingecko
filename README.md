# Coingecko
Python code which filters out top N cryptocurrencies by market capitalization.
## Installation
### Requirements 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pycoingecko.
```bash
pip install pycoingecko
```
### Clone repository
Then install script by clonning repository.
```bash
git clone https://github.com/Ayamainstream/Coingecko.git
cd Coingecko
```
### Edit path in the script
Provide proper path to the file where data will be saved. You need to edit test.py file. In my case it is:
```python
sys.path.insert(0, '/Users/ayaze/Projects/Assignment1/src')
```
## Usage
```python
cd Coingecko\test
python test.py
```
## Examples
You should input N
```bash
Type N numbers of cryptocurrency markets: 5
['Bitcoin', 'Ethereum', 'Cardano', 'Tether', 'Binance Coin']
```
then it will output N numbers of top cryptocurrencies.
## License
[MIT](https://choosealicense.com/licenses/mit/)
