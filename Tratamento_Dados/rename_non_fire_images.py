import re
import os
import shutil

#O Dataset for Forest Fire Detection, o qual foi escolhido
# como padrão de dados, classifica como:
# nofire_0000
# fire_0000


#Adicionar o caminho correspondente ao diretório a ser mudado
main_folder = r'C:\Users\laura\Desktop\fire_dataset\non_fire_images'

def rename_file(file):
  file_name, file_extension = os.path.splitext(file)
  file_name_numbers = re.findall(r'\d+', file_name)

  if not file_name_numbers:
    return file

  file_name_numbers = file_name_numbers[0].zfill(4)

  return f'nofire_{file_name_numbers}{file_extension}'


def main_loop():
  for root, dirs, files in os.walk(main_folder):
    for file in files:
      new_file_name = rename_file(file)
      old_file_full_path = os.path.join(root, file)
      new_file_full_path = os.path.join(root, new_file_name)

      shutil.move(old_file_full_path, new_file_full_path)


if __name__ == '__main__':
  main_loop()