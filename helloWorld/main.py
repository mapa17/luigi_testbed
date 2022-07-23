import luigi
from PipelineTask import RunPipeline

def test_pipeline():
    tasks = [RunPipeline()]

    # Create the pipeline. This will execute the tasks
    luigi.build(tasks, local_scheduler=True)

test_pipeline()