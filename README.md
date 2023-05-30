# backend

- [backend](#backend)
  - [.vscode 資料夾](#vscode-資料夾)
    - [說明](#說明)
- [建立開發環境](#建立開發環境)
  - [Windows](#windows)
  - [Linux](#linux)
  - [安裝套件](#安裝套件)
  - [建立虛擬環境檔案](#建立虛擬環境檔案)
    - [本地端開發](#本地端開發)

## .vscode 資料夾

### 說明

主要統一一些設定，包含使用哪個自動排版的工具。

# 建立開發環境

## Windows

```shell
py -3.10 -m venv .venv # django
```

## Linux

```shell
python3.10 -m venv .venv
```

## 安裝套件

```shell
pip install -U pip # 更新 pip 版本
pip install -r requirements.txt # 下載套件
```

## 建立虛擬環境檔案

將 `.env.example` 複製成 `.env`，並更改內容。

### 本地端開發

> 跟 manage.py 檔案同一個位置

可以參考 .env.example` 檔案，再複製成 .env。

> 為什麼 DATABASE_URL 可以使用這種方式進行連線呢 ? 這是 `django-environ` 管理環境參數套件的其中一個使用方式。

你可以參考 https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url 官方敘述的使用方式。

你也可以不使用 `django-environ` 的做法，你也可以直接至 `backend/settings.py` 把 `default` 預設連線的資料庫連線資訊手動進行修改。