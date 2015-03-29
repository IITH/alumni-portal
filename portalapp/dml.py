from portalapp.models import Department, Degree
#Create all degrees
Degree.objects.create(code='m', name='Master of Technology', short_name='M. Tech.')
Degree.objects.create(code='b', name='Bachelor of Technology',short_name='B. Tech.')
Degree.objects.create(code='p', name='Doctor of Philosophy', short_name='Ph.D.')
Degree.objects.create(code='mdes', name='Master of Design', short_name='M. Des.')

#Create engineering departments
Department.objects.create(code='cs',name='Department of Computer Science and Engineering')
Department.objects.create(code='ee',name='Department of Electrical Engineering')
Department.objects.create(code='me',name='Department of Mechanical Engineering')
Department.objects.create(code='bm',name='Department of Biomedical Engineering')
Department.objects.create(code='ce',name='Department of Civil Engineering')
Department.objects.create(code='ch',name='Department of Chemical Engineering')
Department.objects.create(code='ms',name='Department of Materials Science and Metallurgical Engineering')
Department.objects.create(code='la',name='Department of Liberal Arts')
Department.objects.create(code='es',name='Department of Engineering Science')
Department.objects.create(code='md',name='Department of Design')

#Create Science departments
Department.objects.create(code='cy',name='Department of Chemistry')
Department.objects.create(code='ph',name='Department of Physics')
Department.objects.create(code='bo',name='Department of Biotechnology')

#Other Cases to be included
#Dual Degree(B. Tech. + M. tech.) CONBM01
# Mtech Converted to Phd BM12M14P000002 , CH12M14P000002
# Design department master student : md14mdes11001@iith.ac.in