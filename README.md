# makefun-news20

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/woodhntr1-gif/makefun-news20/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/woodhntr1-gif/makefun-news20/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

The World in One Image — 20 November 2026. A one-page newspaper front page drawn entirely in code (Pillow) that sums up the world's news of Friday, 20 November 2026, in a single 1024×1024 image.

What the picture holds: the lead story is the International Court of Justice ruling that Myanmar committed genocide against the Rohingya, illustrated with a small geometric drawing of the Peace Palace in The Hague. Six cards below it cover the Trump–Xi–Putin joint declaration from Shenzhen ("a nuclear war cannot be won"), Russia's overnight missile barrage on Kyiv, the Houthi missile that damaged Riyadh's PIF tower, the market slide (S&P about −2%, Nikkei −4.8%), the COP31 draft dropping the fossil-fuel phase-out, and Cyclone Akvan making landfall in Odisha. A strip of six short briefs follows: Kenya discharging its last Ebola patient, Israeli troops crossing the Gaza Yellow Line, a tanker burning in Hormuz after hitting a mine, GTA VI making $3.79bn on its first day, the second EU–UK summit in Brussels, and the White House firing its cyber chief.

The news was taken from reporting by the WSJ, CNN, Reuters, AP, BBC, Fox and the NY Post on 20 November 2026. Honest note: this entry was built on 21 November 2026 and covers news reported on 20 November 2026, before that day's deadline. The drawing is fully deterministic — rendering it twice produces byte-identical output.

## Run it

```sh
python3 main.py
```

That copies the pre-rendered `entry.png` (1024×1024) into the working directory, or into `$MAKEFUN_OUTPUT_DIR` when it is set. Nothing is drawn while the program runs — `render.py` documents how the picture was drawn (Pillow, fully deterministic), and `main.py` only copies the exact bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rez34v58&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
