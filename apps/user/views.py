from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import WxUserProfile, UserProfile
from apps.user.serializers import WxLoginSerializer
from apps.utils.wxChecker import checkdata


class WxLoginView(APIView):

    def post(self, request):
        """
        用户扫码登陆
        :param request:
        :return:
        """
        wx_data = WxLoginSerializer(data=request.data)
        if wx_data.is_valid():
            code = wx_data.validated_data.get('code')
            encrypteddata = wx_data.validated_data.get('encrypteddata')
            iv = wx_data.validated_data.get('iv')

            # 检查用户
            res = checkdata(code, encrypteddata, iv)

            errorinfo = res.get('error', None)
            if errorinfo:
                print(errorinfo, "错误的信息！")
                return Response(status=status.HTTP_400_BAD_REQUEST, data=errorinfo)
            openid = res['openId']

            # 创建新用户
            s = WxUserProfile.objects.filter(openid=openid).first()
            if s:
                # res["role"] = s.get_role()
                # if res["role"] == 'null':
                #     res["uid"] = 'null'
                # else:
                #     res["uid"] = s.student.id
                s.cookie = res["cookie"]
                s.save()
            else:
                # TODO (yxc): 如何做好事物

                # first create a commonUser

                new_common_user = UserProfile.objects.create(
                    username=res["nickName"],
                )

                # then create a wxUser
                new_user = WxUserProfile.objects.create(
                    openid=openid,
                    cookie=res['cookie'],
                    nickname=res['nickName'],
                    city=res['city'],
                    province=res['province'],
                    gender=res['gender'],
                    country=res['country'],
                    avatar_url=res['avatarUrl'],
                    uesr=new_common_user
                )
                # then create a System User
                new_user.set_password(raw_password=openid)
                new_user.save()
                res["role"] = "null"
                res["uid"] = "null"
            return Response(status=status.HTTP_201_CREATED, data=res)
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST, data=wx_data.error_messages)
