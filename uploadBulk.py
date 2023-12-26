import requests

def upload_image(file_path):
    files = {'image': open(file_path, 'rb')}
    response = requests.post('http://localhost:5000/upload', files=files)

    if response.status_code == 200:
        print('Image uploaded successfully')
    else:
        print(f'Error: {response.content}')


image_file_path = 'ExampleProfile.jpg'
upload_image(image_file_path)