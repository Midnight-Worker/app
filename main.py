import webview
import sqlite3

DB_PATH = "mydatabase.sqlite"

class Api:
    def get_users(self):
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()

            cur.execute("""
                SELECT id, name, email
                FROM users
                ORDER BY id DESC
                LIMIT 100
            """)
            rows = cur.fetchall()

        # Row -> dict, damit JS ein Array von Objekten bekommt
        return [dict(r) for r in rows]

def main():
	api = Api()
	window = webview.create_window(
		"Python -> Js",
		url="ui/index.html",
		x=-2500,
		y=150,
		width=1000,
		height=700,
        js_api=api
	)

	#def after_start():
	#	window.evaluate_js("console.log('Console: Grüße aus Python')")

	webview.start(debug=True)

if __name__=="__main__":
	main()

