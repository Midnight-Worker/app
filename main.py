import webview

class Api:
	def printit(self):
		print("print it!!")

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

	def after_start():
		window.evaluate_js("console.log('Console: Grüße aus Python')")
		#window.move(200, 150)

	webview.start(after_start, debug=False)

if __name__=="__main__":
	main()

