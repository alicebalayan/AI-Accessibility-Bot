# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 10)


# %%
p = pd.read_csv("signdata.csv",encoding='ISO-8859-1')
#https://docs.google.com/spreadsheets/d/1Md15oi74S7A2z4d9FWl26bOaYi65GgwQOru6nBzC1eA/edit#gid=1884851278jj['Stream'].isin(options)
p


# %%
test_word = 'here'
test = p.loc[p["EntryID"].str.startswith(test_word + "_", 0) | (p["EntryID"] == test_word)| p["SignBankEnglishTranslations"].str.contains(' ' + test_word + ',') | p["SignBankEnglishTranslations"].str.endswith(" " + test_word) | p["SignBankEnglishTranslations"].str.startswith(test_word + ",")]
test[["EntryID", "LexicalClass"]]


# %%
from bot import *

client.run(TOKEN)


# %%



