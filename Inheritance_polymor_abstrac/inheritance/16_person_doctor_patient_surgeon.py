# 16. Multiple + hierarchical inheritance
# Person -> Doctor, Patient -> Surgeon, MedicalResearcher

class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def __init__(self, name, specialization):
        Person.__init__(self, name)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, disease):
        Person.__init__(self, name)
        self.disease = disease


class Surgeon(Doctor):
    def __init__(self, name, specialization, surgeries_done):
        Doctor.__init__(self, name, specialization)
        self.surgeries_done = surgeries_done

    def display(self):
        print(f"Surgeon: {self.name}, Specialization: {self.specialization}, Surgeries Done: {self.surgeries_done}")


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, specialization, research_area):
        Doctor.__init__(self, name, specialization)
        self.research_area = research_area

    def display(self):
        print(f"Researcher: {self.name}, Specialization: {self.specialization}, Research Area: {self.research_area}")


s1 = Surgeon("Dr. Mehta", "Cardiology", 250)
r1 = MedicalResearcher("Dr. Rao", "Oncology", "Cancer Treatment")
s1.display()
r1.display()
