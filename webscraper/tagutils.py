import re


class TagUtils(object):

    """
        Utility class to extract data from tags
    """

    @staticmethod
    def contents(tag):
        """
        :param tag: a tag element
        :return: the string
        Works for tags with contents such a <a> or <p> or <b>
        """
        return tag.contents[0].strip()

    @staticmethod
    def float_contents(tag):
        """
            :param tag: a tag element
            :return: a float
            Works for tags with contents such a <a> or <p> or <b>
            attemtps to extract an int or a float and returns it
        """
        contents = TagUtils.contents(tag)
        # find a float, if the float is followed by a
        # full stop, it's a problem because it matches.
        value = re.findall('[\d.]+', contents)
        value = value[0]
        if value[-1] == '.':
            value = value[:-1]
        return float(value)