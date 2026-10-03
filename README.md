# Notes Service

A tiny HTTP service written in Python (standard library only, no dependencies).

## What it does

| Endpoint       | Response                          |
| -------------- | --------------------------------- |
| `GET /`        | A greeting                        |
| `GET /healthz` | `200 ok` (no database)            |
| `GET /notes`   | A hard-coded JSON list of notes   |

## How to run

```
./scripts/run.sh
```

Then open http://localhost:8080/

## Port

The service listens on the port in the `PORT` environment variable and
defaults to **8080**:

```
PORT=9000 ./scripts/run.sh
```

## How to test

```
./scripts/test.sh
```

Exit code 0 means pass; the last line printed is `TESTS: n/n`.
