# minimal-action

An action to test actions. It's the least an action can do: it accepts a file as input
and writes the same file as output, with a configurable suffix (".bak" by default) before the final suffix.

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
uv run ruff check
uv run ruff format
```

## Releasing

A [GitHub action workflow](.github/workflows/tag.yaml) automatically tags the
action on pushes to main.
