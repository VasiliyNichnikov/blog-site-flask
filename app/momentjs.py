from jinja2 import Markup


class MomentJS(object):
    def __init__(self, timestamp) -> None:
        self.__timestamp = timestamp

    def render(self, format) -> Markup:
        return Markup("<script>\ndocument.write(moment(\"{}\").{});\n</script>".
                      format(self.__timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format))

    def format(self, fmt) -> Markup:
        return self.render(f"format(\"{fmt}\")")

    def calendar(self) -> Markup:
        return self.render("calendar()")

    def fromNow(self) -> Markup:
        return self.render("fromNow()")