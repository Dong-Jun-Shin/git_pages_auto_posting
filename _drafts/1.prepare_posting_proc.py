import os, shutil
import re
from datetime import datetime
from tkinter import messagebox

# ex. C:\\Users\\user\\Desktop\\example.github.io
REPO_PATH = '{your_repo_path}'
FILE_PATH = os.getcwd().replace('\\', '/') + '/ready_post'
TO_POST_PATH = ''
TO_IMG_PATH = ''
CATE_EXP = re.compile(r'^categories: ')
DATE_EXP = re.compile(r'^date: ')
IMG_EXP = re.compile(r'^\[link[0-9]\d*\]:')
DATE_NAME = ''


def delete_group_folder(to_path, to_img_path):
    # 예외 발생 시, 만들어진 폴더는 삭제
    if to_path:
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
    if to_img_path:
        if os.path.exists(to_img_path):
            shutil.rmtree(to_img_path)

def get_sub_folder_list(path):
    return [sub_folder[1] for sub_folder in os.walk(path)]

def get_parent_path(dir):
    return os.path.dirname(os.path.normpath(dir)).replace('\\', '/')

def jekyll_publish_proc():
    try:
        os.system('cd ' + REPO_PATH + ' && bundle exec jekyll build')
    except:
        messagebox.showinfo("Warning", "오류가 발생하였습니다.")

def prepare_posting_proc():
    global TO_POST_PATH, TO_IMG_PATH, DATE_NAME
    folder_names = get_sub_folder_list(FILE_PATH)
    for file_title in folder_names[0]:
        edited_lines = []
        define_bool = False
        layer_path, cat_id, date_year, date_month = '', '', '', ''

        parent_path = get_parent_path(get_parent_path(FILE_PATH))
        from_path = FILE_PATH + '/' + file_title
        file_name = from_path + '/' + file_title + '.md'
        # ready_post/.md 문서 내 링크 변경, 사용한 사진 복사
        with open(file_name, 'r', encoding='utf-8') as md_file:
            lines = md_file.readlines()
            for line in lines:
                # tag value 가져오기
                if '---' in line:
                    define_bool = not define_bool
                    layer_path = cat_id + '/' + date_year + '/' + date_month + '/' + file_title
                    edited_lines.append(line)
                    continue
                if define_bool:
                    if re.search(CATE_EXP, line):
                        cat_id = line.split(' ')[1].strip()
                    if re.search(DATE_EXP, line):
                        now_date = datetime.now()
                        DATE_NAME = str(now_date.date())
                        date_year = str(now_date.year)
                        date_month = str(now_date.month)
                        line = line.split()[0] + ' ' + str(now_date).split('.')[0] + ' +0900\n'
                    edited_lines.append(line)
                    continue
                # [link[0-9]*]: 확인 
                if re.search(IMG_EXP, line):
                    # link 주소 변경
                    line = line.replace('{path}', '{{site.baseurl}}/images/' + layer_path)
                edited_lines.append(line)
            # ready_post/images 폴더를 baseUrl/images로 복사
            from_img_path = from_path + '/images'
            if os.path.exists(from_img_path):
                to_img_path = TO_IMG_PATH = parent_path + '/images/' + layer_path
                if os.path.exists(to_img_path):
                    shutil.rmtree(to_img_path)
                shutil.copytree(from_img_path, to_img_path)
        # ready_post의 md문서에 수정한 Link 적용
        with open(file_name, 'w', encoding='utf-8') as md_file:
            md_file.writelines(edited_lines)
        # ready_post에서 baseUrl/_post/로 복사
        to_post_path = TO_POST_PATH = parent_path + '/_posts/' + layer_path
        if not os.path.exists(to_post_path):
            os.makedirs(to_post_path)
        shutil.copy2(file_name, to_post_path + '/' + DATE_NAME + '-' + file_title + '.md')

def main():
    try:
        # target_post가 있는지 확인
        if get_sub_folder_list(FILE_PATH)[0]:
            # 이름과 내부 문법에 대해 양식을 맞춰 jekyll의 폴더로 복사
            prepare_posting_proc()
            # 추가된 포스트에 대해 publish 실시
            jekyll_publish_proc()
            messagebox.showinfo("Success", "Github Pages repo에\npush할 준비가 되었습니다.")
        else:
            messagebox.showinfo("Warning", "'0.create_layer_folders.py'를\n먼저 실행해주세요.")
    except:
        delete_group_folder(TO_POST_PATH, TO_IMG_PATH)
        messagebox.showinfo("Warning", "오류가 발생하였습니다.")


if __name__ == "__main__":
    main()
