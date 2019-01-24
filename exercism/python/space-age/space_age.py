class SpaceAge(object):

    def __init__(self, seconds):

        ratios = list((planet, ratio * 31557600) for planet, ratio in (
        ('earth', 1.0),
        ('mercury', 0.2408467),
        ('venus', 0.61519726),
        ('mars', 1.8808158),
        ('jupiter', 11.862615),
        ('saturn', 29.447498),
        ('uranus', 84.016846),
        ('neptune', 164.79132)
    ))

        self.seconds = seconds
        for planet, ratio in ratios:
            setattr(self, 'on_' + planet, self._planet_years(ratio))

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds / ratio, 2)
