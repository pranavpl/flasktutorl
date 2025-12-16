from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Home route
@app.route('/')
def home():
    return "httttgg"
# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Application context
if __name__ == '__main__':
    
    
    # Run the development server
    app.run(debug=True, host='127.0.0.1', port=5000)