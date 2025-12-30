import webview

class Api:
	def printit(self):
		print("print it")

def main():
	api = Api()
	window = webview.create_window(
		"Python -> Js",
		url="ui/index.html",
		width=1000,
		height=700,
		js_api=api
	)

	def after_start():
		window.evaluate_js("console.log('Console: Grüße aus Python')")

	webview.start(after_start, debug=True)

if __name__=="__main__":
	main()
