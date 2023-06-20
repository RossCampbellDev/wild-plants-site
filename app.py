from flasky import create_app

if __name__ == "__main__":
	app = create_app()
	app.run(debug=True, host="0.0.0.0", port=31337)

def get_app():
	return app