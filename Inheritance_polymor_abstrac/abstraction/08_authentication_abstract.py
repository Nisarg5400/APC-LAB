# 8. Abstract class Authentication with authenticate()

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuth(Authentication):
    def __init__(self, password, entered_password):
        self.password = password
        self.entered_password = entered_password

    def authenticate(self):
        return self.password == self.entered_password


class OTPAuth(Authentication):
    def __init__(self, otp, entered_otp):
        self.otp = otp
        self.entered_otp = entered_otp

    def authenticate(self):
        return self.otp == self.entered_otp


class BiometricAuth(Authentication):
    def __init__(self, match_percentage):
        self.match_percentage = match_percentage

    def authenticate(self):
        return self.match_percentage >= 90


methods = [PasswordAuth("abc123", "abc123"), OTPAuth("4455", "4455"), BiometricAuth(95)]
for m in methods:
    print(f"{m.__class__.__name__} Authenticated: {m.authenticate()}")
