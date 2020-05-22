import discord
import pandas as pd
import yfinance as yf
import os
import datetime
import requests
import COVID19Py
from discord.ext import commands
from GoogleNews import GoogleNews
import pandas_datareader.data as web
from pandas_datareader import wb


os.system("title WallSt Discord Bot v1.0")
client = commands.Bot(command_prefix = '.')
covid19 = COVID19Py.COVID19(data_source="jhu") #Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)



@client.event
async def on_ready():
    print('''

_    _       _ _ _____ _    ______       _   
| |  | |     | | /  ___| |   | ___ \     | |  
| |  | | __ _| | \ `--.| |_  | |_/ / ___ | |_ 
| |/\| |/ _` | | |`--. \ __| | ___ \/ _ \| __|
\  /\  / (_| | | /\__/ / |_  | |_/ / (_) | |_ 
 \/  \/ \__,_|_|_\____/ \__| \____/ \___/ \__|
                                              

Version: 1.0
Author: Bruno Lazaro

The Bot is ready!                           ''')




#future value
@client.command()
async def fvalue(ctx, periods, starting, interest):
    x = float(periods)
    y = float(starting)
    z = float(interest)
    result = (y*(1+z)**x)
    await ctx.send(f'The Future Value is {round(result, 2)}')

#present value
@client.command()
async def pvalue(ctx, periods, future, interest):
    x = float(periods)
    y = float(future)
    z = float(interest)
    result = (y/(1+z)**x)
    await ctx.send(f'The Present Value is {round(result, 2)}')

#help command
client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(title="List of Commands")
    embed.colour = discord.Colour.from_rgb(166, 245, 255)
    embed.add_field(name="Shows the ping of the BOT", value=".ping", inline=False)
    embed.add_field(name="Shows information about a company", value=".about TICKER",inline=False)
    embed.add_field(name="Shows the statistics of a company", value=".stats TICKER",inline=False)
    embed.add_field(name="Show the summary of a company", value=".sum TICKER",inline=False)
    embed.add_field(name="Shows the dividends of a company", value=".dividends TICKER", inline=False)
    embed.add_field(name="Shows the splits of a company", value=".splits TICKER", inline=False)
    embed.add_field(name="Shows the major holders of a company", value=".major_holders TICKER",inline=False)
    embed.add_field(name="Shows the institutional holders of a company", value=".institutional_holders TICKER",inline=False)
    embed.add_field(name="Shows historical data of a company", value=".hist TICKER",inline=False)
    embed.add_field(name="Shows the recommendations of a company", value=".recommendations TICKER",inline=False)
    embed.add_field(name="Shows the next event of a company", value=".calendar TICKER",inline=False)
    embed.add_field(name="Shows the International Securities Identification Number of a company", value=".isin TICKER",inline=False)
    embed.add_field(name="Shows the sustainability of a company", value=".sustainability TICKER",inline=False)
    embed.add_field(name="Shows the options expiration date of a company", value=".options TICKER",inline=False)
    embed.add_field(name="Shows the S&P500 Index historical price", value=".sp500",inline=False)
    embed.add_field(name="Shows the GDP of a Country", value=".gdp COUNTRY_CODE",inline=False)
    embed.add_field(name="Shows the population of a Country", value=".population COUNTRY_CODE",inline=False)
    embed.add_field(name="Shows the life expectancy of a Country", value=".life COUNTRY_CODE",inline=False)
    embed.add_field(name="Shows the exports of goods and services of a Country", value=".exports COUNTRY_CODE",inline=False)
    embed.add_field(name="Shows the total unemployment of a Country", value=".unemployment COUNTRY_CODE",inline=False)
    embed.add_field(name="Calculates the future value", value=".fvalue periods starting_amount interest",inline=False)
    embed.add_field(name="Calculates the present value", value=".pvalue periods final_amount interest",inline=False)
    embed.add_field(name="Shows CoronaVirus (COVID-19) cases in a Country", value=".covid COUNTRY_CODE",inline=False)
    embed.add_field(name="Search for News", value=".search TEXT",inline=False)
    embed.set_footer(text="WallSt Bot made by Bruno Lazaro.")
    embed.set_author(name="WallSt Bot v1.0", icon_url="https://cdn.discordapp.com/avatars/712712331208949880/1e1953ad4edd8aaf8c42d638d2d16287.png")
    await ctx.send(embed=embed)


#ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Hi! My ping is {round(client.latency * 1000)}ms')


#dividends
@client.command()
async def dividends(ctx,*,message):
    stock1 = yf.Ticker(message)
    await ctx.send(f'Dividends of **{message}**\n```{stock1.dividends}```')


#splits
@client.command()
async def splits(ctx,*,message):
    stock2 = yf.Ticker(message)
    await ctx.send(f'Splits of **{message}**\n```{stock2.splits}```')    


