# Visuals Repo

Each figure lives as a versioned Jupyter notebook (`*_v1.ipynb`, `*_v2.ipynb`, ...) committed with outputs so old visuals remain viewable in git history.

## Iteration workflow

1. Copy the previous notebook to the next version (e.g. `cp billionaire_wealth_chart_v1.ipynb billionaire_wealth_chart_v2.ipynb`)
2. Make changes and run all cells
3. Commit the new notebook with outputs included

## What's tracked / ignored

- `.ipynb` files — tracked **with outputs** (this is intentional; the embedded visual is the record)
- `.ipynb_checkpoints/` — gitignored
- `.png`, `.jpg`, `.jpeg` — gitignored (visuals live in notebooks, not as loose files)