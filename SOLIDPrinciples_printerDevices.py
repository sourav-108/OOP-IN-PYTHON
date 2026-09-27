class BasicPrinter:
    def print_page(self, text):
        print(f"Printing: {text}")


class OfficePrinter:
    def print_page(self, text):
        print(f"Printing: {text}")

    def scan_page(self):
        print("Scanning page")

    def fax_page(self, number):
        print(f"Faxing to {number}")


BasicPrinter().print_page("Meeting agenda")
OfficePrinter().scan_page()