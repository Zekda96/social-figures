---
description: Research and add a new row (person, job, or asset) to the billionaire wealth chart dataset
---

The user proposes a candidate entry — a person, job title, or asset class — whose median or approximate annual income or net worth should appear as a bar in the chart.

## Steps

1. **Assess narrative fit** before researching. Ask: does this entry add a meaningful reference point for the audience? If the value will be visually indistinguishable from an existing entry at the scales used in slides 2–4, flag it.

2. **Research the value** using WebSearch. Look for a specific, citable figure from a credible source (BLS, Fed SCF, Glassdoor, Forbes, Bloomberg, Equilar, Census Bureau). Prefer 2024 or 2025 data. Note whether the figure is annual income/pay or net worth — the chart mixes both, but the label must be explicit.

3. **Determine the group** based on the value in USD billions:
   - `GROUP_BELOW` — below $1B (most income and net-worth reference points)
   - `GROUP_1B_10B` — $1B–$10B (celebrities, athletes, public figures)
   - `GROUP_MULTI` — multi-billionaires with election-day + today values
   - `GROUP_MUSK` — Elon Musk only (three-bar: election-day, pre-IPO, today)

4. **Add the entry** to the correct group's `items` list in `billionaire_wealth_chart_v4.ipynb`, maintaining richest-first order. For `GROUP_BELOW` and `GROUP_1B_10B` the tuple is `(label, value_in_billions)`. Append `(annual pay)` or `(net worth)` to the label if not obvious from the name.

5. **Add the source** to `sources.md` under the appropriate section (create one if needed). Include: source name, year, the specific figure used, and the URL.

6. **Update the footnote** in `draw_chart` inside `billionaire_wealth_chart_v4.ipynb` if a new data provider was used that isn't already cited there.

7. **Re-execute the notebook** using the `execute-notebook` skill.