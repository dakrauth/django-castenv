from setuptools import setup

setup(
    name='django-env',
    version='0.1.0',
    description='Simple Django specific wrapper for dotenv',
    url='http://github.com/dakrauth/django-env',
    author='David Krauth',
    author_email='dakrauth@gmail.com',
    license='MIT',
    zip_safe=False,
    py_modules=['django-env'],
    install_requires=[
        'python-dotenv[cli]==0.10.3',
        'dj-email-url==0.2.0',
        'dj-database-url==0.5.0',
    ]
)
