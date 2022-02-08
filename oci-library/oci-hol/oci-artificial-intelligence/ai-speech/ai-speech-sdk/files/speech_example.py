import oci
from oci.config import from_file

ai_client = oci.ai_speech.AIServiceSpeechClient(oci.config.from_file())

# Give your job related details in these fields
sample_display_name = "test_job"
sample_compartment_id = "ocid1.tenancy.oc1..aaaaaaaavhztk6bkuogd5w3nufs5dzts6dfob4nqxedvgbsi7qadonat76fa"
sample_description = "This is newly created Job"
sample_mode_details = oci.ai_speech.models.TranscriptionModelDetails(domain="GENERIC", language_code="en-US")
sample_object_location = oci.ai_speech.models.ObjectLocation(namespace_name="axsjzgvicq5h", bucket_name="speech_test",
object_names=["adaml-test-3chunk.wav"])
 
sample_input_location = oci.ai_speech.models.ObjectListInlineInputLocation(
location_type="OBJECT_LIST_INLINE_INPUT_LOCATION", object_locations=[sample_object_location])
 
sample_output_location = oci.ai_speech.models.OutputLocation(namespace_name="axsjzgvicq5h", bucket_name="speech_test",
prefix="Python_SDK_DEMO")
# For now only above job details are supported

# Create Transcription Job with details provided
transcription_job_details = oci.ai_speech.models.CreateTranscriptionJobDetails(display_name=sample_display_name,
                                                                               compartment_id=sample_compartment_id,
                                                                               description=sample_description,
                                                                               model_details=sample_mode_details,
                                                                               input_location=sample_input_location,
                                                                               output_location=sample_output_location)
 
transcription_job = None
try:
    transcription_job = ai_client.create_transcription_job(create_transcription_job_details=transcription_job_details)
except Exception as e:
    print(e)
else:
    print(transcription_job.data)

    
    
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
    transcription_jobs = ai_client.list_transcription_jobs(compartment_id=sample_compartment_id)
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
