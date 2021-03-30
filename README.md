# CodeBuild last event logs

```yaml
steps:
- uses: actions/checkout@master
- name: Run codebuild logs action
  id: codebuild-event-logs
  uses: stumason/codebuild-logs@v1
  with:
    aws-access-key-id: ${{ secrets.AWS_KEY }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET }}
    aws-region: ${{ secrets.AWS_REGION }}
    codebuild-project-name: ${{ secrets.PROJECT }}
```