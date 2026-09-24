# 5. Abstract class Patient with calculate_bill() and treatment()

from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def treatment(self):
        print(f"{self.name} is admitted for treatment")

    def calculate_bill(self):
        return 5000   # room charges + treatment


class OutPatient(Patient):
    def treatment(self):
        print(f"{self.name} received outpatient consultation")

    def calculate_bill(self):
        return 500


class EmergencyPatient(Patient):
    def treatment(self):
        print(f"{self.name} received emergency treatment")

    def calculate_bill(self):
        return 8000


patients = [InPatient("Ravi"), OutPatient("Priya"), EmergencyPatient("Amit")]
for p in patients:
    p.treatment()
    print("Bill:", p.calculate_bill())
