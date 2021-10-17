---
layout: post
category: django
tag: [입문, 위코드, TIL, 프로젝트]
title: 위코드 두번째 프로젝트 험블벅 3 카카오 소셜로그인, 최종 구현 영상
---

## 험블벅 최종 구현 영상

<iframe width="560" height="315" src="https://www.youtube.com/embed/qUSai5QtndI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 카카오 소셜로그인

먼저 [공식문서](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api)에 나와있는대로 카카오디벨로퍼스에 웹 플랫폼 및 도메인 정보를 등록한다.

![소셜로그인](/public/img/social_login.png)

프론트에서 카카오 로그인을 통해 토큰을 받을 수 있는 인증코드를 받고, 이 인증코드를 통해서 API를 호출 할 수 있는 사용자 토큰(Access Token, Refresh Token)을 카카오로부터 받아서 header에 담아 백엔드에 보내준다.

### Request

```shell
GET/POST /v2/user/me HTTP/1.1  
Host: kapi.kakao.com  
Authorization: Bearer {access_token}  
Content-type: application/x-www-form-urlencoded;charset=utf-8  
```

### 백엔드 코드
```python
class KakaologinView(View):
    def get(self, request):
        try:
            access_token = request.headers.get("Authorization")
            #프론트에서 헤더스에 담아보낸 토큰 받기
            if not access_token:
                return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
                
            response = requests.get(
                    "https://kapi.kakao.com/v2/user/me", 
                    headers = {"Authorization" : f"Bearer {access_token}"}
                    )
            #{Authorization: bearer+access_token}의 양식으로 kakao에 사용자 정보 reqeust를 보낸다
                    
            if not response:
                    return JsonResponse({"message" : "NOT_FOUND_IN_KAKAO"}, status = 404)
                    
            profile_json  = response.json()
                
            kakao_id      = profile_json.get("id")
            kakao_account = profile_json.get("kakao_account")
            name          = kakao_account["profile"]["nickname"]
            #카카오에서 kakao_id, kakao_account, kakao_account.profile.nickname 받기
            
            if not User.objects.filter(kakao = kakao_id).exists():
                User.objects.create(
                            kakao     = kakao_id,
                            nickname      = name,
                )
            #험블벅 db와 유저정보 비교 후 존재하지 않으면 새로운 유저정보 생성 
            user           = User.objects.get(kakao = kakao_id)
            #험블벅 db와 유저정보 비교 후 존재하면 유저를 가져와서
            user.name      = name
            #이름을 넣고
            user.save()
            #저장

            token = jwt.encode({"id" : user.id}, SECRET_KEY, algorithm = "HS256")
            #토큰 발행
			
		    return JsonResponse({"message" : "SUCCESS", "acess_token" : token}, status = 200)
		except KeyError:
		    return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
```

카카오에서 받게 되는 profile_json데이터는 아래와 같이 생겼다.

```json
{
    'id': 1855599935,
    'connected_at': '2021-08-18T08:54:05Z',
    'properties':
        {
        'nickname': '한효주'
        },
    'kakao_account':
        {'profile_nickname_needs_agreement': False,
         'profile':
            {'nickname': '한효주'},
         'has_email': True,
         'email_needs_agreement': False,
         'is_email_valid': True,
         'is_email_verified': True,
         'email': 'hyojoo@gmail.com'
        }
}
```

