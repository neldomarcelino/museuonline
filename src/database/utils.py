from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_matcher = re.compile('^[\w]+@([a-z]+\.)+[a-z]+$')

        return True if email_matcher.match(email) else False

    @staticmethod
    def check_hashed_password(password, hashed_password):

        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def hash_password(password):
        """

        :param password:
        :return:
        """
        return pbkdf2_sha512.encrypt(password)
