# CodeBuild last event logs

```yaml
steps:
- uses: actions/checkout@master
- name: Run codebuild logs action
  id: codebuild-event-logs
  uses: stumason/codebuild-logs@v1
  env:
    aws-access-key-id: ${{ secrets.AWS_KEY }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET }}
    aws-region: ${{ secrets.AWS_REGION }}
    codebuild-project-name: ${{ secrets.PROJECT }}
```

### Output

Puts something like the following in your github actions log:

```txt
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase context status code:  Message:
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Entering phase INSTALL
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase complete: INSTALL State: SUCCEEDED
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase context status code:  Message:
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Entering phase PRE_BUILD
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase complete: PRE_BUILD State: SUCCEEDED
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Phase context status code:  Message:
2021-03-17 11:40:59: [Container] 2021/03/17 11:40:55 Entering phase BUILD
```
