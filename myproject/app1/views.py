from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app1.models import theme1
from app1.models import new
# from app1.models import srv1

# Create your views here.
# def mypage1(request):
#     ob1 = theme1()
#     ob1.img1 = "img/1-1.jpg"
#     ob1.name1 = 'Bootstrap v3.3.6'
#     ob1.cnt1 = 'Morbi sagittis justo a velit placerat ullamcorper quis quis velit. Sed convallis at risus ullamcorper auctor. Praesent quis velit neque. Quisque semper porta nisi vitae suscipit. Duis lectus magna, ornare ac scelerisque'
#     ob1.btn1 = 'button green'
#     ob2 = theme1()
#     ob2.img1 = "img/1-2.jpg"
#     ob2.name1 = 'Responsive Design'
#     ob2.cnt1 = 'Conquer Template is provided by templatemo for free of charge. You can use this template for any kind of website. No credit link is required. All images by '
#     ob2.btn1 = 'See Details'
#     ob3 = theme1()
#     ob3.img1 = "img/1-3.jpg"
#     ob3.name1 = 'Parallax Layout'
#     ob3.cnt1 = 'Morbi sagittis justo a velit placerat ullamcorper quis quis velit. Sed convallis at risus ullamcorper auctor. Praesent quis velit neque. Quisque semper porta nisi vitae suscipit. Duis lectus magna, ornare ac scelerisque'
#     ob3.btn1 = 'Button Red'
#     objimglist = [ob1, ob2, ob3]
#     l = [ob1, ob2, ob3]
#     return render(request,'index.html')
def mypage1(request):
    ob1=theme1()
    ob1.img1="img/1-1.jpg"
    ob1.name1='Bootstrap v3.3.6'
    ob1.namet='feature-content-title green-text'
    ob1.cnt1='Morbi sagittis justo a velit placerat ullamcorper quis quis velit. Sed convallis at risus ullamcorper auctor. Praesent quis velit neque. Quisque semper porta nisi vitae suscipit. Duis lectus magna, ornare ac scelerisque'
    ob1.btn1='button green'
    ob1.clr='green'
    ob1.clrt='feature-content-link green-btn'
    ob2=theme1()
    ob2.img1="img/1-2.jpg"
    ob2.name1='Responsive Design'
    ob2.namet='feature-content-title blue-text'
    ob2.cnt1='Conquer Template is provided by templatemo for free of charge. You can use this template for any kind of website. No credit link is required. All images by '
    ob2.btn1='See Details'
    ob2.clr='blue'
    ob2.clrt='feature-content-link blue-btn'
    ob3=theme1()
    ob3.img1="img/1-3.jpg"
    ob3.name1='Parallax Layout'
    ob3.namet='feature-content-title black-text'
    ob3.cnt1='Morbi sagittis justo a velit placerat ullamcorper quis quis velit. Sed convallis at risus ullamcorper auctor. Praesent quis velit neque. Quisque semper porta nisi vitae suscipit. Duis lectus magna, ornare ac scelerisque'
    ob3.btn1='Button Red'
    ob3.clr='red'
    ob3.clrt='feature-content-link red-btn'
    list1=[ob1,ob2,ob3]
    ob4 = theme1()
    ob4.img1 = "img/2-1.jpg"
    ob4.name1 = 'Two Column Left Side'
    ob4.cnt1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempor eros eget eros maximus, ut cursus sem euismod. Donec iaculis tristique odio at consectetur. Nullam dignissim varius suscipit. Sed in leo sit amet velit finibus pretium.Vestibulum vel mauris at erat mattis accumsan et ac lorem. Cras non venenatis orci, sed tincidunt massa. Duis nisl lectus, auctor eu sodales at, dignissim eu orci. Sed vitae venenatis magna, in blandit metus.'
    ob4.btn2='Read More'
    ob5 = theme1()
    ob5.img1 = "img/2-2.jpg"
    ob5.name1 = 'Two Column Right Side'
    ob5.cnt1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempor eros eget eros maximus, ut cursus sem euismod. Donec iaculis tristique odio at consectetur. Nullam dignissim varius suscipit. Sed in leo sit amet velit finibus pretium.Vestibulum vel mauris at erat mattis accumsan et ac lorem. Cras non venenatis orci, sed tincidunt massa. Duis nisl lectus, auctor eu sodales at, dignissim eu orci. Sed vitae venenatis magna, in blandit metus.'
    ob5.btn2='Read More'
    list2=[ob4,ob5]
    ob6 = theme1()
    ob6.img1 = "img/4-1.jpg"
    ob6.name1 = 'Column One'
    ob6.cnt1 = 'Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
    ob6.btn3='More'
    ob7 = theme1()
    ob7.img1 = "img/4-2.jpg"
    ob7.name1 = 'Column Two'
    ob7.cnt1 = 'Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
    ob7.btn3='Read It'
    ob8 = theme1()
    ob8.img1 = "img/4-3.jpg"
    ob8.name1 = 'Column Three'
    ob8.cnt1 = 'Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
    ob8.btn3='More'
    ob9 = theme1()
    ob9.img1 = "img/4-4.jpg"
    ob9.name1 = 'Column Four'
    ob9.cnt1 = 'Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
    ob9.btn3='Details'
    list3=[ob6,ob7,ob8,ob9]
    ob10=new()
    ob10.navbar='HomePage'
    ob10.section="#section1"
    ob11=new()
    ob11.navbar='About Us'
    ob11.section = "#section2"
    ob12=new()
    ob12.navbar='Service'
    ob12.section = "#section3"
    ob13=new()
    ob13.navbar='Contact'
    ob13.section = "#section4"
    # ob14=new()
    # ob14.navbar='Extra'
    # ob14.section = "#section5"
    l=[ob10,ob11,ob12,ob13]
    return render(request, 'index.html', {'key': l,'key1':list1,'key2':list2,'key3':list3})
