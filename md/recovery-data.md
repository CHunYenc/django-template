# 備份及還原資料

`20230204` - 以下內容是做記錄用, 因為還不穩定。

## 全部備份

```shell
python manage.py dumpdata --natural-foreign --exclude auth.permission \--exclude contenttypes --exclude admin.logentry --exclude sessions --indent 2 > apps/app_name/fixtures/default.json
```

## 個別備份

### 使用者備份

```shell
python manage.py dumpdata app_name.User --natural-foreign --indent 2 > apps/app_name/fixtures/users.json --settings=backend.settings-local
```

### 群組備份

```shell
python manage.py dumpdata auth.group app_name.decoratedgroup --natural-foreign --indent 2 > apps/app_name/fixtures/groups.json
```

### 頁面備份

```shell
python manage.py dumpdata app_name.page --natural-foreign --indent 2 > apps/app_name/fixtures/pages.json
```

## 全部還原

還原 `使用者`, `群組`

```shell
python manage.py loaddata /Users/work/program/backend-template/apps/app_name/fixtures/default.json
```
