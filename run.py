from app.homepage import homepage_app
from app.user_dash import user_dashboard_app
from app.admin_dash import admin_dashboard_app
from flask import Flask, Blueprint


app = Flask(__name__)

app.secret_key = 'Fluentfusion123'

app.register_blueprint(homepage_app)
app.register_blueprint(user_dashboard_app)
app.register_blueprint(admin_dashboard_app)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
