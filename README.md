# Show Management Platform

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
- `sam local start-lambda` start a persistent local emulation of a Lambda service at http://127.0.0.1:3001 by default
- `sam deploy --guided`
- `sam deploy --config-env <env_name>` environments are different logical groupings of config. This feature can be used if environments are specified on samconfig.toml.

### GitHub Actions

- Protect main branch from pushes and require status checks to pass in order to create PR
- Create separate CI/CD files for push to non-main branch, PR against main, and push to main.
- Store AWS credentials in GitHub Secrets (Switch to OIDC later)
- Parallelize format, lint, security-scan, test, and build jobs. Make deploy job depend on each of the previous jobs.

### Testing

- pytest for unit testing
- bash script for e2e testing after deployment to dev environment

## Developer Setup

## Tips

- Create two proxy configurations, one for root (/shows), and one to all subpaths (/shows/123)
- Use CloudFormation output for APIGW url to dynamically populate BASE_URL of e2e_tests.sh at runtime
