# Table from google sheet

[Mkdocs-Macros-Plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) 을 이용해서 Google Spread Sheet 를 [Mkdocs Data Table](https://squidfunk.github.io/mkdocs-material/reference/data-tables/) 을 생성한다.

## 방법

`get-google-sheet(googleSheetFileUrl, apiJsonFilePath)` 매크로 함수를 호출해서 구글 스프레드 시트의 데이터를 마크다운 데이터 테이블로 만들수 있다.


# Table from google sheet

사용을 위해서 Google Service API 를 활성화하고 인증키 json 파일을 만들어 다운로드 해야 한다.
또한 해당 Json 에서 client-email 을 해당 문서에 Share 에 추가해야 한다.

### Google Service API Key

구글 인증을 받기 위해서는 아래 [gspread 모듈의 인증 설명서](https://github.com/burnash/gspread/blob/master/docs/oauth2.rst) 대로 수행해야 한다.

아래는 원본이 존재하지 않을 경우를 위해 그대로 인용한다. 원본이 존재하는 경우에 원본을 참조한다.

Here's how to get one:

1. :ref:`enable-api-access` if you haven't done it yet.

2. Go to "APIs & Services > Credentials" and choose "Create credentials > Service account key".

3. Fill out the form

4. Click "Create" and "Done".

5. Press "Manage service accounts" above Service Accounts.

6. Press on **⋮** near recently created service account and select "Manage keys" and then click on "ADD KEY > Create new key".

7. Select JSON key type and press "Create".

You will automatically download a JSON file with credentials. It may look like this:

::

    {
        "type": "service_account",
        "project_id": "api-project-XXX",
        "private_key_id": "2cd … ba4",
        "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
        "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
        "client_id": "473 … hd.apps.googleusercontent.com",
        ...
    }

Remember the path to the downloaded credentials file. Also, in the next step you'll need the value of *client_email* from this file.

6. Very important! Go to your spreadsheet and share it with a *client_email* from the step above. Just like you do with any other Google account. If you don't do this, you'll get a ``gspread.exceptions.SpreadsheetNotFound`` exception when trying to access this spreadsheet from your application or a script.

7. Move the downloaded file to `~/.config/gspread/service_account.json`. Windows users should put this file to ``%APPDATA%\gspread\service_account.json``.

8. Create a new Python file with this code:

::

    import gspread

    gc = gspread.service_account()

    sh = gc.open("Example spreadsheet")

    print(sh.sheet1.get('A1'))

Ta-da!