#major_holders
@client.command()
async def major_holders(ctx,*,message):
    stock3 = yf.Ticker(message)
    await ctx.send(f'Major Holders of **{message}**\n```{stock3.major_holders}```')

#institutional_holders
@client.command()
async def institutional_holders(ctx,*,message):
    stock4 = yf.Ticker(message)
    await ctx.send(f'Institutional Holders of **{message}**\n```{stock4.institutional_holders}```')

#historical market data
@client.command()
async def hist(ctx,*,message):
    stock5 = yf.Ticker(message)
    await ctx.send(f'Historical data of **{message}**\n```{stock5.history(period="1mo")}```')

#recommendations
@client.command()
async def recommendations(ctx,*,message):
    stock6 = yf.Ticker(message)
    await ctx.send(f'Recommendations of **{message}**\n```{stock6.recommendations}```')


#calendar
@client.command()
async def calendar(ctx,*,message):
    stock7 = yf.Ticker(message)
    await ctx.send(f'Earnings Calendar of **{message}**\n```{stock7.calendar}```')

#International Securities Identification Number
@client.command()
async def isin(ctx,*,message):
    stock8 = yf.Ticker(message)
    await ctx.send(f'The ISIN of **{message}** is `{stock8.isin}`')

#sustainability
@client.command()
async def sustainability(ctx,*,message):
    stock9 = yf.Ticker(message)
    await ctx.send(f'Sustainability of **{message}**\n```{stock9.sustainability}```')

#options expiration
@client.command()
async def options(ctx,*,message):
    stock10 = yf.Ticker(message)
    await ctx.send(f'Options Expiration dates of **{message}**\n```{stock10.options}```')

#sp500
@client.command()
async def sp500(ctx):
    pd.core.common.is_list_like = pd.api.types.is_list_like
    start = datetime.datetime(2020, 5, 1) #change every month
    end = datetime.datetime(2020, 12, 31)
    SP500 = web.DataReader(['sp500'], 'fred', start, end)
    await ctx.send(f'**S&P 500 Index** - Historical Price```{SP500}```')

#gdp
@client.command()
async def gdp(ctx,*,message):
    matches = wb.search('gdp.*capita.*const')
    dat = wb.download(indicator='NY.GDP.MKTP.CD', country=[message], start=1999, end=2030)
    gdp=dat/1000000000000
    await ctx.send(f'**{message} GDP** in USD trillions```{gdp}```')

#population
@client.command()
async def population(ctx,*,message):
    dat = wb.download(indicator='SP.POP.TOTL', country=[message], start=1999, end=2030)
    pop = dat/1000000
    await ctx.send(f'**Population of {message}** in millions```{pop}```')

#life expectancy
@client.command()
async def life(ctx,*,message):
    dat = wb.download(indicator='SP.DYN.LE00.IN', country=[message], start=1999, end=2030)
    await ctx.send(f'**Life expectancy of {message}**```{dat}```')

#exports of goods and services
@client.command()
async def exports(ctx,*,message):
    dat = wb.download(indicator='NE.EXP.GNFS.ZS', country=[message], start=1999, end=2030)
    await ctx.send(f'**Exports of Goods and Services of {message}** (% of GDP)```{dat}```')

#total unemployment
@client.command()
async def unemployment(ctx,*,message):
    dat = wb.download(indicator='SL.UEM.TOTL.ZS', country=[message], start=1999, end=2030)
    await ctx.send(f'**Total unemployment of {message}** (% of total labor force)```{dat}```')

#hospital beds
@client.command()
async def beds(ctx,*,message):
    dat = wb.download(indicator='SH.MED.BEDS.ZS', country=[message], start=1999, end=2030)
    await ctx.send(f'**Hospital beds in {message}** per 1,000 people```{dat}```')


#covid19
@client.command()
async def covid(ctx,*,message):
    location = covid19.getLocationByCountryCode(f"{message}")
    embed = discord.Embed()
    embed.colour = discord.Colour.from_rgb(255, 247, 50)
    embed.add_field(name="Confirmed", value=(location[0]["latest"]["confirmed"]), inline=True)
    embed.add_field(name="Deaths", value=(location[0]["latest"]["deaths"]), inline=True)
    embed.add_field(name=f"{location[0]['country']} Population", value=(location[0]["country_population"]), inline=True)
    embed.set_footer(text="Data fromJohns Hopkins CSSE")
    embed.set_author(name=f"Coronavirus (COVID-19) Cases | {location[0]['country']}", icon_url="https://i.imgur.com/L0DVWUy.jpg")
    embed.set_image(url="https://s7.gifyu.com/images/giphy029c766c4b20b6fc.gif")
    await ctx.send(embed=embed)

