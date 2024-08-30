import os

def get_dirs(path_dir):
    result = {'pastas': [], 'arquivos': []}
    for dir in os.listdir(path_dir):
        full_path = os.path.join(path_dir, dir)
        if os.path.isdir(full_path):
            result['pastas'].append(dir)
            subdirs = get_dirs(full_path)
            result['pastas'].extend(subdirs['pastas'])
            result['arquivos'].extend(subdirs['arquivos'])
        else:
            result['arquivos'].append(dir)
    return result

print(os.getcwd())
dirs = get_dirs('/home/kauan/Documentos/Codigos/python')
# for item in dirs:
#     print(f'{item}: ', *dirs[item], sep=', ')
print(len(dirs['pastas']))
print(len(dirs['arquivos']))