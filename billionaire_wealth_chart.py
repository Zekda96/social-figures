"""
Comparative wealth chart: US billionaires before the 2024 election vs. today.

Two data points per person:
  - Net worth at Election Day (Nov 5, 2024)
  - Net worth today (mid-June 2026)

Musk gets a third bar showing his wealth just before the SpaceX IPO (Jun 12, 2026),
when he was worth ~$813B (Bloomberg/Forbes). The IPO pushed him past $1 trillion.

Figures are in USD billions. Election-day values are approximate.
Zuckerberg's figure declined, so its label is negative.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

# name -> (net worth Nov 5 2024, net worth today), in USD billions
data = {
    "Elon Musk":      (264, 1260),
    "Larry Page":     (150,  281),
    "Sergey Brin":    (142,  261),
    "Jeff Bezos":     (206,  249),
    "Larry Ellison":  (175,  201),
    "Michael Dell":   (118,  165),
    "Mark Zuckerberg":(201,  187),
}

MUSK_PRE_IPO = 813  # net worth just before SpaceX IPO, ~Jun 2026 (Bloomberg/Forbes est.)

# Sort by current wealth so the chart reads top-to-bottom richest-first.
order = sorted(data.items(), key=lambda kv: kv[1][1], reverse=True)
names = [k for k, _ in order]
before = np.array([v[0] for _, v in order], dtype=float)
now = np.array([v[1] for _, v in order], dtype=float)
pct = (now - before) / before * 100.0

musk_idx = names.index("Elon Musk")

y = np.arange(len(names))
bar_h = 0.26

fig, ax = plt.subplots(figsize=(13, 7.5))

# Election Day bars (all people, top slot)
bars_before = ax.barh(y + bar_h, before, height=bar_h,
                      label="Election Day (Nov 5, 2024)",
                      color="#9aa7b4")

# Pre-IPO bar (Musk only, middle slot)
bar_pre_ipo = ax.barh(musk_idx, MUSK_PRE_IPO, height=bar_h,
                      label="Pre-SpaceX IPO (Jun 2026)",
                      color="#f0a030")

# Today bars (all people, bottom slot)
bars_now = ax.barh(y - bar_h, now, height=bar_h,
                   label="Today (Jun 2026)",
                   color="#1f6feb")

# Value labels on election-day bars.
for b in bars_before:
    w = b.get_width()
    ax.text(w + 8, b.get_y() + b.get_height() / 2,
            f"${w:,.0f}B", va="center", ha="left", fontsize=9, color="#555")

# Pre-IPO label with % change from Election Day.
pct_pre = (MUSK_PRE_IPO - before[musk_idx]) / before[musk_idx] * 100
b0 = bar_pre_ipo[0]
ax.text(MUSK_PRE_IPO + 8, b0.get_y() + b0.get_height() / 2,
        f"${MUSK_PRE_IPO:,.0f}B  (+{pct_pre:.0f}%)",
        va="center", ha="left", fontsize=9, fontweight="bold", color="#a06000")

# % change tip on the current-wealth bars.
for b, p in zip(bars_now, pct):
    w = b.get_width()
    sign = "+" if p >= 0 else ""
    color = "#137333" if p >= 0 else "#b3261e"
    ax.text(w + 8, b.get_y() + b.get_height() / 2,
            f"${w:,.0f}B  ({sign}{p:.0f}%)",
            va="center", ha="left", fontsize=9, fontweight="bold", color=color)

ax.set_yticks(y)
ax.set_yticklabels(names)
ax.invert_yaxis()  # richest at top
ax.set_xlabel("Net worth (USD billions)")
ax.set_title("US Billionaire Wealth: Election Day 2024 vs. Today",
             fontsize=15, fontweight="bold", pad=14)
ax.set_xlim(0, max(now) * 1.18)
ax.legend(loc="lower right", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.4)

fig.text(0.01, 0.01,
         "Source: Bloomberg/Forbes (approx.). Election-day values estimated. "
         "Musk pre-IPO figure from Bloomberg Billionaires Index, ~Jun 11 2026.",
         fontsize=7, color="#888")

plt.tight_layout()

def _next_version(directory: str, stem: str) -> int:
    import re
    pattern = re.compile(rf"^{re.escape(stem)}_v(\d+)\.png$")
    versions = [
        int(m.group(1))
        for f in os.listdir(directory)
        if (m := pattern.match(f))
    ]
    return max(versions, default=0) + 1

out_dir = os.path.dirname(os.path.abspath(__file__))
version = _next_version(out_dir, "billionaire_wealth_chart")
out_path = os.path.join(out_dir, f"billionaire_wealth_chart_v{version}.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved chart to {out_path}")
