import gspread
import pandas as pd


def define_env(env):
    "Mkdocs Macos Plugin Hook Function"

    @env.macro
    def get_google_sheet(url, api_key_file = None):
        gc = gspread.service_account() if not api_key_file else gspread.service_account(filename=api_key_file)
        sheet = gc.open_by_url(url).sheet1
        data = sheet.get_all_values()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)
        markdown_table = df.to_markdown(index=False)
        return markdown_table