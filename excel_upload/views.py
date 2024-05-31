import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomerRecord
from django.db.models import Count

def homepage(request):
    context = {
        'app_description': 'Welcome to our application! This application allows you to upload Excel files and process the data efficiently.',
        'apis': [
            {'name': 'Upload Excel', 'url': '/upload/'},
            {'name': 'Get Results', 'url': '/generate_summary_report'},
            # Add more APIs as needed
        ]
    }
    return render(request, 'homepage.html', context)

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        excel_file = request.FILES['file']
        
        # Check if the file is in Excel format
        if not excel_file.name.endswith('.xls') and not excel_file.name.endswith('.xlsx'):
            return HttpResponse('File is not in Excel format.')

        try:
            # Read Excel file
            df = pd.read_excel(excel_file)
            
            # Iterate over rows and save records
            for index, row in df.iterrows():
                record = CustomerRecord(
                    date=row['Date'],
                    accno=row['ACCNO'],
                    cust_state=row['Cust State'],
                    cust_pin=row['Cust Pin'],
                    dpd=int(row['DPD'])
                )
                record.save()
            
            return HttpResponse('File uploaded successfully!')
        except Exception as e:
            return HttpResponse(f'Error: {e}')

    return render(request, 'upload.html')

def generate_summary_report(request):
    # Query the database to get the summary data
    summary_data = CustomerRecord.objects.values('cust_state', 'dpd').annotate(count=Count('id'))

    # Pass the summary data to the template for rendering
    return render(request, 'summary.html', {'summary_data': summary_data})
