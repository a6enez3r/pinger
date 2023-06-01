# `pinger` [![pipeline](https://github.com/a6enez3r-sidefx/pinger/actions/workflows/pipeline.yml/badge.svg)](https://github.com/a6enez3r-sidefx/pinger/actions/workflows/pipeline.yml)

package to ping the status of various services 


## `install`

`pinger` can be installed from source :-

```shell
  git clone https://github.com/a6enez3r-sidefx/pinger
  cd pinger
```

- Create a virtual environment & install all dependencies

```shell
  python3 -m venv venv
  source venv/bin/activate
  make deps
```
- Install the CLI itself

```shell
  make pkg-install
```

## `quickstart`

```
Usage: pinger/pinger/__main__.py command [args...]

Commands:
  elasticsearch   Check if Elasticsearch is running
  mysql           Check if MySQL is running
  rabbit          Check if Rabbit MQ is running
  redis           Check if Redis is running
```
