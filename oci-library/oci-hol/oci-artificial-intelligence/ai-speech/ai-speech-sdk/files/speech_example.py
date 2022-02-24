import oci
from oci.config import from_file

ai_client = oci.ai_speech.AIServiceSpeechClient(oci.config.from_file())

# Give your job related details in these fields
SAMPLE_DISPLAY_NAME = "test_job"
SAMPLE_COMPARTMENT_ID = "ocid1.tenancy.oc1..<uniqueID>"
SAMPLE_DESCRIPTION = "This is newly created Job"
SAMPLE_NAMESPACE = "<namespace_placeholder>"
SAMPLE_BUCKET = "<bucket_placeholder>"
LANGUAGE_CODE = "<language_code_placeholder>"
SAMPLE_MODE_DETAILS = oci.ai_speech.models.TranscriptionModelDetails(domain="GENERIC", language_code=LANGUAGE_CODE)
SAMPLE_OBJECT_LOCATION = oci.ai_speech.models.ObjectLocation(namespace_name=SAMPLE_NAMESPACE, bucket_name=SAMPLE_BUCKET,
OBJECT_NAMES=["<filename1>, <filename2>"])
SAMPLE_INPUT_LOCATION = oci.ai_speech.models.ObjectListInlineInputLocation(
location_type="OBJECT_LIST_INLINE_INPUT_LOCATION", object_locations=[SAMPLE_OBJECT_LOCATION])
SAMPLE_OUTPUT_LOCATION = oci.ai_speech.models.OutputLocation(namespace_name=SAMPLE_NAMESPACE, bucket_name=SAMPLE_BUCKET,
PREFIX="Python_SDK_DEMO")
# For now only above job details are supported


# Create Transcription Job with details provided
transcription_job_details = oci.ai_speech.models.CreateTranscriptionJobDetails(display_name=SAMPLE_DISPLAY_NAME,
                                                                               compartment_id=SAMPLE_COMPARTMENT_ID,
                                                                               description=SAMPLE_DESCRIPTION,
                                                                               model_details=SAMPLE_MODE_DETAILS,
                                                                               input_location=SAMPLE_INPUT_LOCATION,
                                                                               output_location=SAMPLE_OUTPUT_LOCATION)
 
transcription_job = None
try:
    transcription_job = ai_client.create_transcription_job(create_transcription_job_details=transcription_job_details)
except Exception as e:
    print(e)
else:
    print(transcription_job.data)


# Cancel transcription job and all tasks under it
try:
    ai_client.cancel_transcription_job(transcription_job.data.id)
except Exception as e:
    print(e)



# Gets Transcription Job with given Transcription job id
try:
    if transcription_job.data:
        transcription_job = ai_client.get_transcription_job(transcription_job.data.id)
except Exception as e:
    print(e)
else:
    print(transcription_job.data)


    
# Gets All Transcription Jobs from a particular compartment
try:
    transcription_jobs = ai_client.list_transcription_jobs(compartment_id=SAMPLE_COMPARTMENT_ID)
except Exception as e:
    print(e)
else:
    print(transcription_jobs.data)

    
    
#Gets Transcription tasks under given transcription Job Id
transcription_tasks = None
try:
    transcription_tasks = ai_client.list_transcription_tasks(transcription_job.data.id)
except Exception as e:
    print(e)
else:
    print(transcription_tasks.data)

    
    
# Gets a Transcription Task with given Transcription task id under Transcription Job id
transcription_task = None
try:
    if transcription_tasks.data:
        transcription_task = ai_client.get_transcription_task(transcription_job.data.id, transcription_tasks.data[0].id)
except Exception as e:
    print(e)
else:
    print(transcription_task.data)
