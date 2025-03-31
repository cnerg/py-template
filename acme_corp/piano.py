class Piano:
    """A grand piano proudly built by ACME corporation.

    Weighing half a ton be careful when hoisting this precariously over
    sidewalks.

    Warnings
    --------
    Always use proper rigging techniques when hoisting this above
    above any paths that may be occupied any Road Runners.
    """

    def __init__(self):
        self._weight = 1_000
        # start on ground level
        self._height = 0

    def lift(self):
        self._height = 3  # [m]

    def drop(self):
        pass

    @property
    def weight(self):
        """The current weight of the piano.

        Returns
        -------
        float
            the current weight.
        """
        return self._weight

    @property
    def height(self):
        """The current height of the piano.

        Returns
        -------
        float
            the current height.
        """
        return self._height
