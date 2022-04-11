import os


"""
Sluggifify the filename. The process is 2 folds
1. Lower case the file name
2. Replace the space with '-'
"""
def slug(filename):
    new_name = []
    for word in filename.split(' '):
        new_name.append(word.strip().lower())

    return '-'.join(new_name)


def change_extention_to_markdown(filename):
    if 'txt' in filename:
        return filename.replace('txt','md')

    return filename

def sluggify(files):
    for item in files:
        if os.path.isfile(item):
            has_space = ' ' in item
            if has_space:
                sluggified_name = slug(item)
                new_name = change_extention_to_markdown(sluggified_name)
                print( item,' => ' , new_name)


            
if  __name__ == '__main__':
    print('Current working directory => ', os.getcwd())

    files_in_cwd = os.listdir('.')
    
    print('Total files => ', len(files_in_cwd))
    print('=====================================')
    sluggify(files_in_cwd)
    
                
