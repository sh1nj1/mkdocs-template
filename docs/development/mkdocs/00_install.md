# Mkdocs Material Theme Template 

## Install 

python3, pip3 을 설치한다.

`sudo install python3 python3-pip`

pip 는 version 3 이다.

`pip install -r requirements.txt`

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