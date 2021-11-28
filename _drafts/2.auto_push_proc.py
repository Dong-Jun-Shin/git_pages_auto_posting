from tkinter import messagebox
from git import Repo, Actor

USER_AUTHOR = '{your_git_author_name}'
USER_EMAIL = '{your_git_email}'
SUMMARY = '{commit_summary}'
DESCRIPTION = '{commit_description}'

# ex. 'C:\\Users\\user\\Desktop\\example.github.io'
REPO_PATH = '{your_repo_path}'

def make_commit_message():
    ### 커밋 메세지 생성하기
    message = SUMMARY + '\n\n' + DESCRIPTION
    return message

def push_proc(repo):
    try:
        ### push 전 pull 실행
        pull_result = repo.remotes.origin.pull()[0]     # output >>> origin/main
        ### push 실행
        push_result = repo.remotes.origin.push()[0]
        messagebox.showinfo("Success", "Push가 완료되었습니다.")
    except:
        messagebox.showinfo("Warning", "충돌이 발생했습니다.\n해결 후 다시 시도해주세요.")

def commit_proc(repo):
    ### commit message 설정
    author = Actor(USER_AUTHOR, USER_EMAIL)        # 처음 만든 사람
    message = make_commit_message()

    ### git commit 생성
    r_index = repo.index
    changedFiles = [item.a_path for item in repo.index.diff(None)] + repo.untracked_files
    r_add_result = r_index.add(changedFiles)
    if r_add_result:
        r_index.commit(message, author=author)  # committer=committer 제외, committer = Actor("A committer", "tlsehdwns239@gmail.com") # 최근 수정한 사람
        messagebox.showinfo("Success", "Commit을 완료했습니다.\n확인 후 Push 해주세요.")
    else:
        messagebox.showinfo("Warning", "수정된 파일이 없습니다.")

def main():
    ### repo 정의
    repo = Repo(REPO_PATH)
    ### commit 실행
    commit_proc(repo)
    ### push 실행
    push_proc(repo)


if __name__ == "__main__":
    main()
