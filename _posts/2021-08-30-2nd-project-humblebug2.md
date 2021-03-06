---
layout: post
category: django
tag: [입문, 위코드, TIL, 프로젝트]
title: 위코드 두번째 프로젝트 험블벅 2 AWS S3 코드, 리팩토링
---

## 텀블벅 클론코딩 

2차 프로젝트로 험블벅을 클론코딩하면서 프로젝트 이미지를 AWS S3서버에 올리는 코드를 작성했다.  

https://github.com/boto/boto3/tree/develop/docs/source/guide  

여기에 들어가보면 AWS공식 라이브러리인 boto3를 쓰는 예시가 자세히 잘 나와있다. 
예를 들어서 Access permission을 받는 코드는 다음과 같다.  

![permission](/public/img/aws_access_permission.png)

### AWS S3 권한 설정

권한 관리를 위해서 버킷 정책을 아래와같이 작성했다. 프로젝트 이미지라서 비회원한테도 보여야되니까 퍼블릭 엑세스 차단을 전부 해제했다.

*** 권한 설정 비디오 튜토리얼 ***

<iframe width="560" height="315" src="https://www.youtube.com/embed/dGM53tHXGfY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

버킷 정책은 아래와 같이 했는데 버킷정책에 대한 자세한 내용은 AWS 사용설명서에 나와있는걸 읽어보면 된다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/example-policies-s3.html

```python
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StatementSid1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::182260599663:user/sang*****"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::humble/*"
        },
        {
            "Sid": "StatementSid2",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::humble/*"
        }
    ]
}
```
```python
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://www.example1.com"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

### AWS S3액세스, ProjectView post

프로젝트를 업로드하는 뷰인데 이미지 파일 업로드가 함께 들어가있다

```python
class ProjectView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user
            data = request.POST

            image = request.FILES.get('image')
            #폼데이터로 받은 파일을 이미지 변수에 넣는다
            input_date = data.get('end_date')

            if not image:
                return JsonResponse({'MESSAGE' : 'IMAGE_EMPTY'}, status=400)

            upload_key = str(uuid.uuid4()) + image.name
            #uuid와 이미지 이름으로 키를 생성한다
            s3_client = boto3.client(
                's3',
                aws_access_key_id     = ACCESS_KEY_ID,
                aws_secret_access_key = SECRET_ACCESS_KEY,
            )
            #s3서버에 접근한다

            Project.objects.create(
                name           = data.get('name'),
                user_id        = user.id,
                aim_amount     = data.get('aim_amount'),
                description    = data.get('description'),
                end_date       = input_date[6:10]+'-'+input_date[:2]+'-'+input_date[3:5],
                category_id    = data.get('category_id'),
                main_image_url = 'https://humblebug.s3.us-east-2.amazonaws.com/' + upload_key
                #aws버킷경로와 업로드 키를 포함한 URL을 저장한다. 이렇게 하고 퍼블릭 엑세스를 해제하면 url을 클릭했을 때 브라우저에서 바로 이미지가 나온다.  
            )

            s3_client.upload_fileobj(
                image,
                BUCKET_NAME,
                upload_key,
                ExtraArgs = {
                    'ContentType' : image.content_type #확장자였나..?
                }
            )
            #s3서버에 이미지를 업로드한다

            return JsonResponse({'MESSAGE':'SUCCESS'},status = 201)
    
        except KeyError:
            return JsonResponse({'MESSAGE':'ERROR_INPUT_VALUE'}, status=404) 
```

이런 방식으로 쓰면 이미지 파일 수정 및 삭제할 때도 액세스 코드를 계속 써야되고 멘토님께서 나중에 키가 바뀌거나 아마존이 아닌 구글로 서비스업체를 바꾼다던지 했을 때 유지/보수 및 디버깅이 쉽게 하기 위해서 아래와 같이 리팩토링할 것을 조언해주셨다.

### AWS S3 관련 코드 리팩토링

```python
class CloudStorage:
    def __init__(self, ACCESS_KEY_ID, SECRET_ACCESS_KEY, BUCKET_NAME):
        self.ACCESS_KEY_ID = ACCESS_KEY_ID
        self.SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
        self.BUCKET_NAME = BUCKET_NAME
        self.client = boto3.client(
                's3',
                aws_access_key_id     = ACCESS_KEY_ID,
                aws_secret_access_key = SECRET_ACCESS_KEY,
            )
        self.resource = boto3.resource(
                's3',
                aws_access_key_id     = ACCESS_KEY_ID,
                aws_secret_access_key = SECRET_ACCESS_KEY,
            )
    #AWS 관련 데이터를 변수로 넣는다
        
    def upload_file(self, file):
        file_url = "사용하는 회사의 aws url.ap-northeast-2.rds.amazonaws.com/" + str(uuid.uuid1()) + file.name
        self.client.upload_fileobj(
                        file,
                        self.BUCKET_NAME,
                        file_url,
                        ExtraArgs={
                            "ContentType": file.content_type
                        }
        )
        return file_url

    def delete_file(self, file_url, project_id):
        main_image_url = Project.objects.get(id=project_id).file_url
        bucket = self.resource.Bucket(name=BUCKET_NAME)
        bucket.Object(key = file_url).delete()
    #AWS관련 액션들을 매쏘드로 넣는다

