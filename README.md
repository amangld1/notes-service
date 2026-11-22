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

## Example

Check that the service is alive: curl localhost:8080/healthz

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s
    git revert <commit>
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
