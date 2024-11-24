import os

def organize_files(directory):

    if not os.path.exists(directory):
        return "Directory does not exist!"

    is_windows = os.name == 'nt'

    file_types = {
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Misc': []
    }

    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(file_name)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination = os.path.join(directory, folder, file_name)
                
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True
                break
        
        if not moved:
            misc_destination = os.path.join(directory, 'Misc', file_name)
            if not os.path.exists(misc_destination):
                if is_windows:
                    os.system(f'move "{file_path}" "{misc_destination}"')
                else:
                    os.system(f'mv "{file_path}" "{misc_destination}"')

    return "Files have been organized!"
