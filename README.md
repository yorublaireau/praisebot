# PraiseBot

A crappy twitter robot that praises people!

https://twitter.com/praiserbot


![A Tweet from @praiserbot: @thiscodewitch you're the best 👏👏👏](screenshot.png)
https://twitter.com/praiserbot/status/1454783653909835778

Born and raised at [Remote Hack](https://remotehack.space/)

Almost certainly bad and full of bugs.

## Deployment
Running on and continuously deploying to a piku app on a raspberry pi zero.

Connectivity using tailscale vpn - check out [.github/workflows/deploy.yml](.github/workflows/deploy.yml)

## Linting
Linting is handled by [Black](https://github.com/psf/black)

Once installed, you can run it with
```shell
black .
```

## Git hooks
We use [pre-commit](https://pre-commit.com/) hooks to clean our files before committing to git.

The config is in `.pre-commit-config.yaml`.

### Install:
This should be run when cloning the repo, and anytime the config is modified
```shell
pre-commit install
```
### Run on all files
Run this to run the hook against all files. Useful when the config has just been changed
```shell
pre-commit run --all-files
```
### Uninstall
If there is a problem with your hooks, you can uninstall them
```shell
pre-commit uninstall -t pre-commit
```
