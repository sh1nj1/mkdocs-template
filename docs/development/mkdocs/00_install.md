# Mkdocs Material Theme Template 

## Install 

python3, pip3 을 설치한다.

`sudo install python3 python3-pip`

pip 는 version 3 이다.

`pip install -r requirements.txt`

* custom mkdocs-gen-nav-plugin 설치
  - [Mkdocs Gen Nav Plugin - install](plugins/mkdocs_gen_nav_plugin/README.md#install) 에 따라 빌드및 설치
* `get_google_sheet` 매크로 사용을 위한 인증키 파일 처리
  - 해당 매크로 사용하지 않을 경우 불필요및 사용되는 md 파일에서 제거 필요
  - [Get Google Sheet - Google Service API Key](get-google-sheet-macro.md#google-service-api-key) 에 따라 인증키 파일을 다운로드 받아 `~/.config/gspread/service_account.json` 에 복사한다.

구동 

`mkdocs serve -a 0.0.0.0:8000`

## 설정

* mkdocs.yml 에 Google Analytics ID 설정 필요

## Upgrade

[pur](https://pypi.org/project/pur/) 툴을 설치하고 requirements.txt 파일을 업데이트하고, 설치한다.

```
pip install pur
pur -r requirements.txt
pip install -r requirements.txt
```