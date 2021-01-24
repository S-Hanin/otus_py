# -*- coding: utf-8 -*-

import json
import csv
import sys


class BaseWriter:
    def __init__(self, output_filename=None):
        self.output = sys.stdout if not output_filename else output_filename

    def write(self, data):
        raise NotImplementedError


class ConsoleWriter(BaseWriter):
    def write(self, data):
        for k, v in data:
            print("{0:20s}: {1:>5d}".format(k, v))


class CsvWriter(BaseWriter):
    def write(self, data):
        with open(self.output, 'w', newline='') as fh:
            writer = csv.writer(fh)
            for row in data:
                writer.writerow(row)


class JsonWriter(BaseWriter):
    def write(self, data):
        with open(self.output, 'w') as fh:
            for row in data:
                fh.write(json.dumps(row))
                fh.write('\n')


def make_report(report_format, output_filename, report_data_list):
    report_format_map = {"console": ConsoleWriter,
                         "json": JsonWriter,
                         "csv": CsvWriter}
    writer = report_format_map.get(report_format, ConsoleWriter)(output_filename)
    writer.write(report_data_list)