#def twoclm(request):
    #ob4=clm()
    #ob4.img2="img/2-1.jpg"
    #ob4.name2='Two Column Left Side'
    #ob4.cnt2='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempor eros eget eros maximus, ut cursus sem euismod. Donec iaculis tristique odio at consectetur. Nullam dignissim varius suscipit. Sed in leo sit amet velit finibus pretium.Vestibulum vel mauris at erat mattis accumsan et ac lorem. Cras non venenatis orci, sed tincidunt massa. Duis nisl lectus, auctor eu sodales at, dignissim eu orci. Sed vitae venenatis magna, in blandit metus.'
    #ob5=clm()
    #ob5.img2="img/2-2.jpg"
    #ob5.name2='Two Column Right Side'
#     ob5.cnt2='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempor eros eget eros maximus, ut cursus sem euismod. Donec iaculis tristique odio at consectetur. Nullam dignissim varius suscipit. Sed in leo sit amet velit finibus pretium.Vestibulum vel mauris at erat mattis accumsan et ac lorem. Cras non venenatis orci, sed tincidunt massa. Duis nisl lectus, auctor eu sodales at, dignissim eu orci. Sed vitae venenatis magna, in blandit metus.'
#     objimglist = [ob4,ob5]
#     list=[ob4,ob5]
#     return render(request, 'index.html', {'key': list,'ob4':objimglist,'ob5':objimglist})
# def srve(request):
#     ob6=srv1()
#     ob6.img3="img/4-1.jpg"
#     ob6.name3='Column One'
#     ob6.cnt3='Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis. Fusce posuere egestas enim eu viverra.'
#     ob7=srv1()
#     ob7.img3="img/4-2.jpg"
#     ob7.name3='Column Two'
#     ob7.cnt3='Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
#     ob8=srv1()
#     ob8.img3="img/4-3.jpg"
#     ob8.name3='Column Three'
#     ob8.cnt3='Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis. Fusce posuere egestas enim eu viverra.'
#     ob9=srv1()
#     ob9.img3="img/4-4.jpg"
#     ob9.name3='Column Four'
#     ob9.cnt3='Ut ac odio scelerisque ante ornare commodo. Sed faucibus dui libero, in tincidunt purus pretium quis.'
#     piclist=[ob6,ob7,ob8,ob9]
#     list2=[ob6,ob7,ob8,ob9]
#     #return render(request, 'index.html', {'key': list2,'ob1':piclist,'ob2':piclist,'ob3':piclist,'ob4':piclist})
#     return render(request, 'index.html',{'key': list2, 'ob6': piclist, 'ob7': piclist, 'ob8': piclist, 'ob9': piclist})
#
