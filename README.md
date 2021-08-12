# minimal-action

An action to test actions. It's the least an action can do: it accepts a file as input
and writes the same file as output, with the suffix "bak" before the final suffix.

```yaml
actions:
  generate_study_population:
    ...
    outputs:
      highly_sensitive:
        cohort: output/input.csv

  my_minimal_action:
    run: minimal-action:latest output/input.csv
    needs: [generate_study_population]
    outputs:
      highly_sensitive:
        cohort: output/input.bak.csv
```

It is a dependency of the job-runner integration tests.

## Development

Let's not get carried away, minimal-action should be *minimal*. If you must, then...

Create and activate a new virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install `pip-tools` and sync:

```sh
pip install pip-tools
pip-sync
```

`black`, `flake8`, and `isort` are available:

```sh
black .
flake8 .
isort .
```

## Releasing

Simply tag a commit with `bump2version`:

```sh
bump2version minor
```

Don't forget to `git push --tags`.
