from setuptools import setup

setup(
    name='django-castenv',
    version='0.2.0',
    description='Simple Django specific wrapper for dotenv, with casting',
    url='http://github.com/dakrauth/django-castenv',
    author='David Krauth',
    author_email='dakrauth@gmail.com',
    license='MIT',
    zip_safe=False,
    py_modules=['django-castenv'],
    install_requires=[
        'python-dotenv[cli]==0.15.0',
        'dj-email-url==1.0.2',
        'dj-database-url==0.5.0',
    ]
)
