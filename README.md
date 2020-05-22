# WallSt Discord Bot
My first Discord bot, written in Python! This bot has multiple functions that might help students that are having online classes in Discord.


Requirements
------------

* [Python](https://www.python.org) >= 3.4+
* [Pandas](https://github.com/pydata/pandas)
* [Numpy](http://www.numpy.org) >= 1.11.1
* [requests](http://docs.python-requests.org/en/master/) >= 2.14.2
* [yfinance](https://pypi.org/project/yfinance/)
* [COVID19Py](https://pypi.org/project/COVID19Py/)
* [discord.py](https://pypi.org/project/discord.py/)

Commands List
-------------
| Commmand | Description | Example | 
| --- | --- |--- |
| `.help` | Shows the full list of commands | `.help` |
| `.ping` | Shows the ping of the BOT | `.ping` |
| `.about TICKER` | Shows information about a company | `.about AAPL` |
| `.stats TICKER` | Shows the statistics of a company | `.stats TSLA` |
| `.sum TICKER` | Shows the full list of commands | `.sum MSFT` |
| `.dividends TICKER` | Shows the dividends of a company | `.dividends AAPL` |
| `.splits TICKER` | Shows the splits of a company | `.splits AAPL` |
| `.major_holders TICKER` | Shows the major holders of a company | `.major_holders TSLA` |
| `.institutional_holders TICKER` | Shows the institutional holders of a company | `.institutional_holders TSLA` |
| `.hist TICKER` | Shows historical data of a company | `.hist MSFT` |
| `.recommendations TICKER` | Shows the recommendations of a company | `.recommendations MSFT` |
| `.calendar TICKER` | Shows the next event of a company | `.calendar AAPL` |
| `.isin TICKER` | Shows the International Securities Identification Number of a company | `.isin AAPL` |
| `.sustainability TICKER` | Shows the sustainability of a company | `.sustainability TSLA` |
| `.options TICKER` | Shows the options expiration date of a company | `.options AAPL` |
| `.sp500` | Shows the S&P500 Index historical price | `.sp500` |
| `.gdp COUNTRY_CODE` | Shows the GDP of a Country | `.gdp US` |
| `.population COUNTRY_CODE` | Shows the population of a Country | `.population GB` |
| `.life COUNTRY_CODE` | Shows the life expectancy of a Country | `.life PT` |
| `.exports COUNTRY_CODE` | Shows the exports of goods and services of a Country | `.exports BR` |
| `.unemployment COUNTRY_CODE` | Shows the total unemployment of a Country | `.unemployment ES` |
| `.exports COUNTRY_CODE` | Shows the exports of goods and services of a Country | `.exports BR` |
| `.fvalue periods starting_amount interest` | Calculates the future value | `.fvalue 12 1000 0.02` |
| `.pvalue periods final_amount interest` | Calculates the present value | `.pvalue 6 500 0.01` |
| `.covid COUNTRY_CODE` | Shows CoronaVirus (COVID-19) cases in a Country | `.covid US` |
| `.search TEXT` | Search for News | `.search football` |

License
-------------
    MIT License

    Copyright (c) 2020 Eduard Nikoleisen

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
