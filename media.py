import webbrowser


class Movie():
    """
        class defines the basic structure of Movie objects.
    """

    def __init__(self, title, description, poster, link_trailer):
        """
            This is the constructor function which
            takes the following arguments
            1. Title
            2. Description
            3. Poster image link
            4. Movie trailer link
            This function then initialises the instance variable
        """
        self.title = title
        self.description = description
        self.poster = poster
        self.link_trailer = link_trailer
