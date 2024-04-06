from django.http import HttpResponse
from .algorithms.scheduling import main
from .algorithms.preprocessing import processor_main  
import os

def print_schedule(request):
 
        # Define the path to the Excel dataset
        dataset_path = 'psl.xlsx' 
        if os.path.exists(dataset_path):
            print("Calling preprocess .....")
            # Preprocess the Excel dataset
            preprocessed_df = processor_main(dataset_path)

            if not preprocessed_df.empty:
                # Pass the preprocessed DataFrame to the scheduling algorithm
                print("Calling schedules .....")
                json_result = main(preprocessed_df)

                # Print JSON result in console
                print(json_result)

                # Return a simple HTTP response
                return HttpResponse(f"Algorithm result printed in console: {str(json_result)}")
            else:
                return HttpResponse("Error occurred during preprocessing ")
        else:
            return HttpResponse("File not found")
     
