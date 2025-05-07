# Show Content Platform

## Initial Steps I took to scaffold the project

### Poetry

- `poetry init`
- `poetry shell`
- `poetry add --group dev pre-commit`

### Pre-commit Hooks

- `pre-commit install`
- create .pre-commit-config.yaml file and set up hooks from pre-commit hooks, black, ruff, and mypy

### AWS SAM

- `sam init`
- start Docker Desktop
- `sam build --use-container`
- `sam local invoke <name_of_resource_in_template_file> --event <path_to_file>` to invoke the Lambda locally
- `sam sync --stack-name <stack_name> --watch` to keep deployed infra and Lambda code in sync with local
- `sam deploy --guided`
- `sam deploy --config-env <env_name>` environments are different logical groupings of config. This feature can be used if environments are specified on samconfig.toml.

## Developer Setup

-
