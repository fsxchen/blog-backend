'''
Author: yangxingchen
Date: 2019-04-25 14:42:35
LastEditors: yangxingchen
LastEditTime: 2020-08-19 19:20:03
Description: 
'''
# _*_ coding: utf-8 _*_
__author__ = 'LennonChin'
__date__ = '2017/12/9 13:31'

from rest_framework import serializers

from .models import SiteInfo, BloggerInfo, NavigationLink, FriendLink
from material.serializers import MaterialMasterSerializer, MaterialSocialSerializer
from project.settings import MEDIA_URL_PREFIX, PHOTO_URL


class NavigationLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationLink
        fields = "__all__"


class SiteInfoSerializer(serializers.ModelSerializer):
    navigations = NavigationLinkSerializer(many=True)
    icon = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    def get_icon(self, site_info):
        if site_info.icon:
            return "{0}/{1}".format(MEDIA_URL_PREFIX, site_info.icon)

    def get_background(self, blogger_info):
        if blogger_info.background:
            return "http://{0}/{1}".format(PHOTO_URL, blogger_info.background)

    class Meta:
        model = SiteInfo
        fields = (
            'name', 'en_name', 'desc', 'en_desc', 'keywords', 'icon', 'background', 'api_base_url', 'is_live',
            'is_force_refresh', 'force_refresh_time', 'navigations', 'copyright', 'copyright_desc', 'copyright_desc_en',
            'icp')


class BloggerInfoSerializer(serializers.ModelSerializer):
    socials = MaterialSocialSerializer(many=True)
    masters = MaterialMasterSerializer(many=True)
    avatar = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    def get_avatar(self, blogger_info):
        if blogger_info.avatar:
            return "{0}/{1}".format(MEDIA_URL_PREFIX, blogger_info.avatar)

    def get_background(self, blogger_info):
        if blogger_info.background:
            return "{0}/{1}".format(MEDIA_URL_PREFIX, blogger_info.background)

    class Meta:
        model = BloggerInfo
        fields = "__all__"


class FriendLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendLink
        fields = "__all__"
