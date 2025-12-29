import webview

def main():
    window = webview.create_window(
        "Python → JS",
        url="index.html",
        width=1000,
        height=700
    )

    def after_start():
        # JS-Funktion aufrufen (und Rückgabewert bekommen)
        result = window.evaluate_js("window.setStatus('Hallo aus Python!')")
        print("Python bekam zurück:", result)

        # Du kannst auch direkt JS ausführen:
        window.evaluate_js("console.log('Console: Grüße aus Python')")

    webview.start(after_start, debug=True)

if __name__ == "__main__":
    main()
