REPORT_FOLDER = './report/'


class ReportFileWriter:

    @staticmethod
    def write(report: str, filename: str) -> None:
        with open(f'{filename}.txt', "w") as file:
            file.writelines(report)


class Writer:

    @staticmethod
    def write(
        report, filename: str = REPORT_FOLDER+'output', writer=ReportFileWriter
    ):
        writer.write(report, filename=filename)
