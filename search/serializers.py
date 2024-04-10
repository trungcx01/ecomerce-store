# from rest_framework import serializers
#
# from book.models import BookCategory, Book
# from clothes.models import ClothesCategory, Clothes
# from mobile.models import MobileCategory, Mobile
#
#
# class CategorySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = BookCategory
# 		fields = '__all__'
#
# class BookSerializer(serializers.ModelSerializer):
# 	categories = CategorySerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Book
# 		fields = '__all__'
#
#
# class ClothesCategorySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ClothesCategory
# 		fields = '__all__'
#
#
# class ClothesSerializer(serializers.ModelSerializer):
# 	categories = ClothesCategorySerializer(many=True, read_only=True)
#
# 	class Meta:
# 		model = Clothes
# 		fields = '__all__'
#
# class MobileCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MobileCategory
#         fields = '__all__'
#
#
# class MobileSerializer(serializers.ModelSerializer):
#     categories = MobileCategorySerializer(many=True, read_only=True)
#     class Meta:
#         model = Mobile
#         fields = '__all__'
