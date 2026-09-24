# 13. Multiple inheritance - Printer + Scanner -> MultifunctionDevice

class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def copy_document(self):
        self.scan_document()
        self.print_document()
        print("Document copied")


m1 = MultifunctionDevice()
m1.print_document()
m1.scan_document()
m1.copy_document()
