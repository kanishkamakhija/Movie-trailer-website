import webbrowser
class Movie():
    """
        class defines the basic structure of Movie objects.
    """

    def __init__(self,title,description, poster, link_trailer):
        self.title = title
        self.description = description
        self.poster= poster
        self.link_trailer = link_trailer

    def open_trailer(self):
        webbrowser.open(self.link_trailer)
