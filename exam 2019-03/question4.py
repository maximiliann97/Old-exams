from enum import IntEnum
from collections import deque
import datetime
import abc


class LogLevel(IntEnum):
    debug = 0
    info = 1
    warning = 2
    error = 3


class LogSink(metaclass=abc.ABCMeta):
    def __init__(self, minimum_log_level):
        self.minimum_log_level = minimum_log_level

    @abc.abstractmethod
    def _write(self, entry: str):
        pass

    @staticmethod
    def datestamp():
        return '[' + datetime.datetime.now().isoformat() + ']'

    def push(self, importance: LogLevel, msg: str):
        if importance.value >= self.minimum_log_level:
            self._write(self.datestamp() + '-' + msg)


class PrintSink(LogSink):
    def _write(self, entry: str):
        print(entry)


class FileSink(LogSink):
    def __init__(self, minimum_log_level, filename):
        super().__init__(minimum_log_level)
        self.minimum_log_level = minimum_log_level
        self.output = open(filename, 'w')

    def _write(self, entry: str):
        self.output.write(str(entry) + '\n')


class MemorySink(LogSink):
    def __init__(self, minimum_log_level, maxlen):
        super().__init__(minimum_log_level)
        self.entries = deque(maxlen=maxlen)

    def __iter__(self):
        return iter(self.entries)

    def _write(self, entry: str):
        self.entries.append(entry)


class MultiSink(LogSink):
    def __init__(self, sinks):
        self.sinks = sinks

    def push(self, importance: LogLevel, msg: str):
        ds = self.datestamp()
        for sink in self.sinks:
            if sink.minimum_log_level <= importance:
                sink._write(ds + ' - ' + msg)

    def _write(self, entry: str):
        pass



ps = PrintSink(LogLevel.info)
fs = FileSink(LogLevel.warning, 'logfile.txt')
multi = MultiSink([ps, fs])
multi.push(LogLevel.info, 'Multi-test: Stuff happened.')
multi.push(LogLevel.error, 'Multi-test: An error occurred!')
ms = MemorySink(LogLevel.warning, 5)
for test_message in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    ms.push(LogLevel.warning, test_message)
for event in ms: # Should display C trough G
    print('MemorySink:', event)