# CodeBuild last event logs

```yaml
steps:
- uses: actions/checkout@master
- name: Run action
  id: myaction
  uses: stumason/codebuild-logs@master
  with:
    AWS_KEY: ${{ secrets.AWS_KEY }}
    AWS_SECRET: ${{ secrets.AWS_SECRET }}
    AWS_REGION: ${{ secrets.AWS_REGION }}
    CODEBUILD_PROJET_NAME: ${{ secrets.PROJECT }}
```