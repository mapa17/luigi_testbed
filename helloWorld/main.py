import luigi
from PipelineTask import RunPipeline

def test_pipeline():
    tasks = [RunPipeline()]

    # Create the pipeline. This will execute the tasks
    luigi.build(tasks, scheduler_host='localhost',
                       scheduler_port='8888',
                       local_scheduler=True)

test_pipeline()