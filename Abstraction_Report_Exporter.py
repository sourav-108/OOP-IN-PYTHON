from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass


class CSVExporter(ReportExporter):
    def export(self, data):
        return ",".join(data)


class TextExporter(ReportExporter):
    def export(self, data):
        return "\n".join(data)


report = ["Name,Score", "Sourav,92", "Durjoy,88"]

print(CSVExporter().export(report))
print(TextExporter().export(report))