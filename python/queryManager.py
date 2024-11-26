from pyhive import hive

class queryManager:

    @staticmethod
    def createDatabase(connection : hive.Connection, *arguments):
        print(arguments)

