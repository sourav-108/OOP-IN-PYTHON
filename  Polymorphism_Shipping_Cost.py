class PDFReport:
    def export(self, data):
        return f"Exported {data} as PDF"


class CSVReport:
    def export(self, data):
        return f"Exported {data} as CSV"


def save_report(report, data):
    print(report.export(data))


save_report(PDFReport(), "Sales report")
save_report(CSVReport(), "Sales report")