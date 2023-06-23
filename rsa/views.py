from django.shortcuts import render
from .rsa import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = {
            'N': request.POST.get('N'),
            'e': request.POST.get('e'),
            'd': request.POST.get('d'),
            'public_key': request.POST.get('public_key'),
            'private_key': request.POST.get('private_key'),
            'message': request.POST.get('message'),
            'encrypted_message': request.POST.get('encrypted_message'),
            'message_to_decrypt': request.POST.get('message_to_decrypt'),
            'decrypted_message': request.POST.get('decrypted_message'),
        }
        
        operation = request.POST.get('operation')
        if operation == 'generate-keys':
             p, q, N, e, d, fi_N = rsa_set(5)
             data['N'] = N
             data['e'] = e
             data['d'] = d
             data['public_key'] = e
             data['private_key'] = d
             data['message'] = ''
             data['encrypted_message'] = ''
             data['message_to_decrypt'] = ''
             data['decrypted_message'] = ''
    
        
        if operation == 'encrypt':
            data['encrypted_message'] = "".join(str(num) + ',' for num in rsa_enc(data['message'], int(data['N']), int(data['public_key'])))[:-1]
            data['message_to_decrypt'] = data['encrypted_message']
        if operation == 'decrypt':
            encrypted_arr = [int(num) for num in data['message_to_decrypt'].split(',')] 
            print(encrypted_arr)
            data['decrypted_message'] = rsa_dec(int(data['private_key']), int(data['N']), encrypted_arr)    
                           
        data['disabled_encrypt_button'] = data['public_key'] == ''
        
        return render(request, 'index.html',data)
            
    else:
        return render(request, 'index.html', {})