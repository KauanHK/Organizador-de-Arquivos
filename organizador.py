import os
import shutil

class Organizador:

    def __init__(self,dir):
        self.dir = dir
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    # Definir a extensão de um arquivo
    def get_extension(self,file):
        extensao = file.split('.')[-1]
        return extensao

    def dir_in(self):
        arquivos = os.listdir(self.dir)
        for arquivo in arquivos:
            if os.path.isdir(os.path.join(self.dir,arquivo)):
                return True
        return False

    def mover_pasta(self,src,dst,rm_mescled):

        arquivos_dst = os.listdir(dst)

        # Se não existir uma pasta com o mesmo nome, movê-la para o diretório desejado
        mesclar = False
        for arquivo in arquivos_dst:
            if os.path.join(src,arquivo).split('\\')[-1] == src.split('\\')[-1]:
                mesclar = True
                break
            
        if not mesclar:
            shutil.move(src,dst)
        else:
            # Se já existir uma pasta com o mesmo nome, mesclar pastas
            for arquivo in os.listdir(src):
                shutil.move(os.path.join(src,arquivo),dst)

            if rm_mescled:
                os.rmdir(src)

    def copy_archives(self,src):
        print('Copiando arquivos... Isso pode levar algum tempo.')

        lista_arquivos = os.listdir(src)

        num_arquivos = len(lista_arquivos)

        num_arquivos_denied = 0
        arquivos_denied = []
        for i,arquivo in enumerate(lista_arquivos):
            print(f'{i}/{num_arquivos}',end='\r')
            path_arquivo = src + '\\' + arquivo
            if os.path.isdir(path_arquivo):
                path_nova_pasta = self.dir + '\\' + arquivo
                os.mkdir(path_nova_pasta)
                try:
                    # shutil.copytree(path_arquivo,path_nova_pasta,dirs_exist_ok=True)
                    for arq in os.listdir(path_arquivo):
                        print(f'Arquivo: {arq}')
                        shutil.move(path_arquivo + f'\\{arq}',path_nova_pasta)
                except:
                    num_arquivos_denied += 1
                    arquivos_denied.append(arquivo)
            else:
                try:
                    shutil.copy(path_arquivo,self.dir)
                except:
                    num_arquivos_denied += 1
                    arquivos_denied.append(arquivo)

        if not num_arquivos_denied:
            print(f'{num_arquivos}/{num_arquivos}',end='\r')
            print("Todos os arquivos foram copiados para a pasta com sucesso.")
        else:
            print("A cópia não foi bem-sucedida para todos os arquivos:")
            print("Número de arquivos com permissão negada: ", num_arquivos_denied)
            print("Os arquivos foram: ")
            for arquivo in arquivos_denied:
                print(arquivo, end='')
                if arquivo != arquivos_denied[-1]:
                    print(', ',end='')
                else:
                    print('.')

    # Extrair todas as pastas até sobrar somente arquivos
    def extract_all_dir(self):
        print('Extraindo pastas...')

        # Enquanto existir pastas no diretório, extrai-las todas
        while self.dir_in():
            # Pastas dentro do diretório
            pastas_diretorio = [pasta for pasta in os.listdir(self.dir) if os.path.isdir(os.path.join(self.dir,pasta))]

            # Mover cada arquivo e pasta da pasta para o diretório
            for pasta in pastas_diretorio:
                # Caminho da pasta do diretório
                path_pasta = os.path.join(self.dir,pasta)

                # Para cada arquivo da pasta do diretório
                for arquivo in os.listdir(path_pasta):

                    # Mover arquivo para o diretório, verificando se já há algum arquivo com o mesmo nome
                    novo_nome = arquivo
                    i = 1
                    # Enquanto existir um arquivo com o mesmo nome
                    while os.path.exists(self.dir + '\\' + novo_nome):
                        # Definir um novo nome para o arquivo
                        if os.path.isfile(self.dir + '\\' + novo_nome):
                            novo_nome = arquivo.split('.')
                            novo_nome[0] += f'({i})'
                            novo_nome = f'{novo_nome[0]}.{novo_nome[1]}'
                        else:
                            novo_nome += f'({i})'
                        i += 1

                    # Caminho do arquivo
                    path_arquivo = os.path.join(path_pasta,arquivo)

                    # Renomear o arquivo
                    if arquivo != novo_nome:
                        # Caminho do arquivo renomeado
                        path_novo_nome = path_pasta + '\\' + novo_nome

                        # Renomear arquivo
                        os.rename(path_arquivo,path_novo_nome)

                        path_arquivo = os.path.join(path_pasta,path_novo_nome)

                    shutil.move(path_arquivo, self.dir)

                    print('                                                                                                                   ',end='\r')
                    print(f'Arquivo: {arquivo}',end='\r')
                # shutil.copytree(path_pasta, self.dir, dirs_exist_ok=True)

                # if not os.path.exists(dst + "\\" + arquivo):
                #     self.mover_pasta(src,dst,True)

                # Remover a pasta quando estiver vazia
                try:
                    os.rmdir(os.path.join(self.dir,pasta))
                except:
                    print(f'A pasta {pasta} não pôde ser removida')

        print('\nPastas extraídas com sucesso')

    def organize_dir(self):
        print('Organizando pastas...')

        conteudo_dir = os.listdir(self.dir)

        for arquivo in conteudo_dir:
            path_arquivo = f'{self.dir}\\{arquivo}'

            ext = self.get_extension(arquivo)
            ext_name = ext.upper()

            path_pasta = f'{self.dir}\\{ext_name}'
            if not os.path.exists(path_pasta):
                os.mkdir(path_pasta)

            if not os.path.exists(path_pasta + '\\' + arquivo):
                shutil.move(path_arquivo,path_pasta)
            
        print("Os arquivos foram organizados com sucesso.")


# # Definindo o caminho para a pasta Downloads
# disco,users,usuario = os.getcwd().split('\\')[:3]
# diretorio_downloads = f'{disco}\\{users}\\{usuario}\\Downloads'

# # Caminho da pasta destino 'Downloads Organizados'
# downloads_organizados = os.getcwd() + '\\Downloads Organizados'

# # Copiar todos os arquivos da pasta downloads para a pasta 'Downloads Organizados'
# copy_archives(diretorio_downloads,downloads_organizados)

# # Extrair todo o conteúdo de todas as pastas do diretório
# extract_all_dir(downloads_organizados)

# # Organizar a pasta
# organize_dir(downloads_organizados)



path_pasta = os.getcwd() + '\\Codes Organizados8'
pasta_copiada = 'C:\\Users\\Kauan Kaestner\\Documents\\Kauan\\codigos'

organizador = Organizador(path_pasta)

organizador.copy_archives(pasta_copiada)
organizador.extract_all_dir()
organizador.organize_dir()