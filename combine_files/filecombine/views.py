import os
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

def combine_files(request):
    if request.method == 'POST':
        combined_data = pd.DataFrame()
        
        for file in request.FILES.getlist('files'):
            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
            combined_data = combined_data.append(data)
        
        combined_filename = 'combined_file.xlsx'
        combined_path = os.path.join('media', combined_filename)
        combined_data.to_excel(combined_path, index=False)
        
        response = HttpResponse(open(combined_path, 'rb'), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(combined_filename)
        return response
    
    return render(request, 'filecombine/combine.html')
