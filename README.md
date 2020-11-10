# jython-desktop

## Description
This is a POC project to demonstrate a
jython application running inside a docker container.

## Tech stack
- jdk 7
- jython 2.7
- docker-cli
- xhost

## Docker stack
- alpine:latest

## To run
```xhost +localhost && sudo ./install.sh -u```

## To stop (optional)
```xhost && sudo ./install.sh -d```

## To see help
`sudo ./install.sh -h`
