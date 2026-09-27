class Invoice:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(price for name, price in self.items)


class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice total: ${invoice.total():.2f}")


invoice = Invoice([("Keyboard", 45), ("Mouse", 20)])
InvoicePrinter().print_invoice(invoice)