#search google news
@client.command()
async def search(ctx,*,message):
    googlenews = GoogleNews(lang='en', period='d')
    googlenews.search(message)
    result = googlenews.gettext()
    embed = discord.Embed()
    embed.colour = discord.Colour.from_rgb(255, 225, 135)
    embed.set_author(name="Google NEWS", icon_url="https://i.imgur.com/tDLGRiT.jpg")
    embed.set_footer(text="Data from Google News | WallSt Bot made by Bruno Lazaro.")
    embed.add_field(name=f"{message} News", value=(f'{result[1]}\n\n{result[2]}\n\n{result[3]}\n\n{result[4]}\n\n{result[5]}\n\n{result[6]}'), inline=False)
    await ctx.send(embed=embed)
    googlenews.clear()

#about
@client.command()
async def about(ctx,*,message):
    stock11 = yf.Ticker(message)
    #print (stock11.info)
    embed = discord.Embed(title=f"About {stock11.info['shortName']}")
    embed.colour = discord.Colour.from_rgb(255, 0, 0)
    embed.add_field(name="Full Name", value=f"{stock11.info['longName']}",inline=True)
    embed.add_field(name="Ticker Symbol", value=f"{stock11.info['symbol']}",inline=True)
    embed.add_field(name="Country", value=f"{stock11.info['country']}",inline=True)
    embed.add_field(name="Sector", value=f"{stock11.info['sector']}",inline=True)
    embed.add_field(name="Industry", value=f"{stock11.info['industry']}",inline=True)
    embed.add_field(name="Full Time Employees", value=f"{stock11.info['fullTimeEmployees']}",inline=True)
    embed.add_field(name="Website", value=f"{stock11.info['website']}",inline=False)
    embed.set_footer(text="Data from Yahoo Finance | WallSt Bot made by Bruno Lazaro.")
    embed.set_author(name="WallSt Bot v1.0", icon_url="https://cdn.discordapp.com/avatars/712712331208949880/1e1953ad4edd8aaf8c42d638d2d16287.png")
    embed.set_thumbnail(url=f"{stock11.info['logo_url']}")
    await ctx.send(embed=embed)

#statistics
@client.command()
async def stats(ctx,*,message):
    stock11 = yf.Ticker(message)
    embed = discord.Embed(title=f"Statistics of {stock11.info['shortName']}")
    embed.colour = discord.Colour.from_rgb(255, 0, 0)
    embed.add_field(name="Trailing Annual Dividend Yield", value=f"{stock11.info['trailingAnnualDividendYield']}",inline=True)
    embed.add_field(name="Trailing Annual Dividend Rate", value=f"{stock11.info['trailingAnnualDividendRate']}",inline=True)
    embed.add_field(name="Dividend Yield", value=f"{stock11.info['dividendYield']}",inline=True)
    embed.add_field(name="Forward EPS", value=f"{stock11.info['forwardEps']}",inline=True)
    embed.add_field(name="Trailing EPS", value=f"{stock11.info['trailingEps']}",inline=True)
    embed.add_field(name="Payout Ratio", value=f"{stock11.info['payoutRatio']}",inline=True)
    embed.add_field(name="Beta", value=f"{stock11.info['beta']}",inline=True)
    embed.add_field(name="Shares Outstanding", value=f"{stock11.info['sharesOutstanding']}",inline=True)
    embed.add_field(name="Market Cap", value=f"{stock11.info['marketCap']}",inline=True)
    embed.add_field(name="Price to Sales Trailing 12 Months", value=f"{stock11.info['priceToSalesTrailing12Months']}",inline=True)
    embed.add_field(name="Forward PE", value=f"{stock11.info['forwardPE']}",inline=True)
    embed.add_field(name="Book Value", value=f"{stock11.info['bookValue']}",inline=True)
    embed.add_field(name="Profit Margins", value=f"{stock11.info['profitMargins']}",inline=True)
    embed.add_field(name="Enterprise to EBITDA", value=f"{stock11.info['enterpriseToEbitda']}",inline=True)
    embed.add_field(name="Enterprise Value", value=f"{stock11.info['enterpriseValue']}",inline=True)
    embed.add_field(name="Short Ratio", value=f"{stock11.info['shortRatio']}",inline=True)
    embed.add_field(name="Price to Book", value=f"{stock11.info['priceToBook']}",inline=True)
    embed.add_field(name="PEG Ratio", value=f"{stock11.info['pegRatio']}",inline=True)
    embed.set_footer(text="Data from Yahoo Finance | WallSt Bot made by Bruno Lazaro.")
    embed.set_author(name="WallSt Bot v1.0", icon_url="https://cdn.discordapp.com/avatars/712712331208949880/1e1953ad4edd8aaf8c42d638d2d16287.png")
    embed.set_thumbnail(url=f"{stock11.info['logo_url']}")
    await ctx.send(embed=embed)

#summary
@client.command()
async def sum(ctx,*,message):
    stock12 = yf.Ticker(message)
    await ctx.send(f'Summary of **{stock12.info["shortName"]}**\n```{stock12.info["longBusinessSummary"]}```')


#bot token
client.run('token here') #add token here
