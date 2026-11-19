# Front Page — Thursday 19 November 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](main.py)
[![Image: 1024×1024 PNG](https://img.shields.io/badge/Image-1024%C3%971024%20PNG-green.svg)](entry.png)

Entry for the [make.fun](https://make.fun) bounty
[`news-image-20261119`](https://make.fun/bounty/news-image-20261119):
one image summing up the world news of **Thursday 19 November 2026**.

## The image

A newspaper front page — banner date, headline, four stories:

| Story | Panel |
| --- | --- |
| First-ever Trump–Xi–Putin trilateral summit meets in Shenzhen — nuclear arms on the table | Headline + flags over the Shenzhen skyline |
| GTA VI launches worldwide — Vice City opens | Neon Vice City street |
| Anthropic IPO — record $81.3 billion | Rising stock chart + AI chip |
| Crimea bridge hit again — traffic halted | Smoke over the sea bridge |

The date **THURSDAY 19 NOVEMBER 2026** is printed large at the top and
again in the footer, so the day the image sums up is unmistakable.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
image baked into this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`.
It is deterministic: two runs write byte-identical output, mode `0644`.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Output: `entry.png` — 1024×1024 PNG, 983,206 bytes (under the 1 MiB cap).

## License

MIT — see [LICENSE](LICENSE).
