from rest_framework import serializers
from audiobook.models import Book
from .models import Post, User, Comment,Inquiry

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'post_title', 'post_content']
        
    def save(self, **kwargs):
        book_id = self.context.get('book_id')
        user_id = self.context.get('user_id')
        # 현재 로그인 유저
        user = User.objects.get(pk=user_id)
        # 현재 선택된 책
        book = Book.objects.get(pk=book_id)
        self.validated_data['user'] = user
        self.validated_data['book'] = book

        return super().save(**kwargs)
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_content']
        
    def save(self, **kwargs):
        post_id = self.context['post_id']
        # 수정 필요: 로그인
        # 현재 로그인 유저
        user = User.objects.get(pk=1)
        # 현재 선택된 게시물
        post = Post.objects.get(pk=post_id)
        self.validated_data['user'] = user
        self.validated_data['post'] = post

        return super().save(**kwargs)
    
    
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'