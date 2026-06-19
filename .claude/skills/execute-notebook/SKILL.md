---
description: Execute a Jupyter notebook in-place (re-runs all cells and saves outputs)
---

Run all cells in a notebook and save outputs back to the file:

```
python -m jupyter nbconvert --to notebook --execute --inplace <notebook.ipynb>
```

If no notebook is specified in the prompt, execute the notebook currently open in the IDE (or ask the user which one to run if ambiguous).

Report the output file size written and flag any cell execution errors.
