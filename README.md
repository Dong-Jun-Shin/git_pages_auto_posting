# Github_pages_auto_posting

 - Github Pages로 블로그를 운영할 때, 작성한 글을 자동으로 포스팅하기 위해 만든 tool입니다.
 - \_post 및 images 폴더에 파일 관리하는 방식에 따라 소스코드에서 경로를 수정 후, 사용하셔야 합니다.
 - repo에 대한 정보와 author, message 정보를 수정 후, 사용하셔야 합니다.
 - 문의사항이 있으실 경우, Issues에 등록해주시거나 메일로 연락 부탁드립니다.

## Description

1. 'ready_post':
    - \_post와 images에 배포되기 전, 작업이 완료된 파일이 위치하는 폴더입니다.
2. 'target_post':
    - {title}.md 파일과 {title}(이미지 폴더)가 위치하는 폴더입니다.
3. '0.create_layer_folders.py':  
    - target_post 안에 있는 {title}.md파일들과 {title}(이미지 폴더)들을 복사합니다.  
    - ready_post/{title}/ 경로에 {title}.md와 images(이미지 폴더) 구성으로 복사됩니다.  
4. '1.prepare_posting_proc.py':  
    - ready_post 경로 안의 {title} 폴더마다 작업을 반복합니다.  
      - 파일 내의 tags 중 date 태그에 현재 날짜와 시간을 'yyyy-mm-dd HH:MM:ss +0900' 포맷으로 추가합니다.  
      - 파일 내의 {path}라 정의된 이미지 태그의 경로를 '{{site_baseurl}}/images/{categories}/{date_year}/{date_month}/{file_title}'으로 변경합니다.  
      - .md 파일에 사용된 이미지들을 '{블로그 root 폴더}/images/{categories}/{date_year}/{date_month}/{file_title}'의 위치에 복사합니다.  
      - .md 파일의 이름을 '{블로그 root 폴더}/_posts/{categories}/{date_year}/{date_month}/{file_title}/yyyy-mm-dd-{title}.md'로 복사합니다.  
    - target_post에 존재하는 포스팅에 대해 작업이 완료되면, jekyll의 build를 통해 post를 publish합니다.  
5. '2.auto_push_proc.py':  
    - 지정된 repo의 변경된 파일들에 대해서, commit을 수행합니다.  
    - push 전, pull을 수행합니다.  
    - push를 수행합니다.  

## Getting Started

### Dependencies

- Python 3.8.3
- GitPython 3.1.24

### Installing

- Gemfile이 위치한 블로그 root 폴더에 아래와 같은 구조를 만들고, 0~2.py를 위치시킵니다.
- \_drafts(folder)  
  └ ready_post(folder)  
  └ target_post(folder)  
  └ 0.create_layer_folders.py  
  └ 1.prepare_posting_proc.py  
  └ 2.auto_commit_proc.py  

### Executing program

1. 외부 Markdown 에디터로 작성하고 내보낸 .md파일과 이미지를 target_post에 위치시킵니다.  
  (여기서 이미지 폴더의 이름은 이미지가 사용된 .md파일의 이름과 일치시킵니다.)  
2. '0.create_layer_folders.py'을 실행시킵니다.  
3. '1.prepare_posting_proc.py'을 실행시킵니다.  
4. '2.auto_push_proc.py'을 실행시킵니다.  

## Authors

Contributors names and contact info  
[@Dongjun Shin](https://dong-jun-shin.github.io/about/profile)

## Version History
* 0.1
    * Initial Release
