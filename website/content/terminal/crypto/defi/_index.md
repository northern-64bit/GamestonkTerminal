---
title: Introduction to Cryptocurrency Decentralized Finance (DeFi)
keywords: "cryptocurrency, defi, decentralized finance, crypto, dapps, uniswap, funding, luna, terra, blockchain"
excerpt: "An Introduction to Cryptocurrency DeFi menu, within the Cryptocurrency Menu,
with a brief overview of the features."
geekdocCollapseSection: true
---

The Cryptocurrency Decentralized Finance (DeFi) menu gives the user the ability to delve deeper into borrow and lending rates
(<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/borrow/" target="_blank">borrow</a> and <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/lending/" target="_blank">lending</a>),
Uniswap statistics (<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/tokens/" target="_blank">tokens</a>, <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/stats/" target="_blank">stats</a> and <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/pairs/" target="_blank">pairs</a>),
information about dApps (<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/gdapps/" target="_blank">gdapps</a> and <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/stvl/" target="_blank">stvl</a>)
as well as infomration about terra blockchain (<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/sreturn/" target="_blank">sreturn</a>) and luna (<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/crypto/defi/lcsc/" target="_blank">lcsc</a>).

## How to use

The Cryptocurrency Decentralized Finance (DeFi) menu is called upon by typing `defi`, while inside the `crypto` menu, which opens the following menu:

![Cryptocurrency Decentralized Finance (DeFi) menu](https://user-images.githubusercontent.com/46355364/178734540-716f2232-20a4-4f31-b8a8-10c0badfd5dd.png)

Alternatively, you can also type `/crypto/defi`. Within the Cryptocurrency Decentralized Finance (DeFi) menu you can
find features that delve deeper in the world of decentralized finance. For example, you can look into the funding rates
of the current or last 30 days average with `funding` which returns the following:

```
2022 Jul 13, 08:15 (🦋) /crypto/defi/ $ funding

┏━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ Symbol ┃ Binance    ┃ dYdX         ┃ FTX      ┃ BitMEX  ┃
┡━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│ BTC    │ -0.008009% │ 0.00531744%  │ 0.0016%  │ 0.0092% │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ ETH    │ 0.01%      │ 0.00299744%  │ -0.012%  │ 0.0504% │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ XRP    │ -0.019923% │ –            │ -0.0008% │ 0.0667% │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ BCH    │ -0.008622% │ -0.00606848% │ -0.0496% │ 0.01%   │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ COMP   │ 0.01%      │ 0.00074952%  │ -0.0112% │ –       │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ KNC    │ -0.010541% │ –            │ -0.0048% │ –       │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ LINK   │ -0.000282% │ 0.00989024%  │ 0.004%   │ 0.0551% │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ XTZ    │ -0.035406% │ 0.00790624%  │ -0.0104% │ –       │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ BNB    │ -0.024568% │ –            │ -0.0152% │ 0.0452% │
├────────┼────────────┼──────────────┼──────────┼─────────┤
│ LTC    │ -0.009035% │ -0.00034072% │ -0.0024% │ 0.0187% │
└────────┴────────────┴──────────────┴──────────┴─────────┘
```

## Examples

Delving deeper in Uniswap, we can start bij looking at the tokens trade-able with `tokens`:

```
2022 Jul 13, 08:24 (🦋) /crypto/defi/ $ tokens

                                 UniSwarp DEX Trade-able Tokens
┏━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ index ┃ symbol       ┃ name                       ┃ tradeVolumeUSD ┃ totalLiquidity ┃ txCount ┃
┡━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ 0     │ BID          │ TopBidder                  │ 23.5M          │ 1.9M           │ 2733    │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 1     │ CHI          │ Chi Gastoken by 1inch      │ 19.4M          │ 19.7K          │ 75993   │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 2     │ XDEX         │ XDEFI Governance Token     │ 18.7M          │ 7.8M           │ 4438    │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 3     │ TUSD         │ TrueUSD                    │ 176.2M         │ 37.8K          │ 47385   │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 4     │ LON          │ Tokenlon                   │ 521.8M         │ 1.7M           │ 58951   │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 5     │ dDai         │ Dharma Dai                 │ 0              │ 4              │ 1       │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 6     │ STRIP        │ StripInu2                  │ 0              │ 0              │ 614     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 7     │ GST2         │ Gastoken.io                │ 2.1M           │ 126            │ 10909   │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 8     │ XGME         │ GameStonk.online           │ 0              │ 35.7K          │ 65      │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 9     │ SHKOOBYSHNAX │ SHKOOBY INU SHNAX          │ 0              │ 0              │ 47      │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 10    │ PORN         │ Porn DAO                   │ 2.3M           │ 1.9K           │ 321     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 11    │ TGBP         │ TrueGBP                    │ 24.1K          │ 4K             │ 790     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 12    │ $STEALTH     │ Stealth Standard           │ 9.2M           │ 193.4M         │ 1623    │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 13    │ ADIDAS       │ Adidas Originals Metaverse │ 4.5M           │ 0              │ 488     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 14    │ Nike         │ Nike RTFKT Studio          │ 75.8K          │ 0              │ 15      │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 15    │ DLTA         │ delta.theta                │ 3.1M           │ 4.2M           │ 3006    │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 16    │ Nike         │ Nike Metaverse             │ 4.5M           │ 0              │ 669     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 17    │ Nike         │ Nike RTFKT Studio          │ 131.6K         │ 0              │ 35      │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 18    │ PRADA        │ Prada Metaverse            │ 894.8K         │ 0              │ 196     │
├───────┼──────────────┼────────────────────────────┼────────────────┼────────────────┼─────────┤
│ 19    │ TCAD         │ TrueCAD                    │ 6.5K           │ 650            │ 142     │
└───────┴──────────────┴────────────────────────────┴────────────────┴────────────────┴─────────┘
```

Furthermore, we can also look at the recently added pairs with `pairs`:

```
2022 Jul 13, 08:25 (🦋) /crypto/defi/ $ pairs

                                      Latest Added Pairs on Uniswap DEX
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ created             ┃ pair             ┃ token0        ┃ token1        ┃ volumeUSD ┃ txCount ┃ totalSupply ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 2022-07-12 12:16:52 │ icc/USDT         │ ICC           │ Tether USD    │ 59.4K     │ 356     │ 0           │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-11 13:16:51 │ BOI/WETH         │ Yellow Boi    │ Wrapped Ether │ 233.1K    │ 2256    │ 0           │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-10 20:09:26 │ WOW/WETH         │ LongDoge      │ Wrapped Ether │ 350.2K    │ 1907    │ 316         │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-05 18:08:49 │ Painthereum/WETH │ Painthereum   │ Wrapped Ether │ 652.4K    │ 345     │ 2           │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-05 16:51:52 │ LITx/WETH        │ LITx Token    │ Wrapped Ether │ 171K      │ 161     │ 172.4K      │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-05 11:37:24 │ WETH/SGOLD       │ Wrapped Ether │ Saudi Gold    │ 226.1K    │ 328     │ 1.2M        │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-05 11:33:19 │ DUCKER/WETH      │ Duckereum     │ Wrapped Ether │ 6.1M      │ 10465   │ 29.7K       │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-05 04:23:28 │ WETH/SOIL        │ Wrapped Ether │ Saudi Oil     │ 673.7K    │ 3733    │ 22.4K       │
├─────────────────────┼──────────────────┼───────────────┼───────────────┼───────────┼─────────┼─────────────┤
│ 2022-07-04 21:30:29 │ SKOLL/WETH       │ SKOLL         │ Wrapped Ether │ 328.8K    │ 110     │ 1.2K        │
└─────────────────────┴──────────────────┴───────────────┴───────────────┴───────────┴─────────┴─────────────┘
```

When interested in dApps, it is possible to find the top DeFI dApps grouped by chain with `gdapps`:

![top DeFI dApps grouped by chain](https://user-images.githubusercontent.com/46355364/178734582-c9b96ce5-e0d5-4913-9e7d-ced35e4118d7.png)

Including a list of recent dApps with `ldapps`:

```
2022 Jul 13, 08:28 (🦋) /crypto/defi/ $ ldapps

┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name                     ┃ Symbol ┃ Category       ┃ Chains                                          ┃ Change 1H (%) ┃ Change 1D (%) ┃ Change 7D (%) ┃ TVL ($) ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ MakerDAO                 │ MKR    │ CDP            │ Ethereum                                        │ 0.17          │ -0.22         │ -5.41         │ 7.371 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ Polygon Bridge & Staking │ MATIC  │ Chain          │ Polygon                                         │ -0.09         │ -0.80         │ 3.40          │ 5.692 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ Curve                    │ CRV    │ Dexes          │ Ethereum, Polygon, Avalanche, Fantom, Arbitrum, │ 0.12          │ -0.15         │ -1.19         │ 5.049 B │
│                          │        │                │ xDai, Optimism, Moonbeam, Harmony, Aurora       │               │               │               │         │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ WBTC                     │ WBTC   │ Bridge         │ Ethereum                                        │ 0.24          │ 0.59          │ -5.71         │ 4.925 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ Uniswap                  │ UNI    │ Dexes          │ Ethereum, Polygon, Arbitrum, Optimism           │ 0.50          │ 0.20          │ -4.14         │ 4.840 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ Lido                     │ LDO    │ Liquid Staking │ Ethereum, Solana, Moonriver, Terra              │ 0.57          │ 1.17          │ -4.47         │ 4.674 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ AAVE V2                  │ AAVE   │ Lending        │ Ethereum, Polygon, Avalanche                    │ 0.23          │ -1.02         │ -20.37        │ 4.249 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ Convex Finance           │ CVX    │ Yield          │ Ethereum                                        │ 0.04          │ -0.33         │ 0.54          │ 3.298 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ JustLend                 │ JST    │ Lending        │ Tron                                            │ 0.08          │ -0.63         │ 15.14         │ 3.191 B │
├──────────────────────────┼────────┼────────────────┼─────────────────────────────────────────────────┼───────────────┼───────────────┼───────────────┼─────────┤
│ PancakeSwap              │ CAKE   │ Dexes          │ Binance                                         │ 0.14          │ 0.34          │ -4.40         │ 2.818 B │
└──────────────────────────┴────────┴────────────────┴─────────────────────────────────────────────────┴───────────────┴───────────────┴───────────────┴─────────┘
```