class ProjectUpload(View):
    @login_decorator
    def post(self, request):
        cloud_storage = CloudStorage(ACCESS_KEY_ID, SECRET_ACCESS_KEY, BUCKET_NAME)
        try:
            data = request.POST

            if request.FILES:
                file_url = (cloud_storage.upload_file(file))
                #그러면 이렇게 한 줄로 업로드하고 리턴 받은 url을 가져와서 사용할 수 있다.

            if not request.FILES:
                return JsonResponse({'MESSAGE' : 'IMAGE_EMPTY'}, status=400)

            Project.objects.create(
                    name           = data.get('name'),
                    user_id        = request.user.id,
                    aim_amount     = data.get('aim_amount'),
                    description    = data.get('description'),
                    end_date       = data.get('end_date')[0:4]+'-'+data.get('end_date')[5:7]+'-'+data.get('end_date')[8:10],
                    category_id    = data.get('category_id'),
                    main_image_url = file_url
                    #삭제하고 싶을 때는 앞에 url을 빼고 키값만 넣어줘야한다.
                    )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE':'ERROR_INPUT_VALUE'}, status=404)
```

### 그 외 이미지 수정/삭제 코드

```python
class ProjectModify(View):
    @login_decorator
    def post(self, request, project_id):
        try:
            data = request.POST

            if not Project.objects.filter(id=project_id, user_id=request.user.id).exists():
                return JsonResponse({'MESSAGE':'NOT_EXISTS'}, status=400)

            if request.FILES:
                cloud_storage.delete_file(file, file_url)
                file_url = (cloud_storage.upload_file(file))
                
            if not file:
                main_image_url = Project.objects.get(id=project_id).main_image_url

            Project.objects.filter(id=project_id, user_id=request.user.id).update(
                    name           = data.get('name'),
                    user_id        = request.user.id,
                    aim_amount     = data.get('aim_amount'),
                    description    = data.get('description'),
                    end_date       = data.get('end_date')[0:4]+'-'+data.get('end_date')[5:7]+'-'+data.get('end_date')[8:10],
                    category_id    = data.get('category_id'),
                    file_url = file_url
                    )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE':'ERROR_INPUT_VALUE'}, status=404)

    @login_decorator
    def delete(self, request, project_id):
        cloud_storage = CloudStorage(ACCESS_KEY_ID, SECRET_ACCESS_KEY, BUCKET_NAME)
        user = request.user

        if not Project.objects.filter(id=project_id, user_id=user.id).exists():
            return JsonResponse({'MESSAGE':'NOT_EXISTS'}, status=400)
        
        file_url = Project.objects.get(id=project_id).file_url        
        cloud_storage.delete_file(file_url, project_id)

        Project.objects.get(id=project_id, user_id=user.id).delete()

        return JsonResponse({"MESSAGE": 'SUCCESS'}, status=204)
```

### 쉘을 통해서 AWS s3서버에서 이미지 삭제하는 코드

```python
import boto3
ACCESS_KEY_ID = '**********'
SECRET_ACCESS_KEY = '******************'
BUCKET_NAME = '[name of your bucket]'
s3_client = boto3.client(
                 's3',
                 aws_access_key_id     = ACCESS_KEY_ID,
                 aws_secret_access_key = SECRET_ACCESS_KEY,
             )
s3_resource = boto3.resource(
                 's3',
                 aws_access_key_id     = ACCESS_KEY_ID,
                 aws_secret_access_key = SECRET_ACCESS_KEY,
             )
bucket = s3_resource.Bucket(name='버켓 이름')
#삭제하는 명령어1
bucket.Object('키값, 예를 들어 d457d1b0-169d-487a-950f-ef0cca576ad01.png').delete()
#삭제하는 명령어2
s3_client.delete_object(Bucket='humble', Key ='d457d1b0-169d-487a-950f-ef0cca576ad01.png')
```