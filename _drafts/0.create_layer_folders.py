import os, shutil
from tkinter import messagebox

FILE_PATH = os.getcwd()
TO_PATH = ''
TO_IMG_PATH = ''

def delete_group_folder(to_path, to_img_path):
    # 예외 발생 시, 만들어진 폴더는 삭제
    if to_path:
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
    if to_img_path:
        if os.path.exists(to_img_path):
            shutil.rmtree(to_img_path)

def create_group_folder(file_names):
    global TO_PATH, TO_IMG_PATH
    for file_name in file_names:
        from_path = FILE_PATH + '/target_post'
        to_path = TO_PATH = FILE_PATH + '/ready_post/' + file_name.replace('.md', '')
        # .md 파일 복사
        if not os.path.exists(to_path):
            os.makedirs(to_path)
        shutil.copy2(from_path + '/' + file_name, to_path + '/' + file_name)
        # 해당 md에 사용된 img 폴더 복사
        from_img_path = from_path + '/' + file_name.replace('.md', '')
        to_img_path = TO_IMG_PATH = to_path + '/images'
        if os.path.exists(from_img_path):
            if os.path.exists(to_img_path):
                shutil.rmtree(to_img_path)
            shutil.copytree(from_img_path, to_img_path)

def main():
    try:
        file_names = [_ for _ in os.listdir(FILE_PATH + '/target_post') if _.endswith(r".md")]
        if file_names:
            create_group_folder(file_names)
            messagebox.showinfo("Success", "파일 분류 및 태그 수정이\n완료되었습니다.")
        else:
            messagebox.showinfo("Warning", "포스팅할 md파일을\n'target_post'에 준비해주세요.")
    except:
        delete_group_folder(TO_PATH, TO_IMG_PATH)
        messagebox.showinfo("Warning", "오류가 발생하였습니다.")


if __name__ == "__main__":
    main()
