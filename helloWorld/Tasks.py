import luigi

class HelloLuigiA(luigi.Task):

    def output(self):
        return luigi.LocalTarget('hello-luigi-A.txt')

    def run(self):
        #from pudb import set_trace as st; st()
        print(f"In HelloLuigiA.run()")
        with self.output().open("w") as outfile:
            outfile.write("Hello Luigi-A!")
        
class HelloLuigiB(luigi.Task):

    def output(self):
        return luigi.LocalTarget('hello-luigi-B.txt')

    def run(self):
        print(f"In HelloLuigiB.run()")
        with self.output().open("w") as outfile:
            outfile.write("Hello Luigi-B!")

