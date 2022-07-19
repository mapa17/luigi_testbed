import luigi

from Tasks import HelloLuigiA, HelloLuigiB

class RunPipeline(luigi.Task):

    def run(self):
        print("Running Pipeline ...")

        print("Starting HelloLuigiA!")
        resultA = yield HelloLuigiA() 
        print(resultA)

        print("Starting HelloLuigiB!")
        resultB = yield HelloLuigiB() 

        print("Finishing Pipeline ...")


    def output(self):
        return luigi.LocalTarget('PipelineRun.txt')