class WeatherErr(Exception):
    pass

class NameCityErr(WeatherErr):
    err_text = ('Incorrect City name. Please, try again')

    def __init__(self):
        super().__init__()
        self.msg = self.err_text

    def __str__(self):
        return self.msg

class CoordErr(WeatherErr):
    err_text1 = ("Unknown coords. Pls, try again")

    def __init__(self):
        self.msg = self.err_text1

    def __str__(self):
        return self.msg
