from flask import Flask, render_template
import program

app = Flask(__name__)      
 
@app.route('/')
def home():
	line, title, URI = program.generator()
	return render_template('index.html', line=line, title=title, URI=URI)

@app.route('/about')
def about():
	return render_template('about.html')
 
if __name__ == '__main__':
  app.run(debug=True)