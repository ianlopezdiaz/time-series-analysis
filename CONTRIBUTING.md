# Contributing

Suggestions, corrections, and improvements are welcome.

## Reporting issues

If you find an error, a broken notebook, or an idea for expanding the
project, open an issue describing what's wrong or what you'd like to see.

## Submitting changes

1. Fork the repository and create a branch for your change.
2. Keep notebooks under `notebooks/<NN>_<section>/`, following the existing
   naming convention.
3. If you add reusable logic, put it in the `ts/` package rather than
   duplicating it across notebooks, and add a corresponding test under
   `tests/`.
4. Before opening a pull request, confirm your notebook(s) execute cleanly,
   e.g. with `jupyter nbconvert --to notebook --execute --inplace <path>`.
   `./scripts/publish.sh` also renders and publishes the site to GitHub
   Pages — don't run it as part of routine testing.
