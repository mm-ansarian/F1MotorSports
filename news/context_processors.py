def news_permissions(request):
    user = getattr(request, 'user', None)
    can_create_news = False
    can_show_news_menu = False
    if user and user.is_authenticated:
        can_create_news = user.is_staff and user.has_perm('news.add_news')
        can_show_news_menu = user.is_staff and user.has_perm('news.add_news')
    return {
        'can_create_news': can_create_news,
        'can_show_news_menu': can_show_news_menu,
    }
