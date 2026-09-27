class Printer:
    def print_document(self):
        return "Document printed"


class Scanner:
    def scan_document(self):
        return "Document scanned"


class OfficeMachine(Printer, Scanner):
    pass


machine = OfficeMachine()
print(machine.print_document())
print(machine.scan_document())