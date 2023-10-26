# 🌐 Language Learning Platform (LLP)

Welcome to the Language Learning Platform (LLP) repository! LLP is a fantastic web application designed to make language learning a breeze. Whether you're a student looking to ace your language classes or a language enthusiast eager to explore new cultures, LLP is here to assist you on your linguistic journey. 📚🌍

## 🚀 Installation

****Database - MySql****
*for registration and login purpose*
CREATE DATABASE fluentfusion;

USE fluentfusion;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);


Getting started with LLP is a piece of cake! First, make sure you have Python 3.x installed on your system. Then, install the required dependencies by running this command:

```bash
pip install -r requirements.txt
```

## 💡 Usage

To launch the LLP Flask web app, execute the following command:

```bash
python app.py
```

That's it! You're ready to dive into the world of language learning. 🎉

## 📦 Dependencies

LLP relies on several essential dependencies to run smoothly. Here's a list of what you'll need:

- **blinker==1.6.2**
- **click==8.1.7**
- **colorama==0.4.6**
- **Flask==2.3.3**
- **Flask-SQLAlchemy==3.1.1**
- **Flask-WTF==1.1.1**
- **greenlet==2.0.2**
- **itsdangerous==2.1.2**
- **Jinja2==3.1.2**
- **MarkupSafe==2.1.3**
- **SQLAlchemy==2.0.21**
- **typing_extensions==4.8.0**
- **Werkzeug==2.3.7**
- **WTForms==3.0.1**

You can swiftly install these dependencies with pip:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

We're thrilled to welcome contributions from the community! If you encounter any issues or have brilliant ideas for improvement, please don't hesitate to open an issue or submit a pull request. Your input is invaluable to us. 🙌

Contributors:
- [Ankush Tiwari](https://github.com/tiwaribro)
- [Nikita Choudhari](https://github.com/ChoudhariNikita)
- [Gayatri Yaul](https://github.com/gayatriyaul)



## 📄 License

This project is proudly licensed under the MIT License. Feel free to use and modify it as needed to meet your specific requirements. 📜

Please note that this README is just a sample, and you can customize it further to fit your project's unique personality. Good luck with your Language Learning Platform! 🌟🗺️

For more detailed information on running a Flask web app, consult the official Flask documentation [here](https://flask.palletsprojects.com/en/2.0.x/). 📖👩‍💻
