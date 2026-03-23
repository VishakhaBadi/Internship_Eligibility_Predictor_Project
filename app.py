from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'secret'

users = {}

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']
    users[username] = password
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        u = request.form['username']
        p = request.form['password']
        if u in users and users[u]==p:
            session['user']=u
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        cgpa = float(request.form['cgpa'])
        tech = int(request.form['tech_skills'])
        soft = int(request.form['soft_skills'])
        projects = int(request.form['projects'])
        certs = int(request.form['certifications'])
        intern = int(request.form['internship_exp'])
        workshops = int(request.form['workshops'])
        hackathons = int(request.form['hackathons'])

        # ✅ Suggestions logic (INSIDE POST)
        suggestions = []

        if tech < 5:
            suggestions.append("Improve your technical skills (minimum 5 required).")

        if cgpa < 7:
            suggestions.append("Increase your CGPA (aim for 7+).")

        if projects < 2:
            suggestions.append("Work on more projects (at least 3 recommended).")

        # ✅ Final result
        if tech >= 5 and cgpa >= 7:
            result = "✅ Eligible for Internship"
        else:
            result = "❌ Not Eligible"

        return render_template('predict.html',
                               prediction_text=result,
                               suggestions=suggestions)

    # GET request
    return render_template('predict.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/model')
def model():
    return render_template('model.html')   

@app.route('/faqn')
def faqn():
    return render_template('faqn.html')    

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)