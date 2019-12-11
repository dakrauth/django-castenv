import os
import dotenv
import dj_database_url
import dj_email_url

required = object()


class Config:

    def __init__(self):
        self._values = None
        self.castings = {
            bool: lambda v: v.lower() in {'1', 'yes', 'true', 'y'} if isinstance(v, str) else bool(v),
            list: lambda v: [i.strip() for i in v.split(',')]
        }

    @property
    def values(self):
        if self._values is None:
            path = dotenv.find_dotenv(usecwd=True)
            self._values = dotenv.dotenv_values(path, verbose=True)

        return self._values

    def __call__(self, key, default=required, cast=str):
        value = self.values.get(key, default)
        if value is required:
            keys = ', '.join(self.values.keys())
            raise EnvironmentError(f'{key} is required, {keys}')

        return None if value is None else self.castings.get(cast, cast)(value)

    def db(self, key='DATABASE_URL'):
        return dj_database_url.parse(self(key))

    def email(self, key='EMAIL_URL'):
        return dj_email_url.parse(self(key))


config = Config()
