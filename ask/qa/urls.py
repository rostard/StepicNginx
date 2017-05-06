
test='ask.qa.views.test'
urlpatterns = [
	url(r'^$',test),
	url(r'^login/',test),
	url(r'^signup/',test),
	url(r'^question/\d+/',test),
	url(r'^ask/',test),
	url(r'^popular/',test),
	url(r'^new/',test)
]
